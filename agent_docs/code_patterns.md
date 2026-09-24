# Code Patterns

Level C: copy these patterns instead of inventing new architecture. Inspect existing code once it exists.

## Architecture

- Layered backend: `api` (HTTP) / `services` (orchestration) / `core` (engine) / `repositories` (DB) / `models` / `schemas`
- Routes handle request/response only. No engine or SQLAlchemy sessions inside route functions beyond calling a service.
- New trigger/condition/action: implement the abstraction, register the factory, leave WorkflowEngine unchanged.

Why polymorphism (do not write this in the engine):

```python
# Good — engine stays closed for modification
for action in workflow.actions:
    action.execute(context)

# Bad — adding Slack would require editing the engine
if action_type == "email":
    send_email(...)
```

Why factories exist:

```python
# Stored config is data. Runtime needs objects.
action = ActionFactory.create(row.type, row.config)
```

## Engineering constraints

- TypeScript: do not use `any`; use `unknown` plus narrowing. Type parameters and returns.
- Python: type hints on public methods; Pydantic models at API/config boundaries (not Zod — this is not a TS-backend app).
- Check `package.json` / `requirements.txt` before adding dependencies. Prefer stdlib and existing stack (httpx/fetch, not a new HTTP client unless needed).
- Native APIs over extra libraries.
- State issues briefly and fix them; one clarifying question if a decision is missing.

## Data and state

- Frontend: REST via `services/api.ts`; local React state until sharing across routes requires more
- Server: Postgres configuration rows → factories → OOP objects → engine
- Validate URLs, ownership, and payloads on the server

## Errors

- Do not swallow action failures. Mark the execution FAILED and store a user-safe error.
- Never write secrets into execution logs.

## Naming

- Python files `snake_case.py`; React components `PascalCase.tsx`
- Classes PascalCase (`WorkflowEngine`, `HttpAction`)
- Python functions snake_case; TypeScript camelCase
- Env vars UPPER_SNAKE_CASE
