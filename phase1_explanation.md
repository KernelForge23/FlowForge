# FlowForge Phase 1 Backend Explanation

> This document explains the backend that exists today. It describes the
> implementation in the repository, not the complete backend planned for the
> MVP. Phase 1 is the foundation slice: the application can start, expose a
> health endpoint, create the initial database tables, persist a basic workflow
> configuration, and demonstrate the first object-oriented workflow building
> blocks.

## 1. What Phase 1 is trying to prove

FlowForge is designed around  workflow:

```text
WHEN a trigger arrives
IF the conditions match
THEN run one or more actions
```

The most important Phase 1 decision is that this workflow is represented by
real Python objects and interfaces. The engine should eventually call a
`Trigger`, a `Condition`, and one or more `Action` objects without knowing
which concrete provider each object represents.

Phase 1 therefore establishes four foundations:

1. **A FastAPI application** that can start and respond to HTTP requests.
2. **A database model** for users, workflows, workflow configuration,
   integrations, and future execution history.
3. **An object-oriented core** with `Trigger`, `Condition`, and `Action`
   abstractions.
4. **Tests** that prove the API, persistence model, and first concrete core
   implementations work independently.

It is not yet the complete workflow product. There is no workflow CRUD API, no
authentication, no factory layer, and no `WorkflowEngine` that coordinates
trigger evaluation, condition evaluation, action execution, and execution
records. Those are later slices.

## 2. How the backend is organized

The backend is under [`backend/`](backend/). Its intended layers are:

| Layer | Location | Responsibility |
| --- | --- | --- |
| HTTP/API | `app/api/` | Routes, routers, and HTTP-level dependency wiring |
| Schemas | `app/schemas/` | Pydantic request/response contracts |
| Services | `app/services/` | Application operations called by routes |
| Core engine | `app/core/` | Framework-independent workflow concepts and behavior |
| Repositories | `app/repositories/` | Intended database access layer; not implemented yet |
| Models | `app/models/` | SQLAlchemy persistence mappings |
| Database infrastructure | `app/db.py` | Engine, sessions, and table initialization |
| Application configuration | `app/config.py` | Environment-driven settings |
| Tests | `tests/` | API, persistence, and OOP behavior checks |

The separation matters because the browser should configure workflows through
the API, while the backend owns execution. The `core` package should remain
usable without FastAPI or SQLAlchemy, which makes the workflow behavior easier
to test and keeps vendor integrations out of the engine itself.

## 3. Startup and request flow

### Application startup

[`app/main.py`](backend/app/main.py) creates the FastAPI application. Its
lifespan handler calls `init_db()` during startup. In Phase 1, `init_db()`
uses SQLAlchemy metadata to create tables that do not already exist. This is a
simple greenfield bootstrap, not a production migration system.

The application then includes the central router from
[`app/api/routes/__init__.py`](backend/app/api/routes/__init__.py). That central
router currently includes only the health router.

### A health request

The current request path is:

```text
GET /health
  -> health route
  -> HealthService.status()
  -> HealthResponse
  -> JSON response
```

[`app/api/routes/health.py`](backend/app/api/routes/health.py) handles the
HTTP route and obtains a `HealthService`. The service constructs the result,
and [`app/schemas/health.py`](backend/app/schemas/health.py) gives the result
its typed shape:

```json
{
  "status": "ok",
  "service": "flowforge"
}
```

This may look like more layers than a one-line endpoint needs, but it
demonstrates the pattern intended for larger features: routes handle HTTP,
services handle application operations, and schemas define API contracts.

### A future workflow request

The same separation will eventually support a flow like:

```text
HTTP route
  -> request schema validation
  -> workflow service
  -> repository reads configuration rows
  -> factory creates Trigger/Condition/Action objects
  -> WorkflowEngine executes the runtime workflow
  -> repository stores an Execution row
  -> response schema returns safe result data
```

Only the first health portion exists in Phase 1. The database and core
building blocks exist so later phases can fill in the middle of this flow.

## 4. Configuration and package files

