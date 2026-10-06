# FlowForge Phase 2 Backend Explanation

> This document explains the Week 2 backend that exists in the repository. It
> describes the implemented workflow engine slice, not the complete MVP. Phase
> 2 connects persisted workflow configuration to real runtime objects, executes
> those objects, and records the result.

## 1. What Phase 2 is trying to prove

Phase 1 created the foundation:

```text
FastAPI application
SQLAlchemy models
Trigger / Condition / Action abstractions
Basic OOP implementations
```

Phase 2 proves the complete backend execution path:

```text
Create workflow
      ↓
Save configuration rows
      ↓
Load configuration rows
      ↓
Factories construct OOP objects
      ↓
WorkflowEngine evaluates the workflow
      ↓
Execution row records the result
```

The central technical requirement is that the engine should not know whether a
workflow uses a manual trigger, a webhook trigger, an equality condition, or a
future vendor-specific action. The engine calls abstractions. Factories decide
which concrete classes to construct from stored type names.

At the end of this phase, the backend can:

1. Accept a workflow definition through an API request.
2. Store the workflow, trigger, conditions, and actions in SQLite-compatible
   SQLAlchemy tables.
3. Load the saved configuration.
4. Convert persisted rows into runtime `Trigger`, `Condition`, and `Action`
   objects.
5. Run the workflow manually.
6. Stop when the trigger or conditions do not match.
7. Execute actions in order when the workflow matches.
8. Store `SUCCESS`, `SKIPPED`, or `FAILED` execution information.

The action used in this phase is intentionally deterministic. It is a
`NoOpAction`, so Week 2 can prove orchestration without making network calls.
HTTP, GitHub, and email integrations remain Week 3 work.

## 2. How the Phase 2 backend is organized

The implementation keeps the layered architecture introduced in Phase 1:

| Layer | Location | Responsibility |
| --- | --- | --- |
| HTTP/API | [`backend/app/api/`](backend/app/api/) | Receive requests, call services, return responses |
| Schemas | [`backend/app/schemas/`](backend/app/schemas/) | Validate workflow and execution request/response shapes |
| Services | [`backend/app/services/`](backend/app/services/) | Coordinate persistence, factories, and engine execution |
| Repositories | [`backend/app/repositories/`](backend/app/repositories/) | Encapsulate database access |
| Core engine | [`backend/app/core/`](backend/app/core/) | Define events, runtime objects, factories, and execution behavior |
| Models | [`backend/app/models/`](backend/app/models/) | Store workflow configuration and execution records |
| Tests | [`backend/tests/`](backend/tests/) | Verify core logic, persistence, service orchestration, and API flow |

The most important boundary is between persisted configuration and runtime
objects:

```text
SQLAlchemy rows
      ↓
WorkflowService
      ↓
TriggerFactory / ConditionFactory / ActionFactory
      ↓
Core Workflow object
      ↓
WorkflowEngine
```

The `core` package does not need FastAPI routes or SQLAlchemy sessions to
evaluate a workflow. This keeps the engine independently testable.

## 3. The complete request and execution flow

### 3.1 Creating a workflow

The client sends a request to:

```text
POST /api/workflows
```

The request contains a user ID, workflow name, trigger configuration,
condition configurations, and action configurations:

```json
{
  "user_id": "user-id",
  "name": "Run manually",
  "enabled": true,
  "trigger": {
    "type": "manual",
    "config": {}
  },
  "conditions": [
    {
      "type": "equals",
      "config": {
        "field": "repository",
        "value": "FlowForge"
      }
    }
  ],
  "actions": [
    {
      "type": "noop",
      "config": {}
    }
  ]
}
```

The route does not construct a `ManualTrigger` or execute anything. It passes
the validated request to `WorkflowService.create()`.

The service creates:

```text
Workflow
WorkflowTrigger
WorkflowCondition
WorkflowAction
```

The database stores type names and JSON configuration, rather than Python
objects.

### 3.2 Loading a workflow

The client can load the saved workflow through:

```text
GET /api/workflows/{workflow_id}
```

This endpoint currently returns the safe workflow summary:

