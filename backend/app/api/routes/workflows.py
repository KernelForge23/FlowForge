from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_session
from app.schemas.workflows import (
    ExecutionResponse,
    ManualRunRequest,
    WorkflowCreate,
    WorkflowResponse,
)
from app.services.workflow import WorkflowService

router = APIRouter(prefix="/api/workflows", tags=["workflows"])


@router.post("", response_model=WorkflowResponse, status_code=status.HTTP_201_CREATED)
def create_workflow(
    request: WorkflowCreate,
    session: Session = Depends(get_session),
) -> WorkflowResponse:
    try:
        workflow = WorkflowService(session).create(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return WorkflowResponse.model_validate(workflow, from_attributes=True)


@router.get("/{workflow_id}", response_model=WorkflowResponse)
def get_workflow(
    workflow_id: str,
    session: Session = Depends(get_session),
) -> WorkflowResponse:
    workflow = WorkflowService(session).repository.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return WorkflowResponse.model_validate(workflow, from_attributes=True)


@router.post("/{workflow_id}/run", response_model=ExecutionResponse)
def run_workflow(
    workflow_id: str,
    request: ManualRunRequest,
    session: Session = Depends(get_session),
) -> ExecutionResponse:
    try:
        execution = WorkflowService(session).run_manual(workflow_id, request.payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ExecutionResponse.model_validate(execution, from_attributes=True)