### [`backend/.env.example`](backend/.env.example)

This documents the environment variable used for the database connection. The
local default is a SQLite URL such as:

```text
DATABASE_URL=sqlite:///./flowforge.db
```

The file is an example, not a secret store. It gives a developer a safe
starting point for local setup and shows the configuration name expected by
the application.

The important architectural reason for `DATABASE_URL` is that database choice
belongs in configuration. Local Phase 1 uses SQLite, while the intended
deployed database is PostgreSQL through Supabase. Application code should not
need to change just because the environment changes.

### [`backend/requirements.txt`](backend/requirements.txt)

This declares the Python packages used by the backend:

- **FastAPI** provides the web framework and dependency system.
- **Uvicorn** runs the ASGI application locally and in deployment.
- **SQLAlchemy** maps Python model classes to database tables and manages
  database sessions.
- **Pydantic** defines typed validation and response models.
- **Pydantic Settings** reads typed settings from environment variables and
  `.env`.
- **HTTPX** supports API testing and is available for future HTTP integrations.
- **python-dotenv** supports loading local environment values.
- **pytest** runs the automated test suite.

The dependency list reflects the current foundation. It does not imply that
all planned integrations or execution features already exist.

### [`backend/pytest.ini`](backend/pytest.ini)

This configures pytest so tests can import the application package from the
backend directory and so pytest discovers the tests under `backend/tests/`.
Keeping this setup in the repository makes test commands reproducible instead
of depending on a developer's shell configuration.

### Package marker files

The following files mark directories as Python packages and provide stable
module boundaries:

- [`backend/app/__init__.py`](backend/app/__init__.py)
- [`backend/app/api/__init__.py`](backend/app/api/__init__.py)
- [`backend/app/core/__init__.py`](backend/app/core/__init__.py)
- [`backend/app/core/actions/__init__.py`](backend/app/core/actions/__init__.py)
- [`backend/app/core/conditions/__init__.py`](backend/app/core/conditions/__init__.py)
- [`backend/app/core/triggers/__init__.py`](backend/app/core/triggers/__init__.py)
- [`backend/app/models/__init__.py`](backend/app/models/__init__.py)
- [`backend/app/repositories/__init__.py`](backend/app/repositories/__init__.py)
- [`backend/app/schemas/__init__.py`](backend/app/schemas/__init__.py)
- [`backend/app/services/__init__.py`](backend/app/services/__init__.py)
- [`backend/app/api/routes/__init__.py`](backend/app/api/routes/__init__.py)

Most are intentionally small. Their value is organizational: imports can use
clear package paths, and related modules have an explicit home. Some package
initializers also re-export the public classes of a subpackage, as described
below.

## 5. Application configuration and database infrastructure

### [`backend/app/config.py`](backend/app/config.py)

This module defines the application settings boundary. Its `Settings` class
extends Pydantic Settings and reads values from the environment and `.env`.
Unknown environment variables are ignored, which prevents unrelated variables
from unexpectedly becoming settings fields.

The settings object provides a local SQLite default. The default makes the
foundation runnable without a hosted database, while the environment override
keeps the code ready for PostgreSQL later.

This module is required because hard-coding a connection string inside
`db.py` would make local development, tests, and deployment tightly coupled.
Configuration is a dependency of the database layer, not something individual
routes should manage.

### [`backend/app/db.py`](backend/app/db.py)

This module owns SQLAlchemy's database infrastructure:

- It creates the engine from `settings.database_url`.
- When the URL is SQLite, it enables SQLite's
  `check_same_thread=False` option so the database can be used through
  FastAPI's request/test threading behavior.
- It defines `SessionLocal`, the session factory used to create database
  sessions.
- `init_db()` calls `Base.metadata.create_all(...)` to create missing tables.
- `get_session()` is a generator dependency that yields a session and
  commits, rolls back on an exception, and closes the session afterward.

The session dependency is the boundary that future routes and services will
use. A route should receive a session through dependency injection rather than
creating a global session or manually opening connections.

