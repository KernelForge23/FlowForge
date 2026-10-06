import hashlib
import hmac
import json

from fastapi import APIRouter, Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session

from app.core.event import Event
from app.config import settings
from app.db import get_session
from app.models import Workflow
from app.schemas.workflows import ExecutionResponse
from app.services.workflow import WorkflowService

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


@router.post("/{provider}", response_model=list[ExecutionResponse])
async def receive_webhook(
    provider: str,
    request: Request,
    session: Session = Depends(get_session),
    x_hub_signature_256: str | None = Header(default=None),
) -> list[ExecutionResponse]:
    if provider != "github":
        raise HTTPException(status_code=404, detail="Unsupported webhook provider")
    raw_body = await request.body()
    if settings.github_webhook_secret:
        expected = "sha256=" + hmac.new(
            settings.github_webhook_secret.encode(),
            raw_body,
            hashlib.sha256,
        ).hexdigest()
        if not x_hub_signature_256 or not hmac.compare_digest(x_hub_signature_256, expected):
            raise HTTPException(status_code=401, detail="Invalid webhook signature")
    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=400, detail="Webhook payload must be valid JSON") from exc
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Webhook payload must be an object")
    service = WorkflowService(session)
    executions = []
    workflows = (
        session.query(Workflow)
        .filter(Workflow.enabled.is_(True))
        .all()
    )
    for workflow in workflows:
        if workflow.trigger is None or workflow.trigger.trigger_type != "webhook":
            continue
        executions.append(
            service.run_event(
                workflow.id,
                Event(type="webhook", source="github", payload=payload),
            )
        )
    return [ExecutionResponse.model_validate(item, from_attributes=True) for item in executions]
