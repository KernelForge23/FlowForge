from app.core.actions.base import Action
from app.core.conditions.base import Condition
from app.core.triggers.base import Trigger


class Workflow:
    """Composable workflow configuration object. Not the execution engine."""

    def __init__(
        self,
        name: str,
        trigger: Trigger,
        condition: Condition | None,
        actions: list[Action],
    ) -> None:
        self.name = name
        self.trigger = trigger
        self.condition = condition
        self.actions = actions
