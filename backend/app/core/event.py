from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Event:
    """Normalized inbound event. The engine should never parse vendor JSON directly."""

    type: str
    source: str
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class ExecutionContext:
    event: Event
    user_id: str | None = None
    data: dict[str, Any] = field(default_factory=dict)

    def lookup(self, field_name: str) -> Any:
        if field_name in self.data:
            return self.data[field_name]
        return self.event.payload.get(field_name)