```json
{
  "id": "workflow-id",
  "user_id": "user-id",
  "name": "Run manually",
  "enabled": true
}
```

The runtime loading path is handled inside
[`WorkflowService`](backend/app/services/workflow.py). It reads the persisted
rows through [`WorkflowRepository`](backend/app/repositories/workflow.py), then
passes each type and configuration to the appropriate factory.

### 3.3 Running a workflow manually

The manual execution endpoint is:

```text
POST /api/workflows/{workflow_id}/run
```

The request body contains event payload data:

```json
{
  "payload": {
    "repository": "FlowForge"
  }
}
```

The service converts that request into a normalized event:

```python
Event(
    type="manual",
    source="manual",
    payload={"repository": "FlowForge"},
)
```

The service then:

1. Loads the database workflow.
2. Hydrates the runtime trigger, condition, and actions.
3. Passes the runtime workflow and event to `WorkflowEngine`.
4. Converts the result into an `Execution` database row.
5. Returns the execution response.

An example successful response is:

```json
{
  "id": "execution-id",
  "workflow_id": "workflow-id",
  "status": "SUCCESS",
  "trigger_data": {
    "repository": "FlowForge"
  },
  "result": {
    "action_count": 1
  },
  "error": null
}
```

## 4. Request and response schemas

### [`backend/app/schemas/workflows.py`](backend/app/schemas/workflows.py)

This module defines the API boundary for Phase 2.

### `ComponentConfig`

```python
class ComponentConfig(BaseModel):
    type: str
    config: dict[str, Any] = Field(default_factory=dict)
```

Every trigger, condition, and action has the same external shape:

```text
type   → selects the factory implementation
config → supplies that implementation's parameters
```

For example:

```json
{
  "type": "greater_than",
  "config": {
    "field": "priority",
    "value": 3
  }
}
```

The schema does not contain vendor-specific branches. It accepts configuration
data; the factories interpret the type later.

### `WorkflowCreate`

`WorkflowCreate` validates:

- A user ID.
- A non-empty workflow name.
- A maximum workflow name length of 200 characters.
- One trigger configuration.
- Zero or more conditions.
- Zero or more actions.
- An optional enabled flag.

The schema uses Pydantic at the API boundary. This prevents malformed JSON from
reaching the service layer as an untyped request.

### `WorkflowResponse`

This is the summary response for create and load operations:

```text
id
user_id
name
enabled
```

It intentionally does not expose raw credentials or integration data.

### `ManualRunRequest`

```python
class ManualRunRequest(BaseModel):
    payload: dict[str, Any] = Field(default_factory=dict)
```

The payload becomes the normalized event payload. Conditions read values from
this payload through `ExecutionContext.lookup()`.

### `ExecutionResponse`

This exposes the recorded execution fields:

```text
id
workflow_id
status
trigger_data
result
error
```

It does not expose internal runtime objects.

## 5. Persistence model used by the engine

The SQLAlchemy entities are defined in
[`backend/app/models/entities.py`](backend/app/models/entities.py).

### `Workflow`

The parent workflow stores:

```text
id
user_id
name
enabled
```

It owns relationships to:

```text
trigger
conditions
actions
executions
```

The workflow is configuration. It is not itself the object that evaluates
events.

### `WorkflowTrigger`

The trigger row stores:

```text
workflow_id
trigger_type
config
```

Example:

```json
{
  "trigger_type": "webhook",
  "config": {
    "source": "github"
  }
}
```

The type is data. `TriggerFactory` turns it into a `WebhookTrigger` later.

### `WorkflowCondition`

Each condition row stores:

```text
workflow_id
condition_type
config
parent_id
```

The current service treats multiple top-level condition rows as an implicit
AND group. A single condition is hydrated directly. Nested composite condition
configuration can also be hydrated by `ConditionFactory` using a `conditions`
list in JSON.

The `parent_id` column prepares the persistence model for richer condition
trees. The current Week 2 service does not yet build a database tree from
`parent_id`; that is a future refinement when the builder needs persisted
nested groups.

### `WorkflowAction`

Each action row stores:

```text
workflow_id
position
action_type
config
integration_id
```