`create_all()` is acceptable for this early greenfield slice, but it is not a
substitute for migrations in production. Once the schema evolves or the
application is deployed to Supabase, a deliberate migration strategy is
required.

### [`backend/app/main.py`](backend/app/main.py)

This is the ASGI application entry point:

1. Create a FastAPI app named `FlowForge`.
2. Register the lifespan handler.
3. Initialize database tables at startup.
4. Include the central API router.

Keeping startup wiring here gives Uvicorn one obvious import target and keeps
route modules from owning application construction.

## 6. SQLAlchemy model layer

### [`backend/app/models/base.py`](backend/app/models/base.py)

This module defines shared model infrastructure:

- `new_id()` generates string UUID values for new records.
- `Base` is the SQLAlchemy declarative base from which mapped classes inherit.
- `TimestampMixin` adds a server-generated `created_at` column.

String UUIDs are a practical portable choice for this project. They work with
the local SQLite foundation and remain suitable when the database moves to
PostgreSQL. The declarative base also gives `init_db()` one metadata registry
from which it can create all imported tables.

### [`backend/app/models/entities.py`](backend/app/models/entities.py)

This module contains the persisted domain entities. These rows store workflow
configuration as data. They do **not** serialize Python objects into the
database.

#### `User`

`User` stores an ID and unique email address. It owns workflows and
integrations through SQLAlchemy relationships.

The model is a persistence foundation for ownership and authentication. The
presence of the table does not mean authentication is implemented; Supabase
Auth integration and current-user enforcement are still deferred.

#### `Workflow`

`Workflow` is the persisted definition of a workflow. It stores ownership,
name, enabled state, creation time, and update time. Relationships connect it
to:

- one trigger configuration,
- many condition configurations,
- ordered action configurations,
- execution history rows.

Cascade behavior is configured for workflow-owned trigger, condition, and
action configuration so deleting a workflow does not leave those dependent
configuration rows behind.

This model is deliberately different from the in-memory core `Workflow`.
The SQLAlchemy class represents durable database data. The core class
represents runtime behavior. A future factory/service layer will translate
between them.

#### `WorkflowTrigger`

This stores one trigger configuration for a workflow. It contains a
`trigger_type` discriminator and a JSON `config` object.

For example, a future row might say that the trigger type is `webhook` and
contain provider-specific configuration. The database stores the description;
a factory will later turn that description into a concrete `Trigger` object.

#### `WorkflowCondition`

This stores a condition's type and JSON configuration. It also contains a
`parent_id`, anticipating nested condition trees such as AND/OR groups.

The column is a forward-looking schema choice, not a complete composite
condition implementation. Recursive SQLAlchemy relationship wiring and
runtime tree construction do not yet exist.

#### `Integration`

This stores a user-owned provider and JSON configuration. It is the future
connection between a workflow action and an external service such as an email
provider, GitHub, or an HTTP destination.

Credentials must eventually be handled carefully. Secrets must not be copied
into execution history, API responses, or logs.

#### `WorkflowAction`

This stores an action type, JSON configuration, optional integration
reference, and an integer `position`.

`position` preserves the order in which multiple actions should run. The
`integration_id` lets an action refer to a reusable provider connection
without putting the provider implementation inside the action row.

The table is configuration only in Phase 1. There is no concrete email,
HTTP, or GitHub action yet.

#### `Execution`

This table is prepared for execution history. It stores the workflow
relationship, execution status, timestamps, trigger data, result data, and an
error field.

The important limitation is that no current code creates or updates these
rows. There is not yet a coordinator that sets `PENDING`, `RUNNING`,
`SUCCESS`, or `FAILED`, records action results, or implements retries. The
schema exists ahead of the execution behavior so later phases have a durable
place to record results.

### [`backend/app/models/__init__.py`](backend/app/models/__init__.py)

This module re-exports `Base` and the mapped entity classes. It also helps
ensure the model modules are imported before `Base.metadata.create_all()` runs.
Without importing the mapped classes, SQLAlchemy's metadata registry may not
know about the tables that should be created.

