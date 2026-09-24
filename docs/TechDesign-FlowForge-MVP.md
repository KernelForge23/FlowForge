# Technical Design Document: FlowForge MVP V1

## 1. Executive Summary

**Project:** FlowForge  
**Version:** MVP V1  
**Target Users:** Developers and technically comfortable users  
**Platform:** Web application  
**Development Approach:** Full-code, AI-assisted development  
**Timeline:** 4 weeks  
**Development Budget:** ₹0 / $0  
**Primary Technical Focus:** Object-Oriented workflow execution engine  
**AI Product Features:** Not included in V1; planned for V2

### What is FlowForge?

FlowForge is a web-based workflow automation platform that allows users to connect events, conditions, and actions to automate repetitive tasks.

The fundamental idea is:

```text
WHEN something happens
        ↓
IF certain conditions are satisfied
        ↓
THEN perform one or more actions
```

For example:

```text
WHEN a GitHub Pull Request is merged
        ↓
IF repository = "FlowForge"
        ↓
THEN
    ├── Send notification
    └── Send HTTP request
```

The important distinction is that **GitHub is not the product**.

GitHub, email, webhooks, etc. are simply implementations of FlowForge's more general architecture.

The actual product is:

> **A modular workflow execution engine where users combine triggers, conditions, and actions to create automations.**

---



# 2. V1 Goals

The V1 must achieve two things simultaneously:

### Product goal

Create a genuinely usable automation platform that can be deployed publicly and demonstrated to real users.

### Academic/technical goal

Demonstrate strong implementation of:

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- Interfaces
- Factory Pattern
- Composite Pattern
- Strategy-style polymorphism
- Separation of concerns

The OOP architecture must therefore be part of the **core business logic**.

It should NOT be:

```text
Normal procedural application
        +
random classes added to claim OOP
```

Instead:

```text
Workflow Engine
       ↓
Trigger abstraction
Condition abstraction
Action abstraction
Integration abstraction
       ↓
Concrete implementations
```

The engine itself should depend on the abstractions.

---



# 3. V1 Scope

The four-week constraint is important.

FlowForge could eventually become a very large platform, but V1 will deliberately implement a small number of highly reusable primitives.

## V1 Core Features



### Workflow Management

Users can:

- Create workflow
- View workflows
- Edit workflow
- Delete workflow
- Enable/disable workflow
- Manually execute workflow
- View execution history



### Triggers

V1:

1. Manual Trigger
2. Webhook Trigger
3. GitHub Event Trigger

A Schedule Trigger can be added if time permits.

### Conditions

V1:

1. Equality
2. Contains
3. Greater Than
4. Less Than
5. AND
6. OR

Example:

```text
Repository == "FlowForge"
AND
Author == "John"
```



### Actions

V1:

1. HTTP/Webhook Action
2. Notification/Email Action
3. GitHub Action where practical

The **HTTP/Webhook Action is particularly important** because it prevents FlowForge from becoming restricted to a fixed list of integrations.

A technically comfortable user could connect FlowForge to any service that exposes an HTTP API.

---



# 4. V1 Architecture

The application will use a modular web architecture.

```text
                    ┌─────────────────────┐
                    │     React Web App   │
                    │      Frontend       │
                    └──────────┬──────────┘
                               │
                               │ REST API
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │       Backend       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
        │ Workflow    │ │ Integration │ │ Authentication│
        │ Engine      │ │ Layer       │ │ / Users       │
        └──────┬──────┘ └──────┬──────┘ └──────────────┘
               │                │
               ▼                ▼
       ┌────────────────┐   ┌──────────────┐
       │ OOP Core       │   │ External APIs│
       │                │   │              │
       │ Trigger        │   │ GitHub       │
       │ Condition      │   │ HTTP APIs    │
       │ Action         │   │ Email        │
       │ Workflow       │   │ etc.         │
       └────────────────┘   └──────────────┘
               │
               ▼
        ┌────────────────┐
        │ PostgreSQL DB  │
        └────────────────┘
```

---



# 5. Technology Stack



## Recommended Stack


| Layer             | Technology              |
| ----------------- | ----------------------- |
| Frontend          | React + TypeScript      |
| Build Tool        | Vite                    |
| Styling           | Tailwind CSS            |
| Backend           | Python + FastAPI        |
| OOP Core          | Python                  |
| ORM               | SQLAlchemy              |
| Validation        | Pydantic                |
| Database          | PostgreSQL via Supabase |
| Authentication    | Supabase Auth           |
| Frontend Hosting  | Vercel                  |
| Backend Hosting   | Render                  |
| Version Control   | Git + GitHub            |
| Testing           | pytest                  |
| API Documentation | FastAPI/OpenAPI         |


This stack intentionally separates the frontend from the backend.

