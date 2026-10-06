from unittest.mock import Mock, patch

import pytest

from app.core.actions.github import GitHubAction
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
def test_github_action_does_not_store_token(mock_client: Mock) -> None:
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
