import base64
import hashlib
import secrets
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import formataddr
from urllib.parse import urlencode

import httpx
from cryptography.fernet import Fernet, InvalidToken
from sqlalchemy.orm import Session

from app.config import settings
from app.models import GmailConnection


class GmailService:
    def __init__(self, session: Session) -> None:
        self.session = session

    @staticmethod
    def _cipher() -> Fernet:
        if not settings.token_encryption_key:
            raise RuntimeError("Gmail token encryption is not configured")
        try:
            return Fernet(settings.token_encryption_key.encode())
        except (ValueError, TypeError) as exc:
            raise RuntimeError("Gmail token encryption key is invalid") from exc

    @staticmethod
    def hash_state(state: str) -> str:
        return hashlib.sha256(state.encode()).hexdigest()

    def oauth_url(self, state: str) -> str:
        if not settings.google_client_id or not settings.google_client_secret:
            raise RuntimeError("Google OAuth is not configured")
        query = urlencode(
            {
                "client_id": settings.google_client_id,
                "redirect_uri": settings.google_redirect_uri,
                "response_type": "code",
                "scope": "openid email https://www.googleapis.com/auth/gmail.send",
                "access_type": "offline",
                "prompt": "consent",
                "state": state,
            }
        )
        return f"https://accounts.google.com/o/oauth2/v2/auth?{query}"

    def exchange_code(self, code: str) -> tuple[str, str, datetime]:
        response = httpx.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": settings.google_client_id,
                "client_secret": settings.google_client_secret,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": settings.google_redirect_uri,
            },
            timeout=10.0,
        )
        if response.status_code != 200:
            try:
                error = response.json().get("error")
                description = response.json().get("error_description")
            except ValueError:
                error = None
                description = None
            detail = error if isinstance(error, str) else "unknown_error"
            if isinstance(description, str) and description:
                detail = f"{detail}: {description}"
            raise RuntimeError(f"Google OAuth token exchange failed ({detail})")
        data = response.json()
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")
        expires_in = data.get("expires_in")
        if not all(isinstance(item, str) for item in (access_token, refresh_token)) or not isinstance(
            expires_in, int
        ):
            raise RuntimeError("Google OAuth response was invalid")
        return access_token, refresh_token, datetime.now(timezone.utc) + timedelta(seconds=expires_in)

    def profile(self, access_token: str) -> str:
        response = httpx.get(
            "https://openidconnect.googleapis.com/v1/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=10.0,
        )
        if response.status_code != 200:
            raise RuntimeError(f"Could not read the Gmail profile (status {response.status_code})")
        email = response.json().get("email")
        if not isinstance(email, str) or "@" not in email:
            raise RuntimeError("Google did not return a valid Gmail address")
        return email

    def save_connection(
        self, user_id: str, email: str, access_token: str, refresh_token: str, expires_at: datetime
    ) -> GmailConnection:
        connection = self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()
        if connection is None:
            connection = GmailConnection(user_id=user_id, email=email, access_token="", refresh_token="")
            self.session.add(connection)
        cipher = self._cipher()
        connection.email = email
        connection.access_token = cipher.encrypt(access_token.encode()).decode()
        connection.refresh_token = cipher.encrypt(refresh_token.encode()).decode()
        connection.token_expires_at = expires_at
        self.session.flush()
        return connection

    def disconnect(self, user_id: str) -> None:
        connection = self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()
        if connection is not None:
            self.session.delete(connection)
            self.session.flush()

    def connection(self, user_id: str) -> GmailConnection | None:
        return self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()

    def _decrypt(self, value: str) -> str:
        try:
            return self._cipher().decrypt(value.encode()).decode()
        except (InvalidToken, UnicodeDecodeError) as exc:
            raise RuntimeError("Stored Gmail credentials are invalid") from exc

    def _refresh(self, connection: GmailConnection, refresh_token: str) -> str:
        response = httpx.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": settings.google_client_id,
                "client_secret": settings.google_client_secret,
                "refresh_token": refresh_token,
                "grant_type": "refresh_token",
            },
            timeout=10.0,
        )
        if response.status_code != 200:
            raise RuntimeError("Gmail authorization expired; reconnect Gmail")
        access_token = response.json().get("access_token")
        expires_in = response.json().get("expires_in", 3600)
        if not isinstance(access_token, str) or not isinstance(expires_in, int):
            raise RuntimeError("Gmail token refresh response was invalid")
        connection.access_token = self._cipher().encrypt(access_token.encode()).decode()
        connection.token_expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
        self.session.flush()
        return access_token

    def send(
        self,
        user_id: str,
        recipients: list[str],
        subject: str,
        text: str,
        html: str | None,
        sender: str | None = None,
    ) -> dict[str, object]:
        connection = self.connection(user_id)
        if connection is None:
            raise RuntimeError("Connect Gmail before using the email action")
        access_token = self._decrypt(connection.access_token)
        refresh_token = self._decrypt(connection.refresh_token)
        expires_at = connection.token_expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at <= datetime.now(timezone.utc) + timedelta(minutes=1):
            access_token = self._refresh(connection, refresh_token)

        message = EmailMessage()
        message["From"] = formataddr(("FlowForge", connection.email))
        message["To"] = ", ".join(recipients)
        message["Subject"] = subject
        message.set_content(text)
        if html:
            message.add_alternative(html, subtype="html")
        encoded = base64.urlsafe_b64encode(message.as_bytes()).decode()
        response = httpx.post(
            "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
            headers={"Authorization": f"Bearer {access_token}"},
            json={"raw": encoded},
            timeout=settings.http_action_timeout_seconds,
        )
        if response.status_code >= 400:
            raise RuntimeError(f"Gmail API returned status {response.status_code}")
        provider_id = response.json().get("id")
        result: dict[str, object] = {"type": "email", "provider": "gmail", "status": "sent"}
        if isinstance(provider_id, str):
            result["provider_id"] = provider_id
        return result


def new_oauth_state() -> str:
    return secrets.token_urlsafe(32)
