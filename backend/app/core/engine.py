from dataclasses import dataclass
from enum import StrEnum

from app.core.event import Event, ExecutionContext
from app.core.workflow import Workflow


class ExecutionStatus(StrEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclass(frozen=True)
class EngineResult:
    status: ExecutionStatus
    action_count: int = 0
    error: str | None = None


class WorkflowEngine:
    def execute(self, workflow: Workflow, event: Event, user_id: str | None = None) -> EngineResult:
        if not workflow.trigger.should_execute(event):
            return EngineResult(status=ExecutionStatus.SKIPPED, error="Trigger did not match")

        context = ExecutionContext(event=event, user_id=user_id)
        if workflow.condition is not None and not workflow.condition.evaluate(context):
            return EngineResult(status=ExecutionStatus.SKIPPED, error="Conditions did not match")

        executed = 0
        try:
            for action in workflow.actions:
                action.execute(context)
                executed += 1
        except Exception as exc:
            return EngineResult(
                status=ExecutionStatus.FAILED,
                action_count=executed,
                error=str(exc) or "Action execution failed",
            )
        return EngineResult(status=ExecutionStatus.SUCCESS, action_count=executed)