The relationship orders actions by `position`. This means the workflow can
contain more than one action and the engine can execute them in a predictable
sequence.

`integration_id` exists for future integration-backed actions. Week 2 does not
use it because `NoOpAction` has no external side effect.

### `Execution`

An execution row stores:

```text
id
workflow_id
status
started_at
completed_at
trigger_data
result
error
```

The current statuses are:

```text
SUCCESS
FAILED
SKIPPED
```

The execution record is created after `WorkflowEngine` returns. The raw input
payload is stored as `trigger_data`, while the safe summary currently stores
the number of actions executed.

Secrets must not be placed into event payloads, action results, or error
messages. Future integration work must preserve this rule.

## 6. Normalized events and execution context

### [`backend/app/core/event.py`](backend/app/core/event.py)

The engine should not understand GitHub JSON, browser request formats, or
provider-specific webhook structures. It receives a normalized `Event`.

### `Event`

```python
@dataclass
class Event:
    type: str
    source: str
    payload: dict[str, Any]
    timestamp: datetime
```

Important examples:

```text
manual + manual
webhook + github
scheduled + scheduler
```

`payload` contains the values conditions may inspect. `timestamp` defaults to
the current UTC time.

### `ExecutionContext`

The context contains:

```text
event
data
```

Its `lookup()` method first checks `data`, then checks the event payload:

```text
context.data[field_name]
      ↓ if absent
event.payload[field_name]
```

This gives future actions a place to receive derived runtime data without
changing the event object.

For example:

```python
context.lookup("repository")
```

can read `"repository"` from either the context data or the incoming payload.

## 7. Concrete trigger implementations

### Trigger abstraction

[`backend/app/core/triggers/base.py`](backend/app/core/triggers/base.py)

The `Trigger` abstraction defines one operation:

```python
def should_execute(self, event: Event) -> bool:
    ...
```

The engine calls this method without checking the concrete trigger class.

### `ManualTrigger`

[`backend/app/core/triggers/manual.py`](backend/app/core/triggers/manual.py)

The Phase 1 manual trigger matches when either:

```text
event.type == "manual"
OR
event.source == "manual"
```

This supports operator-initiated runs and simple test events.

### `WebhookTrigger`

[`backend/app/core/triggers/webhook.py`](backend/app/core/triggers/webhook.py)

The webhook trigger requires:

```text
event.type == "webhook"
```

It can optionally restrict the source:

```python
WebhookTrigger(source="github")
```

This matches a GitHub webhook event but rejects a webhook from another source.
The actual HTTP webhook endpoint and provider payload normalization are
deferred to a later phase.

### `ScheduledTrigger`

[`backend/app/core/triggers/scheduled.py`](backend/app/core/triggers/scheduled.py)

The scheduled trigger matches:

```text
event.type == "scheduled"
```

It is a runtime trigger type, not a scheduler. Phase 2 does not start a cron
worker or background scheduler. Render's free-tier sleep behavior makes
reliable scheduling a later, best-effort feature.

### Adding a new trigger

To add a new trigger:

1. Implement `Trigger`.
2. Add the new type to `TriggerFactory`.
3. Export it from the trigger package if it is part of the public core API.
4. Add focused tests.

`WorkflowEngine` should not need to change.

## 8. Concrete condition implementations

### Condition abstraction

[`backend/app/core/conditions/base.py`](backend/app/core/conditions/base.py)

The `Condition` abstraction defines:

```python
def evaluate(self, context: ExecutionContext) -> bool:
    ...
```

Returning `True` means the workflow may continue. Returning `False` means the
engine skips actions.

### Equality

[`backend/app/core/conditions/equals.py`](backend/app/core/conditions/equals.py)

```text
EqualsCondition(field="repository", value="FlowForge")
```

It evaluates whether the looked-up value equals the configured value.

### Not equal

[`backend/app/core/conditions/comparison.py`](backend/app/core/conditions/comparison.py)

```text
NotEqualsCondition(field="status", value="closed")
```

It evaluates the opposite of equality.

### Greater than and less than

These conditions compare values:

