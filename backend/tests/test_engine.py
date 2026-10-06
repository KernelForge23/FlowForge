from app.core.conditions import AndCondition, ContainsCondition, EqualsCondition, OrCondition
from app.core.engine import ExecutionStatus, WorkflowEngine
from app.core.event import Event, ExecutionContext
from app.core.factories import ActionFactory, ConditionFactory, TriggerFactory
from app.core.workflow import Workflow


def test_factories_hydrate_nested_conditions_and_triggers() -> None:
    condition = ConditionFactory.create(
        "and",
        {
            "conditions": [
                {"type": "equals", "config": {"field": "repo", "value": "FlowForge"}},
                {"type": "contains", "config": {"field": "labels", "value": "bug"}},
            ]
        },
    )
    assert isinstance(condition, AndCondition)
    assert condition.evaluate(
        ExecutionContext(
            event=Event(type="manual", source="manual"),
            data={"repo": "FlowForge", "labels": ["bug"]},
        )
    )
    assert isinstance(TriggerFactory.create("webhook", {"source": "github"}), object)
    assert isinstance(ActionFactory.create("noop"), object)


def test_comparison_and_or_conditions() -> None:
    context = ExecutionContext(
        event=Event(type="manual", source="manual"),
        data={"count": 3, "status": "open"},
    )
    assert ConditionFactory.create("greater_than", {"field": "count", "value": 2}).evaluate(context)
    assert ConditionFactory.create("less_than", {"field": "count", "value": 4}).evaluate(context)
    assert ConditionFactory.create("not_equals", {"field": "status", "value": "closed"}).evaluate(context)
    assert OrCondition([EqualsCondition("status", "closed"), EqualsCondition("count", 3)]).evaluate(context)


def test_engine_skips_before_actions_when_trigger_or_condition_fails() -> None:
    action = ActionFactory.create("noop")
    workflow = Workflow(
        name="manual",
        trigger=TriggerFactory.create("manual"),
        condition=ConditionFactory.create("equals", {"field": "repo", "value": "FlowForge"}),
        actions=[action],
    )

    trigger_result = WorkflowEngine().execute(
        workflow,
        Event(type="webhook", source="github", payload={"repo": "FlowForge"}),
    )
    condition_result = WorkflowEngine().execute(
        workflow,
        Event(type="manual", source="manual", payload={"repo": "other"}),
    )

    assert trigger_result.status is ExecutionStatus.SKIPPED
    assert condition_result.status is ExecutionStatus.SKIPPED
    assert action.calls == []


def test_engine_executes_actions_in_order() -> None:
    first = ActionFactory.create("noop")
    second = ActionFactory.create("noop")
    workflow = Workflow("manual", TriggerFactory.create("manual"), None, [first, second])

    result = WorkflowEngine().execute(workflow, Event(type="manual", source="manual"))

    assert result.status is ExecutionStatus.SUCCESS
    assert result.action_count == 2
    assert len(first.calls) == 1
    assert len(second.calls) == 1


def test_engine_preserves_safe_action_error() -> None:
    class FailingAction:
        def execute(self, _context: ExecutionContext) -> None:
            raise RuntimeError("GitHub action returned status 403")

    workflow = Workflow("manual", TriggerFactory.create("manual"), None, [FailingAction()])
    result = WorkflowEngine().execute(workflow, Event(type="manual", source="manual"))

    assert result.status is ExecutionStatus.FAILED
    assert result.error == "GitHub action returned status 403"
