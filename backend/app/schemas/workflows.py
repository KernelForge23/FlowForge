from typing import Any

from pydantic import BaseModel, Field


class ComponentConfig(BaseModel):
    type: str
    config: dict[str, Any] = Field(default_factory=dict)


class WorkflowCreate(BaseModel):
    user_id: str
    name: str = Field(min_length=1, max_length=200)
    enabled: bool = False
    trigger: ComponentConfig
    conditions: list[ComponentConfig] = Field(default_factory=list)
    actions: list[ComponentConfig] = Field(default_factory=list)


class WorkflowResponse(BaseModel):
    id: str
    user_id: str
    name: str
    enabled: bool


class ManualRunRequest(BaseModel):
    payload: dict[str, Any] = Field(default_factory=dict)


class ExecutionResponse(BaseModel):
    id: str
    workflow_id: str
    status: str
    trigger_data: dict[str, Any]
    result: dict[str, Any]
    error: str | None
