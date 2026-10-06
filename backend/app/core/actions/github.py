from collections.abc import Mapping

import httpx

from app.config import settings
from app.core.actions.base import Action
from app.core.event import ExecutionContext


class GitHubAction(Action):
    def __init__(self, config: Mapping[str, object]) -> None:
        token = config.get("token")
        repository = config.get("repository")
        endpoint = config.get("endpoint", "dispatches")
        if not isinstance(token, str) or not token:
            raise ValueError("GitHub action requires a token")
        if not isinstance(repository, str) or repository.count("/") != 1:
            raise ValueError("GitHub action repository must be owner/name")
        if endpoint not in {"dispatches", "issues/comments"}:
            raise ValueError("Unsupported GitHub endpoint")
        self.token = token
        self.repository = repository
        self.endpoint = endpoint
        self.event_type = str(config.get("event_type", "flowforge"))
        self.body = config.get("body", {})

    def execute(self, context: ExecutionContext) -> None:
        if self.endpoint == "dispatches":
            url = f"https://api.github.com/repos/{self.repository}/dispatches"
            payload = {"event_type": self.event_type, "client_payload": self.body}
        else:
            url = f"https://api.github.com/repos/{self.repository}/issues/comments"
            payload = self.body
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        with httpx.Client(timeout=settings.http_action_timeout_seconds) as client:
            response = client.post(url, headers=headers, json=payload)
        if response.is_error:
            raise RuntimeError(f"GitHub action returned status {response.status_code}")
        context.data.setdefault("action_results", []).append(
            {"type": "github", "status_code": response.status_code}
        )
