from app.schemas.workflows import ComponentConfig, WorkflowCreate
from app.services.workflow import WorkflowService


def test_create_load_run_records_execution(db_session) -> None:
    from app.models import User

    user = User(email="engine@example.com")
    db_session.add(user)
    db_session.flush()

    request = WorkflowCreate(
        user_id=user.id,
        name="Run manually",
        enabled=True,
        trigger=ComponentConfig(type="manual"),
        conditions=[ComponentConfig(type="equals", config={"field": "repo", "value": "FlowForge"})],
        actions=[ComponentConfig(type="noop")],
    )
    service = WorkflowService(db_session)
    stored = service.create(request)
    execution = service.run_manual(stored.id, {"repo": "FlowForge"})

    assert execution.status == "SUCCESS"
    assert execution.result == {"action_count": 1}
    assert execution.error is None
