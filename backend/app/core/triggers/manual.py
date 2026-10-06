from app.core.event import Event
from app.core.triggers.base import Trigger


class ManualTrigger(Trigger):
    """Matches operator-initiated or test events. No external webhook required."""

    def should_execute(self, event: Event) -> bool:
        return event.type == "manual" or event.source == "manual"