```text
GreaterThanCondition(field="priority", value=3)
LessThanCondition(field="attempts", value=5)
```

If Python cannot compare the values because their types are incompatible, the
condition returns `False` rather than allowing a `TypeError` to break normal
workflow evaluation.

### Contains

```text
ContainsCondition(field="labels", value="bug")
```

This can test membership in a list, string, or another compatible container.
An incompatible value returns `False`.

### Composite conditions

[`backend/app/core/conditions/composite.py`](backend/app/core/conditions/composite.py)

`AndCondition` evaluates all child conditions:

```text
condition_1 AND condition_2 AND condition_3
```

Python's `all()` provides short-circuit behavior. Once one child returns
`False`, the remaining children are not needed.

`OrCondition` evaluates whether any child condition passes:

```text
condition_1 OR condition_2 OR condition_3
```

Python's `any()` short-circuits after the first `True` child.

Both composites accept any iterable of `Condition` objects and store the
children as a list.

## 9. Factories: converting data into objects

### [`backend/app/core/factories.py`](backend/app/core/factories.py)

Factories are the bridge between database configuration and runtime
polymorphism.

The database stores:

```text
"equals"
{"field": "repository", "value": "FlowForge"}
```

The engine needs:

```python
EqualsCondition(
    field="repository",
    value="FlowForge",
)
```

The factory performs that conversion.

### `TriggerFactory`

Supported types:

```text
manual
webhook
scheduled
```

Examples:

```python
TriggerFactory.create("manual")
TriggerFactory.create("webhook", {"source": "github"})
TriggerFactory.create("scheduled")
```

An unsupported type raises a clear `ValueError`. It does not silently create
a fallback trigger.

### `ConditionFactory`

Supported comparison types:

```text
equals
not_equals
greater_than
less_than
contains
```

Supported composite types:

```text
and
or
```

Composite configuration has this form:

```json
{
  "conditions": [
    {
      "type": "equals",
      "config": {
        "field": "repository",
        "value": "FlowForge"
      }
    },
    {
      "type": "contains",
      "config": {
        "field": "labels",
        "value": "bug"
      }
    }
  ]
}
```

The factory recursively creates the child conditions.

Required scalar configuration such as `field` and `value` is checked by the
private `_required()` helper. Missing values produce a `ValueError` instead of
creating a partially configured condition.

### `ActionFactory`

Week 2 supports:

```text
noop
```

The factory still exists now because future actions should be added through
registration logic in this boundary, not through an engine type switch.

### Why the engine does not contain factory branches

This is intentionally avoided:

```python
if action_type == "http":
    ...
elif action_type == "github":
    ...
```

Instead:

```python
action = ActionFactory.create(action_type, config)
action.execute(context)
```

This keeps the engine closed for modification when new triggers, conditions, or
actions are added.

## 10. The runtime `Workflow` object

### [`backend/app/core/workflow.py`](backend/app/core/workflow.py)

The runtime workflow contains:

```text
name
trigger
condition
actions
```

Its fields use abstractions:

```python
trigger: Trigger
condition: Condition | None
actions: list[Action]
```

The runtime object is intentionally different from the SQLAlchemy `Workflow`
model:

| Persistence model | Runtime model |
| --- | --- |
| Stores IDs and JSON | Stores behavior objects |
| Used for database access | Used for execution |
| Configuration data | Executable composition |

The runtime workflow does not execute itself. `WorkflowEngine` owns the
execution algorithm.

## 11. `WorkflowEngine`

### [`backend/app/core/engine.py`](backend/app/core/engine.py)

The engine coordinates the pipeline in a fixed order:

```text
1. Evaluate trigger
2. Build execution context
3. Evaluate condition
4. Execute actions in order
5. Return an EngineResult
```

### Step 1: trigger evaluation

```python
if not workflow.trigger.should_execute(event):
    return EngineResult(
        status=ExecutionStatus.SKIPPED,
        error="Trigger did not match",
    )
```

If the trigger does not match, no condition or action runs.

### Step 2: context creation

When the trigger matches, the engine creates:

```python
ExecutionContext(event=event)
```

The normalized event becomes available to every condition and action.

