from collections.abc import Mapping
from typing import Any

from app.core.actions import Action, EmailAction, GitHubAction, HttpAction, NoOpAction
from app.core.conditions import (
    AndCondition,
    Condition,
    ContainsCondition,
    EqualsCondition,
    GreaterThanCondition,
    LessThanCondition,
    NotEqualsCondition,
    OrCondition,
)
from app.core.triggers import ManualTrigger, ScheduledTrigger, Trigger, WebhookTrigger


def _required(config: Mapping[str, Any], key: str) -> Any:
    if key not in config:
        raise ValueError(f"Missing required configuration: {key}")
    return config[key]


class TriggerFactory:
    @staticmethod
    def create(trigger_type: str, config: Mapping[str, Any] | None = None) -> Trigger:
        values = config or {}
        if trigger_type == "manual":
            return ManualTrigger()
        if trigger_type == "webhook":
            return WebhookTrigger(source=values.get("source"))
        if trigger_type == "scheduled":
            return ScheduledTrigger()
        raise ValueError(f"Unsupported trigger type: {trigger_type}")


class ConditionFactory:
    @staticmethod
    def create(condition_type: str, config: Mapping[str, Any] | None = None) -> Condition:
        values = config or {}
        if condition_type in {"and", "or"}:
            children = values.get("conditions")
            if not isinstance(children, list):
                raise ValueError("Composite conditions require a conditions list")
            hydrated = [
                ConditionFactory.create(child["type"], child.get("config", {}))
                for child in children
            ]
            return AndCondition(hydrated) if condition_type == "and" else OrCondition(hydrated)

        field = _required(values, "field")
        value = _required(values, "value")
        condition_types = {
            "equals": EqualsCondition,
            "not_equals": NotEqualsCondition,
            "greater_than": GreaterThanCondition,
            "less_than": LessThanCondition,
            "contains": ContainsCondition,
        }
        condition_class = condition_types.get(condition_type)
        if condition_class is None:
            raise ValueError(f"Unsupported condition type: {condition_type}")
        return condition_class(field=field, value=value)


class ActionFactory:
    @staticmethod
    def create(
        action_type: str,
        config: Mapping[str, Any] | None = None,
        gmail_service: Any = None,
    ) -> Action:
        if action_type == "noop":
            return NoOpAction()
        if action_type == "http":
            return HttpAction(config or {})
        if action_type == "github":
            return GitHubAction(config or {})
        if action_type == "email":
            return EmailAction(config or {}, gmail_service=gmail_service)
        raise ValueError(f"Unsupported action type: {action_type}")
