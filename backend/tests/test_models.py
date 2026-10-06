from app.models import User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger


def test_workflow_configuration_round_trip(db_session) -> None:
    user = User(email="builder@example.com")
    db_session.add(user)
    db_session.flush()

    workflow = Workflow(user_id=user.id, name="Notify on PR merge", enabled=True)
    workflow.trigger = WorkflowTrigger(trigger_type="manual", config={"source": "ui"})
    workflow.conditions.append(
        WorkflowCondition(condition_type="equals", config={"field": "repository", "value": "FlowForge"})
    )
    workflow.actions.append(
        WorkflowAction(position=0, action_type="noop", config={})
    )
    db_session.add(workflow)
    db_session.flush()

    stored = db_session.get(Workflow, workflow.id)
    assert stored is not None
    assert stored.trigger is not None
    assert stored.trigger.trigger_type == "manual"
    assert stored.trigger.config["source"] == "ui"
    assert stored.conditions[0].condition_type == "equals"
    assert stored.actions[0].action_type == "noop"