## 7. The framework-independent OOP core

The `core` package is the most important architectural part of Phase 1. It
should not depend on FastAPI, SQLAlchemy, or a specific vendor. That
independence lets the workflow behavior be tested as ordinary Python and
keeps the engine closed to changes when new integrations are added.

### [`backend/app/core/event.py`](backend/app/core/event.py)

This module defines the normalized runtime input:

#### `Event`

An `Event` contains:

- `type`: the event category, such as `manual`,
- `source`: where it came from,
- `payload`: provider or user data,
- a UTC timestamp.

The purpose is normalization. A GitHub webhook and a manual test request may
have completely different external shapes, but the core can consume one
internal event representation.

#### `ExecutionContext`

`ExecutionContext` wraps an event and additional runtime data. Its
`lookup()` method checks explicitly supplied context data first, then falls
back to the event payload.

This gives conditions one consistent way to read values without knowing
whether a value came from the normalized event or from information added while
execution was in progress.

### [`backend/app/core/workflow.py`](backend/app/core/workflow.py)

The core `Workflow` is an in-memory composition object. It stores:

- a name,
- one `Trigger`,
- one `Condition`,
- a list of `Action` objects.

It does not yet have a `run()` method and it does not persist itself. That
separation is intentional: the object describes the runtime pieces, while a
future `WorkflowEngine` will coordinate execution and a service/repository
layer will load and save configuration.

### [`backend/app/core/triggers/base.py`](backend/app/core/triggers/base.py)

This defines the abstract `Trigger` interface:

```python
should_execute(event: Event) -> bool
```

The future engine should ask the interface whether an incoming event matches.
It should not contain `if trigger_type == "github"` or similar vendor-specific
branches. New trigger classes can then be added without modifying the engine.

### [`backend/app/core/triggers/manual.py`](backend/app/core/triggers/manual.py)

`ManualTrigger` is the first concrete trigger. It matches an event whose type
is `"manual"` or whose source is `"manual"`.

It is intentionally small, but it proves the trigger contract and gives the
project a dependable way to exercise workflows before webhook signatures,
provider payload normalization, and scheduling are implemented.

### [`backend/app/core/triggers/__init__.py`](backend/app/core/triggers/__init__.py)

This re-exports `Trigger` and `ManualTrigger`, giving callers a stable import
surface such as the triggers package rather than requiring knowledge of every
implementation module.

### [`backend/app/core/conditions/base.py`](backend/app/core/conditions/base.py)

This defines the abstract `Condition` interface:

```python
evaluate(context: ExecutionContext) -> bool
```

Conditions are the IF part of a workflow. The future engine will stop before
executing actions when a condition evaluates to false.

### [`backend/app/core/conditions/equals.py`](backend/app/core/conditions/equals.py)

`EqualsCondition` receives a field name and expected value. It asks the
execution context for the field and returns whether the actual value equals
the expected value.

This is the first proof that conditions read normalized runtime data through
the shared context rather than directly depending on a provider payload.
Future condition classes can implement not-equal, greater-than, contains, and
composite AND/OR behavior behind the same interface.

### [`backend/app/core/conditions/__init__.py`](backend/app/core/conditions/__init__.py)

This re-exports `Condition` and `EqualsCondition` as the public condition
package surface.

### [`backend/app/core/actions/base.py`](backend/app/core/actions/base.py)

This defines the abstract action interface:

```python
execute(context: ExecutionContext) -> None
```

The future engine will call this interface without knowing whether the
implementation sends an email, makes an HTTP request, calls GitHub, or does
something else. This is the key to keeping vendor behavior out of the
workflow coordinator.

### [`backend/app/core/actions/noop.py`](backend/app/core/actions/noop.py)

`NoOpAction` is a safe testing action. It performs no network side effect and
records each received execution context in its `calls` collection.

That makes it useful for proving action dispatch: a test can run a composed
workflow and assert that exactly one action call occurred, without sending
real data to an external service.

### [`backend/app/core/actions/__init__.py`](backend/app/core/actions/__init__.py)