```text
React
  ↓
REST API
  ↓
FastAPI
  ↓
OOP Workflow Engine
  ↓
PostgreSQL
```

---



# 6. Why This Stack?



## Option A — React + FastAPI + PostgreSQL



### Advantages

- Python is relatively approachable for the user
- Python has excellent OOP support
- FastAPI makes REST APIs straightforward
- Strong separation between frontend and backend
- Easy to demonstrate OOP independently
- PostgreSQL is suitable for relational workflow data
- Easy to test the OOP engine independently from the UI



### Disadvantages

- Two separate deployments
- More configuration than an all-in-one framework
- Authentication requires some integration work



### Decision

**Recommended.**

The main reason is that FlowForge's academic value is strongly tied to the backend OOP engine.

---



## Option B — Next.js Full Stack



### Advantages

- One project
- One deployment
- Excellent frontend ecosystem
- Easier deployment



### Disadvantages

- Backend OOP architecture becomes less visually distinct
- TypeScript/React/server architecture adds learning overhead
- More difficult to present the workflow engine as an independent OOP system



### Decision

Good alternative, but not selected for V1.

---



## Option C — Django



### Advantages

- Mature Python framework
- Excellent ORM
- Authentication support
- Admin interface



### Disadvantages

- More framework functionality than V1 requires
- Django's conventions can obscure the custom workflow-engine architecture
- More overhead for a four-week project



### Decision

Not selected.

---



# 7. Frontend Architecture

The frontend is responsible for:

- Authentication UI
- Dashboard
- Workflow creation
- Workflow editing
- Workflow listing
- Execution history
- Basic integration configuration

It does NOT contain the workflow execution engine.

```text
React Frontend
      │
      │ REST
      ▼
FastAPI Backend
      │
      ▼
Workflow Engine
```

This separation is important.

The browser should never be responsible for deciding how an action is actually executed.

---



# 8. Frontend Structure

```text
frontend/
│
├── src/
│   │
│   ├── components/
│   │   ├── ui/
│   │   ├── workflow/
│   │   └── dashboard/
│   │
│   ├── pages/
│   │   ├── Login
│   │   ├── Dashboard
│   │   ├── CreateWorkflow
│   │   ├── EditWorkflow
│   │   └── Executions
│   │
│   ├── services/
│   │   └── api.ts
│   │
│   ├── types/
│   │   └── workflow.ts
│   │
│   └── App.tsx
│
├── package.json
└── vite.config.ts
```

---



# 9. Backend Architecture

The backend is the most important technical component.

```text
backend/
│
├── app/
│   │
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies/
│   │
│   ├── core/
│   │   ├── workflow/
│   │   ├── triggers/
│   │   ├── conditions/
│   │   ├── actions/
│   │   ├── integrations/
│   │   └── engine/
│   │
│   ├── models/
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │
│   ├── schemas/
│   │
│   └── main.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

The important distinction is:

```text
api/
    HTTP-related code

core/
    actual FlowForge business logic

models/
    database representation

repositories/
    database access

services/
    application-level coordination
```

---



# 10. The Core OOP Architecture

This is the heart of FlowForge.

The system will have four major abstractions:

```text
Trigger
Condition
Action
Integration
```

A workflow combines them.

```text
                    Workflow
                       │
          ┌────────────┼─────────────┐
          │            │             │
          ▼            ▼             ▼
       Trigger     Condition       Actions
                                      │
                              ┌───────┼───────┐
                              ▼       ▼       ▼
                           Action   Action  Action
                              │
                              ▼
                         Integration
```

---



# 11. Abstraction

Abstraction means exposing what an object can do without forcing the rest of the system to know how it does it.

## Trigger

Conceptually:

```python
class Trigger:
    def should_execute(self, event):
        pass
```

Concrete triggers implement this behavior:

```text
Trigger
   │
   ├── ManualTrigger
   ├── WebhookTrigger
   └── GitHubTrigger
```

The Workflow Engine does not need to know the implementation details.

It simply asks:

```text
"Does this trigger match this event?"
```

---



# 12. Condition Abstraction

```text
Condition
   │
   ├── ComparisonCondition
   ├── ContainsCondition
   ├── GreaterThanCondition
   ├── LessThanCondition
   ├── AndCondition
   └── OrCondition
```

The engine simply calls:

```text
condition.evaluate(context)
```

It doesn't care whether the condition is:

```text
repository == "FlowForge"
```

or:

```text
stars > 100
```

or:

```text
A AND B AND C
```

That implementation is hidden behind the abstraction.

---



# 13. Action Abstraction

```text
Action
   │
   ├── HTTPAction
   ├── EmailAction
   ├── GitHubAction
   └── NotificationAction
