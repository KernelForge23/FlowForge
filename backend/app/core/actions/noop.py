from app.core.actions.base import Action
from app.core.event import ExecutionContext


class NoOpAction(Action):
    """Records that execute() ran. No network and no secrets."""

    def __init__(self) -> None:
        self.calls: list[ExecutionContext] = []

    def execute(self, context: ExecutionContext) -> None:
        self.calls.append(context)
