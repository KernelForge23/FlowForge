from sqlalchemy.orm import Session

from app.models import Execution, Workflow


class WorkflowRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, workflow_id: str) -> Workflow | None:
        return self.session.get(Workflow, workflow_id)

    def add(self, workflow: Workflow) -> Workflow:
        self.session.add(workflow)
        self.session.flush()
        return workflow

    def list_for_user(self, user_id: str) -> list[Workflow]:
        return list(
            self.session.query(Workflow)
            .filter(Workflow.user_id == user_id)
            .order_by(Workflow.updated_at.desc())
            .all()
        )

    def executions(self, workflow_id: str) -> list[Execution]:
        return list(
            self.session.query(Execution)
            .filter(Execution.workflow_id == workflow_id)
            .order_by(Execution.started_at.desc())
            .all()
        )