```

The engine only knows:

```text
action.execute(context)
```

This is one of the strongest demonstrations of polymorphism in the project.

---



# 14. Integration Abstraction

Actions describe **what should happen**.

Integrations describe **how communication with an external service happens**.

For example:

```text
EmailAction
      │
      ▼
EmailIntegration
      │
      ▼
External Email Provider
```

Similarly:

```text
GitHubAction
      │
      ▼
GitHubIntegration
      │
      ▼
GitHub API
```

And:

```text
HTTPAction
      │
      ▼
HTTP Client
      │
      ▼
Any external API
```

This distinction keeps FlowForge extensible.

---



# 15. Inheritance

Concrete classes inherit from abstract base classes.

```text
             Trigger
                │
       ┌────────┼────────┐
       │        │        │
    Manual   Webhook   GitHub
    Trigger  Trigger   Trigger
```

Similarly:

```text
             Action
                │
       ┌────────┼─────────┐
       │        │         │
      HTTP     Email    GitHub
     Action    Action    Action
```

And:

```text
            Condition
                │
       ┌────────┼───────────┐
       │        │           │
   Comparison  Contains   Composite
                           │
                      ┌────┴────┐
                     AND       OR
```

This is genuine inheritance because all subclasses satisfy the contract defined by their parent abstraction.

---



# 16. Polymorphism

Polymorphism is arguably the most important OOP principle in FlowForge.

The Workflow Engine can maintain:

```text
List<Action>
```

instead of:

```text
List<HTTPAction>
List<EmailAction>
List<GitHubAction>
```

At runtime:

```text
Action
 │
 ├── HTTPAction
 ├── EmailAction
 └── GitHubAction
```

The engine simply does:

```text
for action in workflow.actions:
        action.execute(context)
```

The correct implementation is selected dynamically.

Therefore:

```text
action.execute()
```

could actually execute:

```text
HTTPAction.execute()
```

or:

```text
EmailAction.execute()
```

or:

```text
GitHubAction.execute()
```

without the engine changing.

---



# 17. Why Polymorphism Matters

Suppose FlowForge originally supports:

```text
HTTPAction
EmailAction
GitHubAction
```

Later we add:

```text
SlackAction
DiscordAction
NotionAction
```

The Workflow Engine does not need to become:

```text
if action == Slack:
    ...
elif action == Discord:
    ...
elif action == Notion:
    ...
```

Instead:

```text
Action
   │
   ├── HTTPAction
   ├── EmailAction
   ├── GitHubAction
   ├── SlackAction
   └── DiscordAction
```

The engine remains unchanged.

This is a direct demonstration of the **Open/Closed Principle**.

---



# 18. Encapsulation

Each class controls its own internal state and implementation.

For example:

```text
GitHubIntegration
```

is responsible for:

- API URL
- authentication
- request construction
- API response handling
- error handling

The rest of the system does not need to know those details.

Instead:

```text
GitHubAction
      ↓
GitHubIntegration.create_issue(...)
```

This means API-specific implementation is encapsulated.

---



# 19. Composition

A Workflow is not simply a class that inherits from everything.

Instead, it **contains objects**.

Conceptually:

```text
Workflow
│
├── Trigger
│
├── Condition
│
└── List<Action>
```

For example:

```text
Workflow
│
├── GitHubTrigger
│
├── AndCondition
│      ├── RepositoryCondition
│      └── AuthorCondition
│
└── Actions
       ├── EmailAction
       └── HTTPAction
```

This is composition.

It is one of the reasons the architecture can remain flexible.

---



# 20. Composite Pattern for Conditions

Conditions can themselves contain other conditions.

For example:

```text
Repository == "FlowForge"
AND
Author == "A"
AND
Label contains "bug"
```

The condition tree becomes:

```text
                  AND
               /   |   \
              /    |    \
     Repository   Author  Label
       ==           ==    contains
   "FlowForge"      "A"    "bug"
```

A more complex example:

```text
                 OR
                /  \
              AND   Condition C
             /  \
        Condition A  Condition B
```

This is a natural use of the **Composite Pattern**.

Both:

```text
SimpleCondition
```

and:

```text
CompositeCondition
```

can satisfy the same `Condition` interface.

Therefore the engine can treat an entire condition tree as a single condition.

---



# 21. Factory Pattern

Workflows will eventually be stored as configuration.

For example, the database may contain:

```text
trigger_type = "github"
action_type = "http"
condition_type = "equals"
```

The system needs to convert those configurations into actual objects.

Instead of putting object creation throughout the application:

```text
if type == github:
    create GitHubTrigger

if type == webhook:
    create WebhookTrigger
```

we use factories.

```text
TriggerFactory
      │
      ├── "github"  → GitHubTrigger
      ├── "webhook" → WebhookTrigger
      └── "manual"  → ManualTrigger