### Step 3: condition evaluation

If a condition exists and returns `False`, the engine returns:

```text
status = SKIPPED
error  = "Conditions did not match"
```

This is not a failed execution. The workflow was evaluated successfully, but
its rules intentionally prevented the actions from running.

### Step 4: ordered action execution

The engine loops over `workflow.actions`:

```python
for action in workflow.actions:
    action.execute(context)
```

The engine only knows the `Action` abstraction. It does not know whether an
action is a no-op, HTTP request, email sender, or GitHub operation.

### Step 5: result creation

The engine returns an immutable `EngineResult`:

```text
status
action_count
error
```

The action count indicates how many actions completed before the result was
returned.

### Failure handling

If an action raises an exception, the engine returns:

```text
status = FAILED
error  = "Action execution failed"
```

The error returned to the caller is deliberately generic. Internal exception
details, credentials, tokens, and provider responses must not be written into
execution history.

## 12. Execution statuses

### `SUCCESS`

The trigger matched, the conditions matched, and all actions completed.

### `SKIPPED`

The workflow did not run its actions because:

```text
the trigger did not match
OR
the conditions did not match
```

### `FAILED`

The trigger and conditions passed, but an action raised an exception.

The distinction between `SKIPPED` and `FAILED` matters for execution history:

```text
SKIPPED → workflow rules prevented work
FAILED  → workflow tried to perform work but an action failed
```

## 13. Repository and service orchestration

### [`backend/app/repositories/workflow.py`](backend/app/repositories/workflow.py)

`WorkflowRepository` currently exposes two focused operations:

```text
get(workflow_id)
add(workflow)
```

It owns the direct SQLAlchemy lookup and flush operations used by the service.
The route does not need to know how the model is loaded.

### [`backend/app/services/workflow.py`](backend/app/services/workflow.py)

`WorkflowService` is the application-level coordinator.

### Creating configuration

`create()`:

1. Verifies that the requested user exists.
2. Creates the parent `Workflow`.
3. Creates a `WorkflowTrigger`.
4. Converts request conditions into `WorkflowCondition` rows.
5. Converts request actions into ordered `WorkflowAction` rows.
6. Flushes the session so IDs are available.

The service stores configuration. It does not execute the workflow during
creation.

### Loading runtime objects

`load_runtime()`:

1. Retrieves the stored workflow.
2. Rejects missing workflows or workflows without triggers.
3. Calls `TriggerFactory`.
4. Hydrates one condition directly, or combines multiple conditions with an
   implicit `AndCondition`.
5. Calls `ActionFactory` for every stored action.
6. Returns both the stored model and runtime `Workflow`.

Returning both objects lets `run_manual()` use the database ID for the
execution record while passing only the runtime object into the engine.

### Running manually

`run_manual()`:

1. Calls `load_runtime()`.
2. Creates a normalized manual event.
3. Calls `WorkflowEngine.execute()`.
4. Copies the engine result into an `Execution` row.
5. Flushes and returns the execution record.

The service is where persistence and runtime behavior meet. The core engine
still does not import SQLAlchemy.

## 14. API routes

### [`backend/app/api/routes/workflows.py`](backend/app/api/routes/workflows.py)

The route module is intentionally thin.

### `POST /api/workflows`

This route:

1. Receives a `WorkflowCreate` Pydantic model.
2. Calls `WorkflowService.create()`.
3. Converts `ValueError` into an HTTP 400 response.
4. Returns `WorkflowResponse`.

### `GET /api/workflows/{workflow_id}`

This route:

1. Loads the workflow through the service repository.
2. Returns HTTP 404 when it does not exist.
3. Returns the safe workflow summary.

### `POST /api/workflows/{workflow_id}/run`

This route:

1. Receives a `ManualRunRequest`.
2. Calls `WorkflowService.run_manual()`.
3. Returns HTTP 404 when the workflow configuration is missing.
4. Returns `ExecutionResponse`.

The route does not contain trigger, condition, or action logic. That belongs in
the core and service layers.

## 15. Tests and what they prove

### [`backend/tests/conftest.py`](backend/tests/conftest.py)

