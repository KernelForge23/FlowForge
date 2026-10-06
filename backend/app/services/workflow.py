from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.engine import WorkflowEngine
from app.core.event import Event
from app.core.factories import ActionFactory, ConditionFactory, TriggerFactory
from app.core.workflow import Workflow as RuntimeWorkflow
from app.models import Execution, User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger
from app.repositories.workflow import WorkflowRepository
from app.schemas.workflows import WorkflowCreate


class WorkflowService:
    def __init__(self, session: Session) -> None:
        self.session = session
        self.repository = WorkflowRepository(session)

    def create(self, request: WorkflowCreate) -> Workflow:
        if self.session.get(User, request.user_id) is None:
            raise ValueError("User does not exist")
        workflow = self.repository.add(
            Workflow(
                user_id=request.user_id,
                name=request.name,
                enabled=request.enabled,
            )
        )
        workflow.trigger = WorkflowTrigger(
            trigger_type=request.trigger.type,
            config=request.trigger.config,
        )
        workflow.conditions = [
            WorkflowCondition(condition_type=item.type, config=item.config)
            for item in request.conditions
        ]
        workflow.actions = [
            WorkflowAction(position=index, action_type=item.type, config=item.config)
            for index, item in enumerate(request.actions)
        ]
        self.session.flush()
        return workflow

    def load_runtime(self, workflow_id: str) -> tuple[Workflow, RuntimeWorkflow]:
        stored = self.repository.get(workflow_id)
        if stored is None or stored.trigger is None:
            raise ValueError("Workflow configuration does not exist")
        trigger = TriggerFactory.create(stored.trigger.trigger_type, stored.trigger.config)
        condition = ConditionFactory.create("and", {"conditions": [
            {"type": row.condition_type, "config": row.config} for row in stored.conditions
        ]}) if len(stored.conditions) > 1 else (
            ConditionFactory.create(
                stored.conditions[0].condition_type,
                stored.conditions[0].config,
            ) if stored.conditions else None
        )
        actions = [
            ActionFactory.create(row.action_type, row.config)
            for row in stored.actions
        ]
        return stored, RuntimeWorkflow(
            name=stored.name,
            trigger=trigger,
            condition=condition,
            actions=actions,
        )

    def run_manual(self, workflow_id: str, payload: dict) -> Execution:
        stored, runtime = self.load_runtime(workflow_id)
        event = Event(type="manual", source="manual", payload=payload)
        result = WorkflowEngine().execute(runtime, event)
        execution = Execution(
            workflow_id=stored.id,
            status=result.status.value,
            started_at=datetime.now(timezone.utc),
            completed_at=datetime.now(timezone.utc),
            trigger_data=payload,
            result={"action_count": result.action_count},
            error=result.error,
        )
        self.session.add(execution)
        self.session.flush()
        return execution
