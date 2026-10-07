from unittest.mock import MagicMock, Mock, patch

import pytest

from app.core.actions.github import GitHubAction
from app.core.actions.email import EmailAction
from app.core.actions.http import HttpAction
from app.core.event import Event, ExecutionContext


def test_http_action_rejects_private_addresses() -> None:
    with pytest.raises(ValueError, match="private or local"):
        HttpAction({"url": "http://127.0.0.1:8080/hook"})


def test_http_action_rejects_unsupported_scheme() -> None:
    with pytest.raises(ValueError, match="http or https"):
        HttpAction({"url": "file:///etc/passwd"})


@patch("app.core.actions.http.httpx.Client")
def test_http_action_records_status_without_response_body(mock_client: Mock) -> None:
    response = Mock()
    response.is_error = False
    response.status_code = 204
    mock_client.return_value.__enter__.return_value.send.return_value = response

    context = ExecutionContext(Event(type="manual", source="test"))
    HttpAction({"url": "https://8.8.8.8/hook", "body": {"ok": True}}).execute(context)

    assert context.data["action_results"] == [{"type": "http", "status_code": 204}]
    request = mock_client.return_value.__enter__.return_value.send.call_args.args[0]
    assert request.url == "https://8.8.8.8/hook"


@patch("app.core.actions.github.httpx.Client")
def test_github_action_sends_token_without_storing_it(mock_client: Mock) -> None:
    response = Mock()
    response.is_error = False
    response.status_code = 204
    mock_client.return_value.__enter__.return_value.post.return_value = response

    context = ExecutionContext(Event(type="manual", source="test"))
    GitHubAction(
        {"token": "secret-token", "repository": "owner/repo", "event_type": "deploy"}
    ).execute(context)

    assert context.data["action_results"] == [{"type": "github", "status_code": 204}]
    headers = mock_client.return_value.__enter__.return_value.post.call_args.kwargs["headers"]
    assert headers["Authorization"] == "Bearer secret-token"


def test_email_action_sends_safe_metadata(monkeypatch) -> None:
    monkeypatch.setattr("app.core.actions.email.settings.email_api_key", "test-key")
    monkeypatch.setattr("app.core.actions.email.settings.email_from", "sender@example.com")
    response = Mock(is_error=False, status_code=200)
    response.json.return_value = {"id": "email-123"}
    client = MagicMock()
    client.__enter__.return_value.send.return_value = response

    with patch("app.core.actions.email.httpx.Client", return_value=client):
        context = ExecutionContext(Event(type="manual", source="test"))
        EmailAction(
            {
                "to": ["recipient@example.com"],
                "subject": "FlowForge test",
                "text": "The workflow ran.",
            }
        ).execute(context)

    assert context.data["action_results"] == [
        {"type": "email", "provider": "resend", "status_code": 200, "provider_id": "email-123"}
    ]
    request = client.__enter__.return_value.send.call_args.args[0]
    assert "test-key" in request.headers["Authorization"]
    assert "test-key" not in str(context.data)


def test_email_action_validates_recipients(monkeypatch) -> None:
    monkeypatch.setattr("app.core.actions.email.settings.email_api_key", "test-key")
    with pytest.raises(ValueError, match="valid email"):
        EmailAction(
            {
                "from": "sender@example.com",
                "to": ["not-an-email"],
                "subject": "Test",
                "text": "Body",
            }
        )