This re-exports `Action` and `NoOpAction`.

### [`backend/app/core/__init__.py`](backend/app/core/__init__.py)

This is the package-level export boundary for the core. The behavior remains
in the event, workflow, trigger, condition, and action modules; the initializer
keeps the package organized and gives later code a consistent import location.

## 8. API, schema, and service layers

### [`backend/app/api/routes/__init__.py`](backend/app/api/routes/__init__.py)

This creates the central `api_router` and includes the health router. It is the
composition point where future routers should be added for workflows,
executions, and webhooks.

Centralizing router inclusion keeps `main.py` small and makes the API surface
easy to inspect.

### [`backend/app/api/routes/health.py`](backend/app/api/routes/health.py)

This module defines `GET /health`. It creates or receives a `HealthService`
dependency and returns a typed `HealthResponse`.

The route does not query SQLAlchemy or contain workflow logic. That is
important because route functions should translate HTTP input/output, not
become a second application layer.

### [`backend/app/schemas/health.py`](backend/app/schemas/health.py)

`HealthResponse` is a Pydantic response model with `status` and `service`
fields. FastAPI uses it to validate and document the response shape.

This is the pattern future workflow schemas should follow: validate API
boundaries with Pydantic rather than passing unvalidated dictionaries deep
into the application.

### [`backend/app/services/health.py`](backend/app/services/health.py)

`HealthService.status()` constructs the standard health response. The
operation is intentionally simple, but it demonstrates the intended
route-to-service boundary.

Future services should orchestrate repository access, factories, and the
engine. They should not make the route responsible for database transactions
or runtime workflow assembly.

### Empty repository package

[`backend/app/repositories/__init__.py`](backend/app/repositories/__init__.py)
marks the intended repository layer, but no repository implementation exists
yet. A future repository will encapsulate workflow and execution persistence
queries so services do not spread SQLAlchemy query details across route
functions.

## 9. Tests and what they prove

### [`backend/tests/conftest.py`](backend/tests/conftest.py)

The shared pytest setup keeps tests isolated from the local
`backend/flowforge.db` file:

- It sets an in-memory SQLite `DATABASE_URL` before importing the application.
- The `client` fixture creates a FastAPI `TestClient`.
- The `db_session` fixture creates a separate in-memory database, creates all
  tables, yields a SQLAlchemy session, commits and closes it, and removes the
  test tables afterward.

The ordering of the environment setup matters. Configuration is read when the
application/database modules are imported, so the test database must be
selected before those imports happen.

### [`backend/tests/test_health.py`](backend/tests/test_health.py)

This verifies the public health contract:

- `GET /health` returns HTTP 200.
- The response status is `"ok"`.
- The service name is `"flowforge"`.

It proves the FastAPI app starts, the router is included, dependency wiring
works, and the response schema matches the expected JSON.

### [`backend/tests/test_models.py`](backend/tests/test_models.py)

This performs a basic persistence round trip:

1. Create a `User`.
2. Create an enabled `Workflow`.
3. Attach a manual trigger with JSON configuration.
4. Attach an equality condition.
5. Attach a no-op action.
6. Flush and reload the workflow.
7. Assert that relationships and JSON configuration survive persistence.

This proves the foundational schema can represent a basic workflow
configuration. It does not prove complete CRUD, ownership enforcement,
runtime hydration, or execution history behavior.

### [`backend/tests/test_oop.py`](backend/tests/test_oop.py)

This verifies the framework-independent core:

- A manual event matches `ManualTrigger`.
- A webhook event does not match `ManualTrigger`.
- `EqualsCondition` returns true for matching data and false for nonmatching
  data.
- A composed workflow can dispatch through the abstract `Action` type.
- `NoOpAction` records one execution call.

This is an abstraction and composition test. It is not yet a full engine test
because `WorkflowEngine` has not been implemented.

## 10. What is implemented versus deferred

### Implemented in Phase 1

