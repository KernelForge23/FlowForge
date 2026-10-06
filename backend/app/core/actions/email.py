import re
from collections.abc import Mapping
from email.utils import parseaddr

import httpx

from app.config import settings
from app.core.actions.base import Action
from app.core.event import ExecutionContext
from app.services.gmail import GmailService

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _validate_email(value: object, field: str) -> str:
    if not isinstance(value, str) or not EMAIL_PATTERN.fullmatch(parseaddr(value)[1]):
        raise ValueError(f"{field} must be a valid email address")
    return value


class EmailAction(Action):
    def __init__(
        self, config: Mapping[str, object], gmail_service: GmailService | None = None
    ) -> None:
        if settings.email_provider not in {"resend", "gmail"}:
            raise ValueError("Unsupported email provider")
        if settings.email_provider == "resend" and not settings.email_api_key:
            raise ValueError("Email provider is not configured")
        if settings.email_provider == "gmail" and gmail_service is None:
            gmail_service = None
        self.gmail_service = gmail_service

        sender = config.get("from", settings.email_from)
        self.sender = _validate_email(sender, "from") if settings.email_provider == "resend" else None
        recipients = config.get("to")
        if isinstance(recipients, str):
            recipients = [recipients]
        if not isinstance(recipients, list) or not recipients:
            raise ValueError("to must contain at least one recipient")
        if len(recipients) > settings.email_max_recipients:
            raise ValueError("Too many email recipients")
        self.recipients = [_validate_email(item, "recipient") for item in recipients]

        subject = config.get("subject")
        if not isinstance(subject, str) or not subject.strip() or len(subject) > 200:
            raise ValueError("subject must be between 1 and 200 characters")
        self.subject = subject
        text = config.get("text", "")
        html = config.get("html")
        if not isinstance(text, str) or not isinstance(html, (str, type(None))):
            raise ValueError("text and html must be strings")
        if not text and not html:
            raise ValueError("Email requires text or html content")
        self.text = text
        self.html = html

    def execute(self, context: ExecutionContext) -> None:
        if settings.email_provider == "gmail":
            if self.gmail_service is None or context.user_id is None:
                raise RuntimeError("Gmail email action requires an authenticated workflow owner")
            result = self.gmail_service.send(
                context.user_id,
                self.recipients,
                self.subject,
                self.text,
                self.html,
                self.sender,
            )
            context.data.setdefault("action_results", []).append(result)
            return
        payload: dict[str, object] = {
            "from": self.sender,
            "to": self.recipients,
            "subject": self.subject,
        }
        if self.text:
            payload["text"] = self.text
        if self.html:
            payload["html"] = self.html
        request = httpx.Request(
            "POST",
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {settings.email_api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
        )
        if len(request.content) > settings.email_max_message_bytes:
            raise ValueError("Email message is too large")
        response = None
        for attempt in range(settings.http_action_max_retries + 1):
            try:
                with httpx.Client(timeout=settings.http_action_timeout_seconds) as client:
                    response = client.send(request)
            except httpx.TransportError:
                if attempt == settings.http_action_max_retries:
                    raise RuntimeError("Email provider network request failed") from None
                continue
            if response.status_code < 500 or attempt == settings.http_action_max_retries:
                break
        if response is None:
            raise RuntimeError("Email provider did not return a response")
        if response.is_error:
            raise RuntimeError(f"Email provider returned status {response.status_code}")
        provider_id = None
        try:
            response_data = response.json()
            if isinstance(response_data, dict) and isinstance(response_data.get("id"), str):
                provider_id = response_data["id"]
        except ValueError:
            pass
        result: dict[str, object] = {
            "type": "email",
            "provider": settings.email_provider,
            "status_code": response.status_code,
        }
        if provider_id:
            result["provider_id"] = provider_id
        context.data.setdefault("action_results", []).append(result)
