from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

from app.models.base import Base, TimestampMixin, new_id


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)

    workflows: Mapped[list["Workflow"]] = relationship(back_populates="user")
    integrations: Mapped[list["Integration"]] = relationship(back_populates="user")


class Workflow(TimestampMixin, Base):
    __tablename__ = "workflows"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    enabled: Mapped[bool] = mapped_column(default=False, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    user: Mapped[User] = relationship(back_populates="workflows")
    trigger: Mapped["WorkflowTrigger | None"] = relationship(
        back_populates="workflow", uselist=False, cascade="all, delete-orphan"
    )
    conditions: Mapped[list["WorkflowCondition"]] = relationship(
        back_populates="workflow", cascade="all, delete-orphan"
    )
    actions: Mapped[list["WorkflowAction"]] = relationship(
        back_populates="workflow", cascade="all, delete-orphan", order_by="WorkflowAction.position"
    )
    executions: Mapped[list["Execution"]] = relationship(
        back_populates="workflow", cascade="all, delete-orphan"
    )


class WorkflowTrigger(Base):
    __tablename__ = "workflow_triggers"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), unique=True, nullable=False)
    trigger_type: Mapped[str] = mapped_column(String(64), nullable=False)
    config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    workflow: Mapped[Workflow] = relationship(back_populates="trigger")


class WorkflowCondition(Base):
    __tablename__ = "workflow_conditions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), nullable=False)
    parent_id: Mapped[str | None] = mapped_column(ForeignKey("workflow_conditions.id"), nullable=True)
    condition_type: Mapped[str] = mapped_column(String(64), nullable=False)
    config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    workflow: Mapped[Workflow] = relationship(back_populates="conditions")


class Integration(TimestampMixin, Base):
    __tablename__ = "integrations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    provider: Mapped[str] = mapped_column(String(64), nullable=False)
    config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    user: Mapped[User] = relationship(back_populates="integrations")
    actions: Mapped[list["WorkflowAction"]] = relationship(back_populates="integration")


class GmailConnection(TimestampMixin, Base):
    __tablename__ = "gmail_connections"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(320), nullable=False)
    access_token: Mapped[str] = mapped_column(Text, nullable=False)
    refresh_token: Mapped[str] = mapped_column(Text, nullable=False)
    token_expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    user: Mapped[User] = relationship()


class GmailOAuthState(Base):
    __tablename__ = "gmail_oauth_states"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    state_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class WorkflowAction(Base):
    __tablename__ = "workflow_actions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), nullable=False)
    integration_id: Mapped[str | None] = mapped_column(ForeignKey("integrations.id"), nullable=True)
    position: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    action_type: Mapped[str] = mapped_column(String(64), nullable=False)
    config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)

    workflow: Mapped[Workflow] = relationship(back_populates="actions")
    integration: Mapped[Integration | None] = relationship(back_populates="actions")


class Execution(Base):
    __tablename__ = "executions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
    workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="PENDING")
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    trigger_data: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    result: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)

    workflow: Mapped[Workflow] = relationship(back_populates="executions")