```

Similarly:

```text
ActionFactory
      │
      ├── "http"    → HTTPAction
      ├── "email"   → EmailAction
      └── "github"  → GitHubAction
```

This makes configuration-driven workflows possible.

---



# 22. Complete OOP Relationship

The core architecture becomes:

```text
                         Workflow
                            │
             ┌──────────────┼───────────────┐
             │              │               │
             ▼              ▼               ▼
          Trigger       Condition        Actions
             │              │               │
       ┌─────┼─────┐    ┌───┴───┐      ┌────┼─────┐
       │     │     │    │       │      │    │     │
    Manual Webhook GitHub   Simple Composite HTTP Email GitHub
       │     │     │        │       │      │    │     │
       └─────┴─────┴────────┴───────┴──────┴────┴─────┘
                            │
                            ▼
                     Workflow Engine
                            │
                            ▼
                      Integration Layer
```

---



# 23. Workflow Engine

The `WorkflowEngine` is the central coordinator.

Its responsibility is NOT to implement every trigger or action.

Instead, it coordinates them.

Conceptually:

```text
Event
  ↓
Find applicable workflows
  ↓
Evaluate trigger
  ↓
Evaluate condition
  ↓
Execute actions
  ↓
Record result
```

The engine therefore depends on abstractions.

```text
WorkflowEngine
      │
      ├── Trigger
      ├── Condition
      └── Action[]
```

This is what makes the OOP architecture meaningful.

---



# 24. Complete Execution Flow

```text
                External Event
                     │
                     ▼
              Event Receiver
                     │
                     ▼
              Event Normalizer
                     │
                     ▼
              Internal Event
                     │
                     ▼
             Workflow Engine
                     │
                     ▼
             Trigger Evaluation
                     │
              ┌──────┴──────┐
              │             │
            FALSE          TRUE
              │             │
              ▼             ▼
            STOP       Condition Check
                              │
                       ┌──────┴──────┐
                       │             │
                     FALSE          TRUE
                       │             │
                       ▼             ▼
                     STOP      Execute Actions
                                    │
                          ┌─────────┼─────────┐
                          ▼         ▼         ▼
                       Action    Action    Action
                          │         │         │
                          ▼         ▼         ▼
                    Integration Integration Integration
                          │         │         │
                          └─────────┼─────────┘
                                    ▼
                            Execution Record
```

---



# 25. Event Model

Different external services produce different event formats.

For example, GitHub might provide one JSON structure while another service provides something completely different.

FlowForge therefore converts external events into a common internal representation.

```text
GitHub JSON
     │
     ▼
GitHub Event Parser
     │
     ▼
Internal Event
```

The internal event might conceptually contain:

```text
Event
├── type
├── source
├── timestamp
└── payload
```

The rest of the workflow engine operates on this common structure.

---



# 26. Webhook Flow

A GitHub webhook could follow:

```text
GitHub
   │
   │ HTTP POST
   ▼
/webhooks/github
   │
   ▼
Webhook Handler
   │
   ▼
Verify Event
   │
   ▼
Convert → Internal Event
   │
   ▼
Workflow Engine
```

The webhook endpoint should validate the request before processing it.

In V1, webhook authentication/signature validation will be implemented for integrations where the external provider supports it.

---



# 27. Manual Trigger

Manual execution is particularly useful for:

- Testing workflows
- Demonstrating the application
- Debugging
- Development

Flow:

```text
User clicks "Run"
       ↓
POST /workflows/{id}/run
       ↓
Workflow Engine
       ↓
Evaluate
       ↓
Execute
       ↓
Execution Result
```

This also means the entire OOP engine can be demonstrated without depending on a live external service.

---



# 28. Scheduled Trigger

A schedule trigger can conceptually work as:

```text
Scheduler
    ↓
Find workflows whose schedule is due
    ↓
Create internal event
    ↓
Workflow Engine
```

However, free hosting introduces an important limitation.

The Render free service can spin down after 15 minutes of inactivity, and the next request can require a cold start.

Therefore V1 should NOT claim that scheduled workflows provide production-grade reliability.

### V1 approach

Implement the Schedule abstraction, but treat scheduled execution as:

**Optional / best-effort V1 functionality.**

The primary reliable demonstrations should use:

- Manual triggers
- Webhook triggers

---



# 29. Background Execution

FastAPI provides `BackgroundTasks`, which can execute small tasks after returning an HTTP response. FastAPI itself notes that heavier or multi-process workloads are better handled with larger job systems such as Celery.

For V1:

```text
HTTP Request
     ↓
Workflow Engine
     ↓
Small background action
     ↓
