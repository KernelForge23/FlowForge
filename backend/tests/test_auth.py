from unittest.mock import Mock, patch

from app.api.auth import current_user


@patch("app.api.auth.httpx.get")
def test_current_user_reads_supabase_identity(mock_get: Mock, monkeypatch) -> None:
    monkeypatch.setattr("app.api.auth.settings.supabase_url", "https://project.supabase.co")
    response = Mock(status_code=200)
    response.json.return_value = {"id": "user-123", "email": "user@example.com"}
    mock_get.return_value = response

    user = current_user("Bearer access-token")

    assert user is not None
    assert user.id == "user-123"
    assert user.email == "user@example.com"
    mock_get.assert_called_once()
