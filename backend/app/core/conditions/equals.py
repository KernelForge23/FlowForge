from app.core.conditions.base import Condition
from app.core.event import ExecutionContext


class EqualsCondition(Condition):
    def __init__(self, field: str, value: object) -> None:
        self.field = field
        self.value = value

    def evaluate(self, context: ExecutionContext) -> bool:
        return context.lookup(self.field) == self.value
