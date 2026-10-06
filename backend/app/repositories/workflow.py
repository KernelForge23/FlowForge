from sqlalchemy.orm import Session

from app.models import Workflow


class WorkflowRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, workflow_id: str) -> Workflow | None:
        return self.session.get(Workflow, workflow_id)

    def add(self, workflow: Workflow) -> Workflow:
        self.session.add(workflow)
        self.session.flush()
        return workflow
