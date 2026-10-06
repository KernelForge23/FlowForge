from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qs, urlparse
from unittest.mock import Mock, patch

from cryptography.fernet import Fernet

from app.config import settings
from app.api.auth import AuthenticatedUser, current_user
from app.core.event import Event, ExecutionContext
from app.core.actions.email import EmailAction
from app.db import get_session
from app.main import app
from app.models import GmailConnection, User
from app.services.gmail import GmailService


def test_gmail_action_sends_message_without_exposing_token(db_session, monkeypatch) -> None:
    key = Fernet.generate_key().decode()
    monkeypatch.setattr(settings, "token_encryption_key", key)
    monkeypatch.setattr(settings, "email_provider", "gmail")
    user = User(email="gmail@example.com")
    db_session.add(user)
    db_session.flush()
    GmailService(db_session).save_connection(
        user.id,
        "sender@gmail.com",
        "access-token",
        "refresh-token",
        datetime.now(timezone.utc) + timedelta(hours=1),
    )
    response = Mock(status_code=200)
    response.json.return_value = {"id": "gmail-message-1"}

    with patch("app.services.gmail.httpx.post", return_value=response) as request:
        context = ExecutionContext(Event(type="manual", source="test"), user_id=user.id)
        EmailAction(
            {"to": ["recipient@example.com"], "subject": "Test", "text": "Body"},
            gmail_service=GmailService(db_session),
        ).execute(context)

    assert context.data["action_results"] == [
        {"type": "email", "provider": "gmail", "status": "sent", "provider_id": "gmail-message-1"}
    ]
    assert request.call_args.kwargs["headers"]["Authorization"] == "Bearer access-token"
    assert "refresh-token" not in str(context.data)
    assert "access-token" not in str(context.data)


def test_gmail_service_rejects_missing_connection(db_session, monkeypatch) -> None:
    monkeypatch.setattr(settings, "token_encryption_key", Fernet.generate_key().decode())
    service = GmailService(db_session)

    try:
        service.send("missing-user", ["recipient@example.com"], "Test", "Body", None)
    except RuntimeError as exc:
        assert str(exc) == "Connect Gmail before using the email action"
    else:
        raise AssertionError("Expected missing Gmail connection to fail")


def test_gmail_connect_and_callback_store_user_connection(client, db_session, monkeypatch) -> None:
    user = User(id="supabase-user", email="user@example.com")
    db_session.add(user)
    db_session.commit()
    authenticated = AuthenticatedUser(id=user.id, email=user.email)
    def override_session():
        yield db_session

    app.dependency_overrides[get_session] = override_session
    app.dependency_overrides[current_user] = lambda: authenticated
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(settings, "token_encryption_key", Fernet.generate_key().decode())
    try:
        connect = client.get("/api/integrations/gmail/connect")
        assert connect.status_code == 200
        authorization_url = connect.json()["authorization_url"]
        assert "state=" in authorization_url
        query = parse_qs(urlparse(authorization_url).query)
        assert query["scope"][0] == "openid email https://www.googleapis.com/auth/gmail.send"
        state = query["state"][0]

        monkeypatch.setattr(
            GmailService,
            "exchange_code",
            lambda _service, _code: (
                "access-token",
                "refresh-token",
                datetime.now(timezone.utc) + timedelta(hours=1),
            ),
        )
        monkeypatch.setattr(GmailService, "profile", lambda _service, _token: "user@gmail.com")
        callback = client.get(
            f"/api/integrations/gmail/callback?code=oauth-code&state={state}",
            follow_redirects=False,
        )

        assert callback.status_code == 302
        assert "gmail=connected" in callback.headers["location"]
        assert GmailService(db_session).connection(user.id).email == "user@gmail.com"
    finally:
        app.dependency_overrides.clear()
