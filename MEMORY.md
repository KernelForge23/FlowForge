# Memory

Update this after major decisions, completed phases, or bugs that future agents need to know about. Keep it short. This file travels with the repo; tool-side memories do not.

## Current State

- Current task: Final MVP verification and deployment
- Current phase: Week 4 refinement complete; deployment smoke test pending
- Next step: Configure production Supabase/Postgres, Render, and Vercel values and run the deployed smoke test
- Blocked by: deployment access and production environment values are user-supplied; Render/Vercel/Supabase dashboard steps remain

## Decisions

- 2026-09-23 FlowForge: Trigger → Condition → Action, 4-week ₹0 MVP, user level C
- 2026-09-23 Stack: React+Vite+Tailwind, FastAPI+SQLAlchemy, Supabase Postgres/Auth, Vercel+Render
- 2026-09-23 No in-product AI; HTTP action is the extensibility valve; schedule is best-effort
- 2026-09-23 Product docs live under `docs/` (research, PRD, Tech Design)
- 2026-09-23 AI coding tools: Claude Code, Cursor, Codex, Gemini/Antigravity legacy
- 2026-10-03 Phase 1 uses SQLite locally (`DATABASE_URL`); SQLAlchemy models stay Postgres-ready. Auth and live Supabase deferred.
- 2026-10-06 Phase 2 hydrates persisted workflow configuration through factories, evaluates trigger/condition objects in `WorkflowEngine`, and records manual executions. Week 2 actions are deterministic `NoOpAction`; network integrations are deferred to Week 3.
- 2026-10-06 Week 3 adds SSRF-guarded HTTP actions, GitHub dispatch actions, GitHub webhook dispatch, CORS for local frontend development, and a React workflow dashboard with Supabase client login wiring. Backend ownership checks activate when Supabase is configured; local tests retain auth-disabled SQLite mode.
- 2026-10-06 Final slice adds workflow CRUD/configuration APIs, frontend trigger/condition/action builder, deletion, disabled-workflow protection, signed GitHub webhooks, bounded HTTP retries, and deployment instructions.
- 2026-10-06 Email action adds Resend delivery through a backend-only API key, validated recipients/content, safe provider metadata, bounded retries, and dedicated frontend fields.
- 2026-10-06 Approved and implemented personal Gmail OAuth integration using encrypted per-user tokens, Gmail send scope, connection/disconnect UI, and ownership-aware email execution.

## AI / Tooling Decisions

- 2026-09-23 No product model provider, retention setting, or AI eval suite in V1

## Known Issues

- Render free-tier cold starts make reliable cron unrealistic in V1
- Generic HTTP actions need SSRF protections from day one
- SQLite JSON + string UUIDs; switch `DATABASE_URL` to Postgres before production
- 2026-10-06 Debug: authenticated workflow creation failed because frontend API calls omitted the Supabase bearer token; fixed token propagation and local User synchronization.
- 2026-10-07 Production login debug: `https://flow-forge-ruddy.vercel.app/` calls the `hivvbrbucixasoorbbsd` Supabase project, while local `frontend/.env` uses `bdhhvmwxbinibiksjhnc`; production `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` are mismatched or point to the wrong project. Correct the Vercel Production pair and redeploy.
- 2026-10-07 Production project decision: use the `flowforge-production` Supabase project at `hivvbrbucixasoorbbsd.supabase.co` for production. Vercel must use this project's matching anonymous/publishable key, then redeploy and repeat the browser sign-in check.
- 2026-10-07 Gmail production debug: Render health is 200, but an OPTIONS preflight from `https://flow-forge-ruddy.vercel.app` to `/api/integrations/gmail/connect` returns `400 Disallowed CORS origin`; set Render `FRONTEND_ORIGIN` to the exact Vercel origin and redeploy. After CORS is fixed, verify Google OAuth variables and redirect URI.

## Completed

- [x] Research, PRD, Tech Design
- [x] Agent instruction files (Part 4)
- [x] Core data model (SQLAlchemy + SQLite `create_all`)
- [x] Trigger / Condition / Action ABCs + Workflow composition (pytest)
- [x] Concrete trigger/condition/composite/action factories
- [x] WorkflowEngine and execution records
- [x] Workflow create/load/manual-run API path
- [x] Auth
- [x] Core MVP flow
- [ ] Launch checks
- [x] Added psycopg PostgreSQL driver and updated deployment runbook for Supabase production
