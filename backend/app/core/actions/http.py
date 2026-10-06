import ipaddress
import socket
from collections.abc import Mapping
from urllib.parse import urlparse

import httpx

from app.config import settings
from app.core.actions.base import Action
from app.core.event import ExecutionContext


def validate_public_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("URL must use http or https")
    try:
        addresses = socket.getaddrinfo(parsed.hostname, parsed.port or 443, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise ValueError("URL hostname could not be resolved") from exc
    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_unspecified:
            raise ValueError("URL must not target a private or local address")
    return url


class HttpAction(Action):
    def __init__(self, config: Mapping[str, object]) -> None:
        url = config.get("url")
        if not isinstance(url, str):
            raise ValueError("HTTP action requires a URL")
        self.url = validate_public_url(url)
        self.method = str(config.get("method", "POST")).upper()
        if self.method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
            raise ValueError("Unsupported HTTP method")
        self.headers = {
            str(key): str(value)
            for key, value in (config.get("headers", {}) or {}).items()
            if isinstance(key, str)
        }
        payload = config.get("body", {})
        self.body = payload if isinstance(payload, (dict, list, str, int, float, bool)) else {}

    def execute(self, context: ExecutionContext) -> None:
        request = httpx.Request(self.method, self.url, headers=self.headers, json=self.body)
        if len(request.content) > settings.http_action_max_payload_bytes:
            raise ValueError("HTTP action payload is too large")
        response = None
        for attempt in range(settings.http_action_max_retries + 1):
            try:
                with httpx.Client(timeout=settings.http_action_timeout_seconds, follow_redirects=False) as client:
                    response = client.send(request)
            except httpx.TransportError:
                if attempt == settings.http_action_max_retries:
                    raise RuntimeError("HTTP action network request failed") from None
                continue
            if response.status_code < 500 or attempt == settings.http_action_max_retries:
                break
        if response is None:
            raise RuntimeError("HTTP action did not receive a response")
        if response.is_error:
            raise RuntimeError(f"HTTP action returned status {response.status_code}")
        context.data.setdefault("action_results", []).append(
            {"type": "http", "status_code": response.status_code}
        )
