from abc import ABC, abstractmethod

from app.core.event import Event


class Trigger(ABC):
    @abstractmethod
    def should_execute(self, event: Event) -> bool:
        """Return True when this workflow should start for the given event."""