- FastAPI application startup.
- Lifespan-based local table initialization.
- Environment-driven database URL configuration.
- SQLite database support for local development and tests.
- SQLAlchemy base, timestamp, UUID, and domain entity mappings.
- User/workflow/trigger/condition/action/integration/execution schema.
- Normalized `Event` and `ExecutionContext` objects.
- Abstract `Trigger`, `Condition`, and `Action` contracts.
- `ManualTrigger`, `EqualsCondition`, and `NoOpAction`.
- In-memory core workflow composition.
- `GET /health`.
- Tests for health, model relationships, JSON persistence, and OOP behavior.

### Deferred to later phases

- `WorkflowEngine` coordination and execution lifecycle.
- Trigger, condition, and action factories.
- Webhook receivers, signature validation, and provider event normalization.
- Scheduled triggers (best effort because Render can sleep).
- Additional comparison and AND/OR composite conditions.
- Real HTTP, email, GitHub, and other integration actions.
- SSRF protection, timeouts, and payload limits for generic HTTP actions.
- Workflow, execution, and webhook API endpoints.
- Workflow repositories and application services.
- Execution creation, status transitions, safe result/error storage, and
  retries.
- Supabase Auth, token validation, ownership checks, and authorization.
- PostgreSQL deployment and migration management.

The database has placeholders for some future capabilities, but a table or
column alone is not an implemented feature. For example, `Execution` exists,
but no current code records executions.

## 11. Why configuration rows become runtime objects

The database stores data such as:

```text
trigger_type = "manual"
config = {...}
```

The core needs an object implementing `Trigger`:

```text
ManualTrigger(...)
```

The intended later flow is:

```text
database row
  -> TriggerFactory.create(type, config)
  -> Trigger object
  -> WorkflowEngine
```

The same applies to conditions and actions. This is why workflows should be
persisted as configuration and hydrated through factories. Pickling Python
objects would couple stored data to implementation details, make migrations
harder, and create unsafe deployment assumptions.

The engine should remain polymorphic:

```python
for action in workflow.actions:
    action.execute(context)
```

It should not become a collection of vendor checks such as
`if action_type == "email"`. Adding a new action should mean implementing the
action abstraction and registering it with a factory, not editing the engine's
decision tree.

## 12. How to run and extend the Phase 1 backend

From [`backend/`](backend/):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The health endpoint is then available at `http://127.0.0.1:8000/health`.

Run the tests with:

```powershell
pytest
```

When adding a new core type:

1. Define behavior behind the existing abstract interface.
2. Keep the implementation independent of FastAPI and SQLAlchemy.
3. Add focused tests for matching, evaluation, or execution behavior.
4. Add factory registration when factories are introduced.
5. Do not add vendor-specific branches to the engine.

When adding an API feature:

1. Define Pydantic request and response schemas.
2. Keep the route focused on HTTP concerns.
3. Put orchestration in a service.
4. Put database queries in a repository.
5. Enforce ownership and validate external URLs/configuration on the server.
6. Never expose credentials or secret values in execution history or logs.

## 13. Files intentionally not explained as implementation

The backend also contains generated or local data artifacts:

- `backend/flowforge.db` is the local SQLite data file.
- `__pycache__/` directories and `.pyc` files are Python bytecode caches.
- `backend/.pytest_cache/` is pytest's local cache.

These are outputs of running the application or tests, not source files that
define backend behavior. The code that creates and uses the database is
explained in [`app/db.py`](backend/app/db.py) and the model sections above.

## 14. Phase 1 mental model

The simplest accurate mental model is:

```text
Configuration:
  SQLAlchemy rows describe users and workflow parts.

Runtime foundation:
  Event -> ExecutionContext
  Event -> Trigger.should_execute()
  Context -> Condition.evaluate()
  Context -> Action.execute()

Current HTTP surface:
  FastAPI -> /health -> HealthService -> HealthResponse

Not yet connected:
  persisted configuration -> factories -> WorkflowEngine -> Execution
```

Phase 1 is successful when these boundaries are understandable and tested.
The next phase should connect them with factories and an execution engine,
then add the API and integrations around that stable core.