Execution Log
```

We will deliberately NOT introduce:

- Redis
- Celery
- RabbitMQ
- Kafka
- Kubernetes

into the first four-week version.

That would add infrastructure complexity without improving the core OOP demonstration enough to justify it.

---



# 30. Database Design

PostgreSQL will store persistent application data.

Supabase currently provides PostgreSQL and authentication in its free tier, making it suitable for a zero-budget MVP. Its current free plan includes a 500 MB database and limited free-project activity requirements.

## Main Tables

```text
users
workflows
workflow_triggers
workflow_conditions
workflow_actions
integrations
executions
```

Conceptually:

```text
User
 │
 └── Workflows
       │
       ├── Trigger
       │
       ├── Conditions
       │
       ├── Actions
       │
       └── Executions
```

---



# 31. Workflow Persistence

A workflow needs to be stored as configuration rather than as executable Python objects.

For example:

```text
Workflow
│
├── trigger:
│      type = github
│      event = pull_request_merged
│
├── conditions:
│      type = AND
│      children:
│          repository == FlowForge
│          author == John
│
└── actions:
       type = http
       url = ...
```

When a workflow executes:

```text
Database configuration
        ↓
Factories
        ↓
Concrete OOP objects
        ↓
Workflow Engine
        ↓
Execution
```

This is one of the most important architectural flows in the entire project.

---



# 32. Database → OOP Object Flow

```text
PostgreSQL
    │
    │ Workflow Configuration
    ▼
Workflow Repository
    │
    ▼
TriggerFactory
ConditionFactory
ActionFactory
    │
    ▼
Concrete Objects
    │
    ▼
Workflow Object
    │
    ▼
Workflow Engine
```

This allows the application to dynamically construct workflows.

---



# 33. API Design

The frontend communicates with FastAPI through REST APIs.

### Authentication

```text
POST /auth/...
```

Authentication itself will primarily be handled through Supabase Auth.

Supabase Auth supports authentication and authorization and integrates with PostgreSQL Row Level Security.

### Workflows

```text
GET    /api/workflows
POST   /api/workflows
GET    /api/workflows/{id}
PUT    /api/workflows/{id}
DELETE /api/workflows/{id}

POST   /api/workflows/{id}/run
POST   /api/workflows/{id}/enable
POST   /api/workflows/{id}/disable
```



### Executions

```text
GET /api/workflows/{id}/executions
GET /api/executions/{id}
```



### Webhooks

```text
POST /api/webhooks/{provider}
```

---



# 34. Authentication and Authorization

The system must ensure that:

```text
User A
    ↓
can access
    ↓
User A's workflows
```

but cannot access:

```text
User B's workflows
```

Authorization must therefore be enforced on the backend.

The basic rule is:

```text
Authenticated User
       ↓
Get user_id
       ↓
Query workflow
       ↓
Verify workflow.user_id == authenticated user
       ↓
Allow operation
```

Database-level Row Level Security can provide an additional protection layer when using Supabase.

---



# 35. Integration Architecture

The architecture should avoid tightly coupling actions to APIs.

```text
             Action
               │
               ▼
          Integration
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
    GitHub   Email     HTTP
     API      API      API
```

For example:

```text
GitHubAction
      ↓
GitHubIntegration
      ↓
GitHub REST API
```

This makes the system easier to extend.

---



# 36. Generic HTTP Integration

The generic HTTP action is especially important.

Instead of implementing:

```text
SlackAction
DiscordAction
NotionAction
TrelloAction
JiraAction
```

immediately, FlowForge can provide:

```text
HTTPAction
```

with configurable:

```text
URL
HTTP Method
Headers
Body
```

Therefore:

```text
FlowForge
    ↓
HTTPAction
    ↓
External API
```

can communicate with many services.

This significantly increases the practical scope of V1 without requiring dozens of custom integrations.

---



# 37. Execution Logging

Every workflow execution should create an execution record.

Conceptually:

```text
Execution
├── workflow_id
├── started_at
├── completed_at
├── status
├── trigger_data
├── result
└── error
```

Possible statuses:

```text
PENDING
RUNNING
SUCCESS
FAILED
```

This gives users visibility into what happened.

---



# 38. Error Handling

Example:

```text
Workflow
   ↓
Action 1 → SUCCESS
   ↓
Action 2 → FAILED
   ↓
Execution marked FAILED
```

The UI should show:

```text
Workflow: GitHub Notification

Status: FAILED

Action:
HTTP Request

Error:
External API returned 401