The test database is an in-memory SQLite database. It creates all SQLAlchemy
tables for each test and removes them afterward.

The SQLite connection uses:

```python
check_same_thread=False
```

This is required because the FastAPI test client can execute request handling
in a different thread from the test function.

### [`backend/tests/test_engine.py`](backend/tests/test_engine.py)

These tests prove:

- Factories construct nested composite conditions.
- Greater-than, less-than, not-equal, and OR conditions work.
- Trigger mismatch skips actions.
- Condition mismatch skips actions.
- Multiple actions execute.
- Action count is recorded.

The tests use the core classes directly, so they validate the engine without
requiring HTTP or a database.

### [`backend/tests/test_workflow_service.py`](backend/tests/test_workflow_service.py)

This test proves the persistence-to-runtime path:

```text
create request
      ↓
database configuration
      ↓
factory hydration
      ↓
manual engine execution
      ↓
execution record
```

It asserts that a matching condition produces:

```text
status = SUCCESS
action_count = 1
error = None
```

### [`backend/tests/test_workflow_api.py`](backend/tests/test_workflow_api.py)

This test verifies the user-facing backend path:

```text
POST workflow
      ↓
GET workflow
      ↓
POST manual run
      ↓
SUCCESS response
```

The test overrides the database dependency so the API uses the isolated test
session.

### Existing Phase 1 tests

The Phase 1 tests remain part of the suite:

- [`backend/tests/test_health.py`](backend/tests/test_health.py)
- [`backend/tests/test_models.py`](backend/tests/test_models.py)
- [`backend/tests/test_oop.py`](backend/tests/test_oop.py)

Together with the Phase 2 tests, the current backend suite contains 12 passing
tests.

## 16. What is implemented versus deferred

### Implemented in Phase 2

- Manual, webhook, and scheduled trigger classes.
- Equality, inequality, numeric comparison, and contains conditions.
- AND and OR composite conditions.
- Runtime factories.
- Framework-independent workflow engine.
- Ordered action execution.
- Execution statuses.
- Execution records.
- Workflow configuration creation.
- Workflow loading.
- Manual execution API.
- Core, service, and API regression tests.

### Intentionally deferred

- Supabase authentication.
- Workflow ownership checks based on the authenticated session.
- Workflow update and delete endpoints.
- Execution history list/detail endpoints.
- Real HTTP actions.
- GitHub actions.
- Email actions.
- Webhook HTTP ingestion.
- A production scheduler.
- Retry queues and distributed workers.
- Frontend workflow builder and dashboard.
- PostgreSQL migrations.

The deferred items are not hidden engine requirements. They are later product
slices that will call the same core boundaries.

## 17. Why actions are deterministic in Week 2

The documented MVP eventually needs HTTP and GitHub integrations, but adding
network behavior at the same time as the engine would make it difficult to
separate orchestration failures from integration failures.

The deterministic `NoOpAction` allows the project to prove:

```text
the correct action is hydrated
the action is called only after trigger/condition checks
multiple actions preserve order
execution records contain the right status
```

It also prevents the initial engine tests from depending on:

- Internet availability.
- External API credentials.
- Provider rate limits.
- Network latency.
- Third-party API response changes.

When HTTP actions are added, they must include:

```text
http/https-only URL validation
private and loopback address blocking
request timeouts
payload-size limits
safe error handling
secret-safe execution records
```

## 18. Example walkthrough

Assume this saved workflow:

```text
Name: Notify on FlowForge repository
Trigger: manual
Condition: repository equals "FlowForge"
Action: noop
```

The client runs it with:

```json
{
  "payload": {
    "repository": "FlowForge"
  }
}
```

### Stored configuration

The database contains:

```text
workflows
  name = "Notify on FlowForge repository"

workflow_triggers
  trigger_type = "manual"
  config = {}

workflow_conditions
  condition_type = "equals"
  config = {"field": "repository", "value": "FlowForge"}

workflow_actions
  position = 0
  action_type = "noop"
  config = {}
```

### Hydration

Factories create:

```python
ManualTrigger()
EqualsCondition(
    field="repository",
    value="FlowForge",
)
NoOpAction()
```

