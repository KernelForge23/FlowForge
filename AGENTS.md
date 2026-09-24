# AGENTS.md — FlowForge

> Write only what an agent could not work out by reading the repo. Skip the
> directory tree, the dependency list, and generic advice.

## Project

- **What this is:** A modular workflow automation platform built around triggers, conditions, actions, and integrations.
- **Who it is for:** Developers and technically comfortable users
- **User level:** C (learning while building; explain architecture, still plan small steps)
- **Current phase:** Foundation — agent config complete; application source not started
- **Timeline / budget:** 4 weeks, ₹0 / $0 (free-tier hosting only)
- **UI vibe:** Clean, technical, minimal, professional

## How I Should Think

1. **Understand intent first:** identify what the user actually needs before answering.
2. **Ask if unsure:** if a critical choice is missing, ask one specific question before proceeding.
3. **Plan before coding:** propose a short plan, wait for approval, then implement one slice.
4. **Verify after changes:** run the commands in `agent_docs/testing.md` or a browser check; fix before the next slice.
5. **Explain trade-offs:** when recommending a path, name the alternative you did not take.

## Plan → Execute → Verify

- **Plan:** outline the approach and wait for approval. Use Plan mode when the tool has it.
- **Execute:** one feature at a time. Do not start Week 2 work during Week 1.
- **Verify:** `pytest`, `tsc --noEmit`, `npm run lint`, `npm run build`, and browser checks as listed in `agent_docs/testing.md`.

## Commands

Split app. After scaffolding, run frontend commands from `frontend/` and backend commands from `backend/` with the venv active.

- Setup: `npm create vite@latest frontend -- --template react-ts && python -m venv .venv`
- Frontend dev: `npm run dev`
- Backend dev: `uvicorn app.main:app --reload`
- Tests: `pytest`
- Typecheck: `tsc --noEmit`
- Lint / build: `npm run lint` / `npm run build`

Product documents: `docs/PRD-FlowForge-MVP.md`, `docs/TechDesign-FlowForge-MVP.md`, `docs/Research-FlowForge.md`. Paths are in `vibe.project.json`.

## Read first

1. `docs/PRD-FlowForge-MVP.md`
2. `docs/TechDesign-FlowForge-MVP.md`
3. `agent_docs/project_brief.md`
4. `agent_docs/tech_stack.md`
5. `agent_docs/testing.md`
6. `MEMORY.md` for current phase and blockers

Load `agent_docs/code_patterns.md` and `agent_docs/product_requirements.md` when implementing.

## Gotchas

- The workflow engine belongs on the backend. The browser configures workflows; it never executes actions.
- Engine code depends on Trigger, Condition, Action, and Integration abstractions. Do not type-switch on concrete integrations inside the engine.
- Persist workflows as configuration, then hydrate runtime objects through factories. Do not pickle Python objects as the source of truth.
- Generic HTTP actions can SSRF the backend: validate URLs, allow only http/https, block private/loopback/link-local addresses, set timeouts, and limit payload size.
- Never log integration credentials, tokens, or secrets into execution history or the frontend.
- Render free tier spins down after inactivity. Scheduled triggers are optional/best-effort in V1. Demonstrate with manual + webhook first.
- Do not add Redis, Celery, Kafka, or similar queues in V1. FastAPI background tasks are enough.
- Persistent data stays in PostgreSQL (Supabase). Render local disk is ephemeral.
- V1 has no in-product AI. Do not add model calls, AI workflow generation, or paid AI APIs.
- Academic constraint: OOP is the core of the engine, not a decorative class layer around scripts.

## What NOT To Do

- Do not delete files without explicit confirmation.
- Do not modify database schemas without a rollback/backup plan.
- Do not add features that are not in the current phase or that the PRD lists as V2.
- Do not skip tests for "simple" changes.
- Do not bypass failing tests or pre-commit hooks.
- Do not use deprecated libraries or invent extra package-manager scripts.

## Protected areas — ask before changing

- `.env*`, secrets, credentials, private logs
- `.github/workflows/`, deployment, infrastructure
- existing database migrations
- auth, payments, billing, production email/send flows
- AI provider credentials, MCP servers, tool permissions

**Never print, commit, or transmit secrets, tokens, private logs, or production
data.** Never delete files, rewrite large areas, or change
infrastructure/auth/billing/migrations without approval.

## Done means

Report: files changed · commands run · test/build/device results · remaining risks · rollback notes if relevant.

---

**When this file gets long, that is the signal to split it.** Move task-specific
procedures into `.claude/skills/<name>/SKILL.md` or `.agents/skills/<name>/SKILL.md`.
Move directory-specific conventions into `<subdir>/CLAUDE.md`. Keep universal
constraints and safety prohibitions here.