Time:
...
```

V1 will implement basic error recording and limited retry behavior.

Advanced retry queues will remain outside V1.

---



# 39. Security Considerations

FlowForge handles external integrations, therefore credentials must be treated carefully.

### Never:

```text
API keys inside frontend code
API keys committed to Git
credentials stored in plain text logs
```



### Environment variables

Backend secrets should be stored through deployment environment variables.

Example:

```text
DATABASE_URL
SUPABASE_URL
SUPABASE_SERVICE_KEY
GITHUB_CLIENT_SECRET
```

Actual values must never be committed.

---



# 40. HTTP Action Security

The generic HTTP action creates an important security concern.

If users can send requests to arbitrary URLs, the backend can potentially be abused.

Therefore V1 should impose restrictions such as:

- Validate URLs
- Restrict unsupported protocols
- Do not allow access to internal/private network addresses
- Apply request timeouts
- Limit payload size
- Avoid exposing server credentials to user-controlled requests

This is an area where FlowForge's V1 implementation should remain conservative.

---



# 41. Testing Strategy

The most important tests will focus on the OOP engine.

## Unit Tests

Test:

```text
Trigger
Condition
Action
Factory
Workflow Engine
```

Examples:

```text
GitHubTrigger matches correct event
GitHubTrigger rejects incorrect event

EqualsCondition returns true for equal values
EqualsCondition returns false otherwise

AndCondition requires all children to pass
OrCondition requires at least one child to pass

HTTPAction executes valid request

Factory creates correct concrete class
```

---



# 42. Workflow Engine Test

A complete test could construct:

```text
GitHubTrigger
       +
RepositoryCondition
       +
HTTPAction
```

Then:

```text
Event
 ↓
Trigger = TRUE
 ↓
Condition = TRUE
 ↓
Action executed
```

This proves the entire OOP pipeline independently of the frontend.

---



# 43. Testing Philosophy

Do not aim for an arbitrary percentage simply because it sounds professional.

Instead, prioritize testing the architecture.

### Highest priority

```text
Workflow Engine
Trigger evaluation
Condition evaluation
Action execution
Factories
Authentication boundaries
Workflow CRUD
Webhook handling
```



### Lower priority

```text
Visual styling
Animations
Minor UI components
```

---



# 44. AI-Assisted Development Strategy

AI will be used as a development assistant, not as the person who designs the architecture blindly.

The recommended loop is:

```text
Understand
    ↓
Design
    ↓
Ask AI for implementation
    ↓
Read implementation
    ↓
Run tests
    ↓
Debug
    ↓
Refactor
```

The user should particularly understand:

- Why each abstraction exists
- Why inheritance is used
- Where polymorphism occurs
- How factories create objects
- How workflows become runtime objects
- How the engine executes them

This is essential for the college project.

---



# 45. AI Tool Strategy

The user already works with VS Code/GitHub tooling and can use an AI coding assistant.

Recommended pattern:


| Task                | Approach                        |
| ------------------- | ------------------------------- |
| Architecture        | ChatGPT                         |
| Understanding OOP   | ChatGPT                         |
| Code implementation | AI coding assistant             |
| Debugging           | AI + manual debugging           |
| Tests               | AI-generated, manually reviewed |
| Documentation       | ChatGPT                         |
| Final explanation   | User understands and verifies   |


The important rule:

> **Do not ask the coding agent to build the entire project in one prompt.**

Instead:

```text
Task 1 → Database
Task 2 → Workflow model
Task 3 → Trigger abstraction
Task 4 → Condition abstraction
Task 5 → Action abstraction
Task 6 → Engine
...
```

---



# 46. Development Workflow

Use GitHub Flow.

```text
main
 │
 ├── feature/workflow-model
 ├── feature/trigger-system
 ├── feature/condition-system
 ├── feature/action-system
 └── feature/frontend-builder
```

Each feature should be:

```text
Implement
   ↓
Test
   ↓
Commit
   ↓
Merge
```

Suggested commit style:

```text
feat: add workflow model
feat: implement trigger abstraction
feat: add webhook trigger
feat: implement condition evaluator
feat: add workflow execution engine
test: add workflow engine tests
fix: validate webhook payload
```

---



# 47. Four-Week Development Plan

The four-week limit is the most important scope constraint.

## Week 1 — Foundation + OOP Core



### Backend

- FastAPI setup
- Project structure
- PostgreSQL connection
- SQLAlchemy models
- Basic authentication integration
- Workflow model
- Trigger abstraction
- Condition abstraction
- Action abstraction



### OOP target

By the end of Week 1:

```text
Trigger
Condition
Action
Workflow
```

should exist and be testable.

---



## Week 2 — Workflow Engine

Implement:

- Concrete triggers
- Concrete conditions
- Composite conditions
- Concrete actions
- Factories
- Workflow Engine
- Execution records
- Manual workflow execution

Target:

```text
Create workflow
      ↓
Save workflow
      ↓
Load workflow
      ↓
Construct OOP objects
      ↓
Execute workflow
      ↓
Record execution
```

At the end of Week 2, the **backend should already be a functioning automation engine**, even without a polished frontend.

---



# 48. Week 3 — Frontend + Integrations

Implement:

### Frontend

- Login
- Dashboard
- Workflow list
- Create workflow
- Edit workflow
- Workflow details
- Execution history



### Integrations

Prioritize:

```text
Generic HTTP
GitHub
```

Add email/notification integration if the core system is stable.

### Webhook

Implement:

```text
GitHub
 ↓
