from abc import ABC, abstractmethod

from app.core.event import ExecutionContext


class Action(ABC):
    @abstractmethod
    def execute(self, context: ExecutionContext) -> None:
        """Perform the side effect."""