These objects are composed into:

```python
Workflow(
    name="Notify on FlowForge repository",
    trigger=manual_trigger,
    condition=equals_condition,
    actions=[noop_action],
)
```

### Execution

The engine:

1. Sees a manual event.
2. The manual trigger returns `True`.
3. The context looks up `repository`.
4. The equality condition returns `True`.
5. The no-op action executes.
6. The engine returns `SUCCESS` and `action_count = 1`.

### Recording

The service stores:

```json
{
  "status": "SUCCESS",
  "trigger_data": {
    "repository": "FlowForge"
  },
  "result": {
    "action_count": 1
  },
  "error": null
}
```

If the payload contained `"repository": "OtherProject"`, the action would not
run and the execution would be recorded as:

```json
{
  "status": "SKIPPED",
  "result": {
    "action_count": 0
  },
  "error": "Conditions did not match"
}
```

## 19. How to run and extend Phase 2

From the repository root:

```powershell
& .\.venv\Scripts\python.exe -m pytest backend\tests -q
```

To compile the backend:

```powershell
& .\.venv\Scripts\python.exe -m compileall -q backend\app backend\tests
```

To start the API locally:

```powershell
Set-Location backend
& ..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Then create a user in the local database or through a test fixture and call:

```text
POST /api/workflows
GET /api/workflows/{workflow_id}
POST /api/workflows/{workflow_id}/run
```

### Adding a condition

1. Create a class implementing `Condition`.
2. Add its type to `ConditionFactory`.
3. Export it from `conditions/__init__.py` when appropriate.
4. Add unit tests for matching and non-matching input.

### Adding an action

1. Create a class implementing `Action`.
2. Add its type to `ActionFactory`.
3. Keep external integration code inside the action or an integration boundary,
   not inside `WorkflowEngine`.
4. Add tests using mocked or deterministic dependencies.

### Adding a trigger

1. Create a class implementing `Trigger`.
2. Add its type to `TriggerFactory`.
3. Normalize provider input into `Event` before the engine sees it.
4. Add matching and rejection tests.

The engine should remain unchanged for all three extensions.

## 20. Important current limitations

### Authentication is not active

The API accepts a `user_id` in the create request and verifies that the user
exists. It does not yet derive the user from an authenticated Supabase
session, and it does not yet enforce ownership on read or run operations.

### `enabled` is stored but not enforced

The workflow model has an `enabled` flag. The current manual-run path does not
reject a disabled workflow. Enable/disable policy belongs in the next service
iteration when workflow lifecycle endpoints are added.

### Scheduled execution is not automatic

`ScheduledTrigger` can evaluate a normalized scheduled event, but nothing
creates those events automatically yet.

### Composite persistence is still being expanded

The factory supports nested composite configuration. The current service
combines multiple top-level condition rows as an implicit AND. Full persisted
condition trees using `parent_id` will be needed when the frontend builder
supports nested condition groups.

### Local database initialization is not migration management

Phase 2 continues to use SQLAlchemy `create_all()` for local development.
Production PostgreSQL migration management is a later deployment concern.

## 21. Phase 2 mental model

The simplest way to remember the architecture is:

```text
Configuration is data.
Factories turn data into objects.
The engine executes objects.
The service records results.
Routes expose the service.
```

Or as a single diagram:

```text
                         POST /api/workflows
                                  │
                                  ▼
                         WorkflowCreate schema
                                  │
                                  ▼
                         WorkflowService.create
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
        Workflow row       Trigger row          Condition/action rows
                                  │
                                  │ later load
                                  ▼
                         WorkflowService.load_runtime
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              TriggerFactory  ConditionFactory  ActionFactory
                    │             │             │
                    └─────────────┼─────────────┘
                                  ▼
                           Runtime Workflow
                                  │
                                  ▼
                         WorkflowEngine.execute
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
                SKIPPED        FAILED        SUCCESS
                                  │
                                  ▼
                            Execution row
```

The main achievement of Phase 2 is that this pipeline is now executable and
tested. The frontend, authentication, and real integrations can be added
around it without moving execution logic into the browser or route handlers.