Webhook
 ↓
FlowForge
 ↓
Workflow Engine
```

---



# 49. Week 4 — Deployment + Testing + Polish



### Testing

- Unit tests
- API tests
- Workflow execution tests
- Authentication tests
- Webhook tests



### Security

- Validate inputs
- Protect secrets
- Validate ownership
- Restrict HTTP actions
- Add request timeouts



### Deployment

```text
React → Vercel
FastAPI → Render
Database/Auth → Supabase
```

Vercel supports deployment of Vite/React applications, while Render supports FastAPI web services.

### Final work

- Fix bugs
- Improve UI
- Write README
- Create architecture diagrams
- Record demonstration
- Prepare college presentation

---



# 50. Deployment Architecture

```text
                    Internet
                       │
             ┌─────────┴──────────┐
             │                    │
             ▼                    ▼
       Vercel Frontend       Render Backend
          React                 FastAPI
             │                    │
             │ REST API           │
             └──────────┬─────────┘
                        │
                        ▼
                   Supabase
                 PostgreSQL
                 + Auth
                        │
                        ▼
                External Services
             ┌──────────┼───────────┐
             ▼          ▼           ▼
           GitHub      HTTP        Email
```

Render currently offers free web services, but its free services spin down after 15 minutes without inbound traffic and can take time to wake. Render explicitly describes the free tier as suitable for testing/hobby projects rather than production workloads.

Therefore the deployment is appropriate for the **V1 college project/public demo**, but should not be described as production-grade infrastructure.

---



# 51. Cost Plan

The development target is:

> **₹0 / $0**



### Intended services


| Service         | Purpose           | V1 Target                            |
| --------------- | ----------------- | ------------------------------------ |
| GitHub          | Code              | Free                                 |
| Vercel          | Frontend          | Free tier                            |
| Render          | Backend           | Free tier                            |
| Supabase        | PostgreSQL + Auth | Free tier                            |
| AI coding tools | Development       | Existing/free access where available |


Supabase currently lists a free tier with $0/month pricing, 500 MB database capacity, and other usage limits.

Render's free tier has significant limitations, particularly service sleeping and ephemeral local storage, so persistent application data must remain in PostgreSQL rather than local files.

### Important

The project should not depend on:

- Paid APIs
- Paid servers
- Paid databases
- Paid queues
- Paid AI APIs

for V1.

External integrations should preferably use services/APIs that can be tested without mandatory paid usage.

---



# 52. V1 vs V2

The scope boundary is extremely important.

## V1

```text
Workflow CRUD
       +
Trigger system
       +
Condition system
       +
Action system
       +
OOP engine
       +
Factories
       +
Composite conditions
       +
HTTP integration
       +
GitHub integration
       +
Webhook support
       +
Execution history
       +
Authentication
       +
Deployment
```



## V2

AI-generated workflows will be intentionally postponed.

Potential V2:

```text
User:
"When a GitHub PR is merged,
notify me on Discord and create
a task if it contains the word bug."

                ↓

          AI Workflow Builder

                ↓

      Trigger + Conditions + Actions
```

Other V2 possibilities:

- More integrations
- Visual workflow builder
- Drag-and-drop editor
- AI workflow generation
- Natural-language workflow editing
- Retry queues
- Background workers
- Advanced scheduling
- Workflow templates
- Team collaboration
- Analytics
- Advanced permissions
- OAuth-based integrations

The V1 architecture should make these extensions possible without requiring a complete rewrite.

---



# 53. Definition of Technical Success

FlowForge V1 will be considered technically successful when the following pipeline works:

```text
User
 ↓
Creates Workflow
 ↓
Workflow saved in PostgreSQL
 ↓
Workflow configuration loaded
 ↓
Factories create OOP objects
 ↓
Trigger evaluates event
 ↓
Condition tree evaluates context
 ↓
Action executes
 ↓
Integration communicates with external service
 ↓
Execution result is stored
 ↓
