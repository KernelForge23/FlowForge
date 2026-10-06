from collections.abc import Iterable

from app.core.conditions.base import Condition
from app.core.event import ExecutionContext


class AndCondition(Condition):
    def __init__(self, conditions: Iterable[Condition]) -> None:
        self.conditions = list(conditions)

    def evaluate(self, context: ExecutionContext) -> bool:
        return all(condition.evaluate(context) for condition in self.conditions)


class OrCondition(Condition):
    def __init__(self, conditions: Iterable[Condition]) -> None:
        self.conditions = list(conditions)

    def evaluate(self, context: ExecutionContext) -> bool:
        return any(condition.evaluate(context) for condition in self.conditions)
