# Memory

Update this after major decisions, completed phases, or bugs that future agents need to know about. Keep it short. This file travels with the repo; tool-side memories do not.

## Current State

- Current task: Phase 2 complete — backend workflow engine and manual execution path
- Current phase: Workflow Engine (Week 2 done)
- Next step: Week 3 — frontend workflow surfaces plus SSRF-safe HTTP/GitHub integrations
- Blocked by: none

## Decisions

- 2026-09-23 FlowForge: Trigger → Condition → Action, 4-week ₹0 MVP, user level C
- 2026-09-23 Stack: React+Vite+Tailwind, FastAPI+SQLAlchemy, Supabase Postgres/Auth, Vercel+Render
- 2026-09-23 No in-product AI; HTTP action is the extensibility valve; schedule is best-effort
- 2026-09-23 Product docs live under `docs/` (research, PRD, Tech Design)
- 2026-09-23 AI coding tools: Claude Code, Cursor, Codex, Gemini/Antigravity legacy
- 2026-10-03 Phase 1 uses SQLite locally (`DATABASE_URL`); SQLAlchemy models stay Postgres-ready. Auth and live Supabase deferred.
- 2026-10-06 Phase 2 hydrates persisted workflow configuration through factories, evaluates trigger/condition objects in `WorkflowEngine`, and records manual executions. Week 2 actions are deterministic `NoOpAction`; network integrations are deferred to Week 3.

## AI / Tooling Decisions

- 2026-09-23 No product model provider, retention setting, or AI eval suite in V1

## Known Issues

- Render free-tier cold starts make reliable cron unrealistic in V1
- Generic HTTP actions need SSRF protections from day one
- SQLite JSON + string UUIDs; switch `DATABASE_URL` to Postgres before production

## Completed

- [x] Research, PRD, Tech Design
- [x] Agent instruction files (Part 4)
- [x] Core data model (SQLAlchemy + SQLite `create_all`)
- [x] Trigger / Condition / Action ABCs + Workflow composition (pytest)
- [x] Concrete trigger/condition/composite/action factories
- [x] WorkflowEngine and execution records
- [x] Workflow create/load/manual-run API path
- [ ] Auth
- [ ] Core MVP flow
- [ ] Launch checks