User sees execution history
```

More importantly, the following statement should be demonstrably true:

> **A new Trigger, Condition, or Action can be added by creating a new implementation of the relevant abstraction without rewriting the Workflow Engine.**

That is the central technical achievement of FlowForge.

---



# Recommended V1 Architecture in One Diagram

```text
                         ┌───────────────────┐
                         │    FLOWFORGE      │
                         └─────────┬─────────┘
                                   │
                         ┌─────────▼─────────┐
                         │   React Frontend  │
                         └─────────┬─────────┘
                                   │
                              REST API
                                   │
                         ┌─────────▼─────────┐
                         │    FastAPI API    │
                         └─────────┬─────────┘
                                   │
                         ┌─────────▼─────────┐
                         │ Workflow Service  │
                         └─────────┬─────────┘
                                   │
                         ┌─────────▼─────────┐
                         │ Workflow Engine   │
                         └─────────┬─────────┘
                                   │
              ┌────────────────────┼───────────────────┐
              │                    │                   │
              ▼                    ▼                   ▼
         ┌─────────┐          ┌──────────┐        ┌─────────┐
         │ Trigger │          │Condition │        │ Action  │
         └────┬────┘          └────┬─────┘        └────┬────┘
              │                    │                   │
       ┌──────┼──────┐       ┌─────┴─────┐      ┌─────┼─────┐
       ▼      ▼      ▼       ▼           ▼      ▼     ▼     ▼
    Manual Webhook GitHub  Simple     Composite HTTP Email GitHub
                              │           │
                              └───────────┘
                                   │
                                   ▼
                           Integration Layer
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
                  GitHub          HTTP          Email
                    │              │              │
                    └──────────────┼──────────────┘
                                   ▼
                              PostgreSQL
                              + Auth
```

---



# Final Architectural Principle

The most important thing to remember while implementing FlowForge is:

```text
                 DON'T BUILD:

      GitHub → Email → Some Automation

                 BUILD:

           ┌─────────────────┐
           │ Workflow Engine │
           └────────┬────────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     Trigger    Condition     Action
        │           │           │
        └───────────┼───────────┘
                    │
              Integration
                    │
              External APIs
```

GitHub, email, Discord, Slack, etc. are merely implementations around this engine.

This makes **OOP the core architecture of the product**, while still giving FlowForge a legitimate real-world use case.

---



# Handoff Context



- Stage: techdesign
- App name: FlowForge
- User level: C  (A = vibe coder, B = developer, C = in-between)
- Target platform: Web
- Budget: ₹0 / $0 development budget
- Timeline: 4 weeks
- Chosen stack: React + TypeScript + Vite + Tailwind / Python + FastAPI + SQLAlchemy / PostgreSQL + Supabase Auth / Vercel + Render
- AI coding tool: AI-assisted development; exact primary coding agent to be finalized
- Source files: research-FlowForge.md → PRD-FlowForge-MVP.md → TechDesign-FlowForge-MVP.md

---



## Machine-Readable Summary

```json
{
  "schemaVersion": 1,
  "documentType": "techdesign",
  "appName": "FlowForge",
  "stack": {
    "frontend": "React + TypeScript + Vite",
    "backend": "Python + FastAPI",
    "database": "PostgreSQL + SQLAlchemy",
    "auth": "Supabase Auth",
    "styling": "Tailwind CSS",
    "deployment": "Vercel + Render"
  },
  "commands": {
    "setup": "npm create vite@latest frontend -- --template react-ts && python -m venv .venv",
    "dev": "npm run dev",
    "test": "pytest",
    "typecheck": "tsc --noEmit",
    "lint": "npm run lint",
    "build": "npm run build"
  },
  "aiScope": "automation"
}
```

---



## Technical Design Status


| Required Section                     | Present? |
| ------------------------------------ | -------- |
| Platform/approach clearly chosen     | Yes      |
| Alternatives compared with pros/cons | Yes      |
| Tech stack fully specified           | Yes      |
| Trade-offs honestly acknowledged     | Yes      |
| Cost breakdown included              | Yes      |
| Timeline realistic                   | Yes      |
| AI assistance strategy defined       | Yes      |
| OOP architecture defined in detail   | Yes      |
| Deployment architecture defined      | Yes      |
| V1/V2 boundary defined               | Yes      |


---



## Critical Review



### 1. Does the stack match the budget?

**Yes, for an MVP/demo.**

The intended deployment uses free tiers. However, the free infrastructure has limitations, especially backend cold starts and service inactivity.

### 2. Does the timeline match the complexity?

**Yes, if the scope remains V1.**

The dangerous mistake would be trying to implement:

```text
20 integrations
+
visual drag-and-drop builder
+
AI workflow generation
+
distributed workers
+
OAuth for every service
```

in four weeks.

The four-week version should instead focus on:

```text
Excellent OOP engine
+
2-3 useful integrations
+
simple workflow builder
+
execution history
+
real deployment
```



### 3. What is the biggest technical risk?

Not React.

Not PostgreSQL.

Not FastAPI.

The biggest risk is **overbuilding the automation infrastructure**.

Therefore:

> **Build the OOP engine first. Build the product around it second.**

That order protects the project's primary academic objective while still producing a deployable product.

---

*Technical Design for: FlowForge*  
*Approach: Full-code, AI-assisted development*  
*Version: MVP V1*  
*Estimated Development Time: 4 weeks*  
*Development Budget: ₹0 / $0*