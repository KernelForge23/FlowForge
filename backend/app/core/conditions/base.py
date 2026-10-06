from abc import ABC, abstractmethod

from app.core.event import ExecutionContext


class Condition(ABC):
    @abstractmethod
    def evaluate(self, context: ExecutionContext) -> bool:
        """Return True when the workflow should continue."""
