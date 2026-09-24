# Tech Stack

Last verified: 2026-09-23 from `docs/TechDesign-FlowForge-MVP.md`

Level C: this is the agreed stack. Do not swap it without asking.

## Stack

| Area | Choice | Why |
|------|--------|-----|
| Frontend | React + TypeScript + Vite | Builder/dashboard only; engine stays on the backend |
| Styling | Tailwind CSS | Clean/technical UI without a design-system project |
| Backend | Python + FastAPI | OOP engine is easy to test without the UI |
| Validation | Pydantic | Request/config validation at the API boundary |
| ORM | SQLAlchemy | Maps tables to models; engine still uses factories |
| Database | PostgreSQL via Supabase | Persistent data; Render disk is ephemeral |
| Auth | Supabase Auth | Sessions on the client; backend still checks ownership |
| Frontend host | Vercel | Vite/React free tier |
| Backend host | Render | FastAPI free web service; cold starts after idle |
| Tests | pytest | Engine and API tests |

Rejected for V1: Next.js full-stack (hides the OOP engine), Django (too much framework), Redis/Celery/Kafka.

## Commands

- Setup: `npm create vite@latest frontend -- --template react-ts && python -m venv .venv`
- Dev: `npm run dev` from `frontend/`; `uvicorn app.main:app --reload` from `backend/`
- Test: `pytest`
- Typecheck: `tsc --noEmit`
- Lint: `npm run lint`
- Build: `npm run build`
- Browser check: http://localhost:5173 — login → dashboard → create workflow → run → history; also a narrow viewport

## Target layout (from Tech Design)

```text
frontend/src/{components,pages,services,types}
backend/app/{api,core,models,repositories,services,schemas,main.py}
backend/tests/
```

`core/` is the OOP engine. `api/` is HTTP only.

## Intended tables

users, workflows, workflow_triggers, workflow_conditions, workflow_actions, integrations, executions

## API surface (V1)

- Workflows: GET/POST `/api/workflows`, GET/PUT/DELETE `/api/workflows/{id}`, POST run/enable/disable
- Executions: GET `/api/workflows/{id}/executions`, GET `/api/executions/{id}`
- Webhooks: POST `/api/webhooks/{provider}`
- Auth primarily via Supabase Auth

## Deployment

Internet → Vercel (React) and Render (FastAPI) → Supabase (Postgres + Auth) → GitHub/HTTP/email.

Cost ceiling: ₹0 / $0. Do not add paid services.

## AI Runtime

None in the product. No model provider, MCP product tools, or eval suite for in-app AI. Development assistants (Cursor, Claude, Codex, Gemini) are not part of the runtime.
