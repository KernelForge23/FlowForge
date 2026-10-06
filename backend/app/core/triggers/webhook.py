from app.core.event import Event
from app.core.triggers.base import Trigger


class WebhookTrigger(Trigger):
    def __init__(self, source: str | None = None) -> None:
        self.source = source

    def should_execute(self, event: Event) -> bool:
        if event.type != "webhook":
            return False
        return self.source is None or event.source == self.source
