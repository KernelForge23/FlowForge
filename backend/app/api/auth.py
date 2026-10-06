from dataclasses import dataclass
from typing import Annotated

import httpx
from fastapi import Header, HTTPException

from app.config import settings


@dataclass(frozen=True)
class AuthenticatedUser:
    id: str
    email: str


def current_user(
    authorization: Annotated[str | None, Header()] = None,
) -> AuthenticatedUser | None:
    if not settings.supabase_url:
        return None
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authentication required")
    try:
        response = httpx.get(
            f"{settings.supabase_url.rstrip('/')}/auth/v1/user",
            headers={
                "Authorization": authorization,
                "apikey": settings.supabase_anon_key,
            },
            timeout=5.0,
        )
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail="Authentication service unavailable") from exc
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    data = response.json()
    user_id = data.get("id")
    email = data.get("email")
    if not isinstance(user_id, str) or not isinstance(email, str):
        raise HTTPException(status_code=401, detail="Invalid authentication response")
    return AuthenticatedUser(id=user_id, email=email)
