from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_session
from app.api.auth import AuthenticatedUser, current_user
from app.models import User
from app.schemas.workflows import (
    ExecutionResponse,
    ManualRunRequest,
    WorkflowCreate,
    WorkflowDetailResponse,
    WorkflowResponse,
    WorkflowUpdate,
)
from app.services.workflow import WorkflowService

router = APIRouter(prefix="/api/workflows", tags=["workflows"])


def _detail(workflow) -> WorkflowDetailResponse:
    return WorkflowDetailResponse(
        id=workflow.id,
        user_id=workflow.user_id,
        name=workflow.name,
        enabled=workflow.enabled,
        trigger=(
            {"type": workflow.trigger.trigger_type, "config": workflow.trigger.config}
            if workflow.trigger else {"type": "manual", "config": {}}
        ),
        conditions=[
            {"type": item.condition_type, "config": item.config}
            for item in workflow.conditions
        ],
        actions=[
            {"type": item.action_type, "config": item.config}
            for item in workflow.actions
        ],
    )


@router.get("", response_model=list[WorkflowResponse])
def list_workflows(
    user_id: str,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> list[WorkflowResponse]:
    if authenticated_user is not None and authenticated_user.id != user_id:
        raise HTTPException(status_code=403, detail="Workflow ownership violation")
    workflows = WorkflowService(session).repository.list_for_user(user_id)
    return [WorkflowResponse.model_validate(item, from_attributes=True) for item in workflows]


@router.post("", response_model=WorkflowResponse, status_code=status.HTTP_201_CREATED)
def create_workflow(
    request: WorkflowCreate,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> WorkflowResponse:
    if authenticated_user is not None and authenticated_user.id != request.user_id:
        raise HTTPException(status_code=403, detail="Workflow ownership violation")
    try:
        if authenticated_user is not None and session.get(User, authenticated_user.id) is None:
            session.add(User(id=authenticated_user.id, email=authenticated_user.email))
            session.flush()
        workflow = WorkflowService(session).create(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return WorkflowResponse.model_validate(workflow, from_attributes=True)


@router.put("/{workflow_id}", response_model=WorkflowDetailResponse)
def update_workflow(
    workflow_id: str,
    request: WorkflowUpdate,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> WorkflowDetailResponse:
    workflow = WorkflowService(session).repository.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    if authenticated_user is not None and workflow.user_id != authenticated_user.id:
        raise HTTPException(status_code=403, detail="Workflow ownership violation")
    try:
        updated = WorkflowService(session).update(workflow_id, request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return _detail(updated)


@router.delete("/{workflow_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workflow(
    workflow_id: str,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> None:
    workflow = WorkflowService(session).repository.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    if authenticated_user is not None and workflow.user_id != authenticated_user.id:
        raise HTTPException(status_code=403, detail="Workflow ownership violation")
    try:
        WorkflowService(session).delete(workflow_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/{workflow_id}", response_model=WorkflowDetailResponse)
def get_workflow(
    workflow_id: str,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> WorkflowResponse:
    workflow = WorkflowService(session).repository.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    if authenticated_user is not None and workflow.user_id != authenticated_user.id:
        raise HTTPException(status_code=403, detail="Workflow ownership violation")
    return _detail(workflow)


@router.get("/{workflow_id}/executions", response_model=list[ExecutionResponse])
def list_executions(
    workflow_id: str,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> list[ExecutionResponse]:
    workflow = WorkflowService(session).repository.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")
    if authenticated_user is not None and workflow.user_id != authenticated_user.id:
        raise HTTPException(status_code=403, detail="Workflow ownership violation")
    executions = WorkflowService(session).repository.executions(workflow_id)
    return [ExecutionResponse.model_validate(item, from_attributes=True) for item in executions]


@router.post("/{workflow_id}/run", response_model=ExecutionResponse)
def run_workflow(
    workflow_id: str,
    request: ManualRunRequest,
    session: Session = Depends(get_session),
    authenticated_user: AuthenticatedUser | None = Depends(current_user),
) -> ExecutionResponse:
    try:
        workflow = WorkflowService(session).repository.get(workflow_id)
        if workflow is None:
            raise ValueError("Workflow not found")
        if authenticated_user is not None and workflow.user_id != authenticated_user.id:
            raise HTTPException(status_code=403, detail="Workflow ownership violation")
        execution = WorkflowService(session).run_manual(workflow_id, request.payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return ExecutionResponse.model_validate(execution, from_attributes=True)
