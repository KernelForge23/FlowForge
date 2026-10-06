from datetime import datetime, timedelta, timezone
from urllib.parse import urlencode

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.api.auth import AuthenticatedUser, current_user
from app.config import settings
from app.db import get_session
from app.models import GmailOAuthState, User
from app.services.gmail import GmailService, new_oauth_state

router = APIRouter(prefix="/api/integrations/gmail", tags=["integrations"])


def _require_user(user: AuthenticatedUser | None) -> AuthenticatedUser:
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user


@router.get("/connect")
def connect_gmail(
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> dict[str, str]:
    user = _require_user(authenticated_user)
    if session.get(User, user.id) is None:
        session.add(User(id=user.id, email=user.email))
        session.flush()
    state = new_oauth_state()
    session.add(
        GmailOAuthState(
            state_hash=GmailService.hash_state(state),
            user_id=user.id,
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=10),
        )
    )
    try:
        destination = GmailService(session).oauth_url(state)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return {"authorization_url": destination}


@router.get("/callback")
def gmail_callback(
    code: str | None = None,
    state: str | None = None,
    error: str | None = None,
    session: Session = Depends(get_session),
) -> RedirectResponse:
    params = {"gmail": "error"}
    if error or not code or not state:
        params["reason"] = "authorization_cancelled"
    else:
        oauth_state = (
            session.query(GmailOAuthState)
            .filter_by(state_hash=GmailService.hash_state(state))
            .one_or_none()
        )
        now = datetime.now(timezone.utc)
        expires_at = oauth_state.expires_at if oauth_state is not None else None
        if expires_at is not None and expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if oauth_state is None or oauth_state.used_at is not None or expires_at < now:
            params["reason"] = "invalid_authorization_state"
        else:
            oauth_state.used_at = now
            try:
                service = GmailService(session)
                access_token, refresh_token, expires_at = service.exchange_code(code)
                email = service.profile(access_token)
                service.save_connection(
                    oauth_state.user_id, email, access_token, refresh_token, expires_at
                )
                params = {"gmail": "connected"}
            except RuntimeError as exc:
                params["reason"] = "authorization_failed"
                params["detail"] = str(exc)
    return RedirectResponse(
        f"{settings.frontend_origin}/?{urlencode(params)}",
        status_code=302,
    )


@router.get("/status")
def gmail_status(
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> dict[str, object]:
    user = _require_user(authenticated_user)
    connection = GmailService(session).connection(user.id)
    return {"connected": connection is not None, "email": connection.email if connection else None}


@router.delete("")
def disconnect_gmail(
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> None:
    user = _require_user(authenticated_user)
    GmailService(session).disconnect(user.id)
