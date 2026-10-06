from app.core.actions import Action, NoOpAction
from app.core.conditions import EqualsCondition
from app.core.event import Event, ExecutionContext
from app.core.triggers import ManualTrigger, Trigger
from app.core.workflow import Workflow


def test_manual_trigger_matches_manual_event() -> None:
    trigger: Trigger = ManualTrigger()
    event = Event(type="manual", source="ui", payload={})
    assert trigger.should_execute(event) is True


def test_manual_trigger_rejects_webhook_event() -> None:
    trigger = ManualTrigger()
    event = Event(type="webhook", source="github", payload={})
    assert trigger.should_execute(event) is False


def test_equals_condition_true_and_false() -> None:
    condition = EqualsCondition(field="repository", value="FlowForge")
    matching = ExecutionContext(
        event=Event(type="manual", source="manual"),
        data={"repository": "FlowForge"},
    )
    other = ExecutionContext(
        event=Event(type="manual", source="manual"),
        data={"repository": "other"},
    )
    assert condition.evaluate(matching) is True
    assert condition.evaluate(other) is False


def test_workflow_composition_executes_actions_via_base_type() -> None:
    action = NoOpAction()
    workflow = Workflow(
        name="Notify on manual run",
        trigger=ManualTrigger(),
        condition=EqualsCondition(field="repository", value="FlowForge"),
        actions=[action],
    )
    event = Event(type="manual", source="manual", payload={"repository": "FlowForge"})
    context = ExecutionContext(event=event, data={"repository": "FlowForge"})

    assert workflow.trigger.should_execute(event) is True
    assert workflow.condition.evaluate(context) is True

    executed = 0
    for step in workflow.actions:
        assert isinstance(step, Action)
        step.execute(context)
        executed += 1

    assert executed == 1
    assert len(action.calls) == 1
