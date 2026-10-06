from app.core.event import Event
from app.core.triggers.base import Trigger


class ScheduledTrigger(Trigger):
    def should_execute(self, event: Event) -> bool:
        return event.type == "scheduled"
