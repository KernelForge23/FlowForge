from typing import Any

from app.core.conditions.base import Condition
from app.core.event import ExecutionContext


class NotEqualsCondition(Condition):
    def __init__(self, field: str, value: Any) -> None:
        self.field = field
        self.value = value

    def evaluate(self, context: ExecutionContext) -> bool:
        return context.lookup(self.field) != self.value


class GreaterThanCondition(Condition):
    def __init__(self, field: str, value: Any) -> None:
        self.field = field
        self.value = value

    def evaluate(self, context: ExecutionContext) -> bool:
        try:
            return context.lookup(self.field) > self.value
        except TypeError:
            return False


class LessThanCondition(Condition):
    def __init__(self, field: str, value: Any) -> None:
        self.field = field
        self.value = value

    def evaluate(self, context: ExecutionContext) -> bool:
        try:
            return context.lookup(self.field) < self.value
        except TypeError:
            return False


class ContainsCondition(Condition):
    def __init__(self, field: str, value: Any) -> None:
        self.field = field
        self.value = value

    def evaluate(self, context: ExecutionContext) -> bool:
        candidate = context.lookup(self.field)
        try:
            return self.value in candidate
        except TypeError:
            return False
