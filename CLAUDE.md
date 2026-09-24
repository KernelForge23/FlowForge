# CLAUDE.md — Claude Code Configuration for FlowForge

## Project Context

**App:** FlowForge  
**Stack:** React + TypeScript + Vite + Tailwind / Python + FastAPI + SQLAlchemy / PostgreSQL + Supabase Auth / Vercel + Render  
**Stage:** MVP Development  
**User Level:** C (in-between)

## Directives

1. **Master plan:** Always read `AGENTS.md` first.
2. **Documentation:** Use `agent_docs/` for stack, patterns, and tests. Product source: `docs/PRD-FlowForge-MVP.md` and `docs/TechDesign-FlowForge-MVP.md`.
3. **Plan-first:** Propose a brief plan and wait for approval before coding.
4. **Incremental build:** One small feature at a time. Test frequently.
5. **Pre-commit:** If hooks exist, run them; fix failures. Do not bypass.
6. **Verification:** Exact commands in `agent_docs/testing.md`.
7. **Communication:** Be concise. One clarifying question when needed.
8. **Subagents:** Use `.claude/agents/` for research, review, and tests. Do not spawn a team unless work is disjoint.
9. **Privacy:** Do not read or print secrets without explicit permission.

## What NOT To Do

- Do not delete files without confirmation
- Do not change schemas without a rollback plan
- Do not add V2 features during V1
- Do not skip tests or bypass hooks
- Do not auto-approve MCP, shell/network, production, billing, or destructive tools

## Commands

- Setup: `npm create vite@latest frontend -- --template react-ts && python -m venv .venv`
- Dev: `npm run dev` (frontend); `uvicorn app.main:app --reload` (backend)
- Test: `pytest`
- Lint/typecheck/build: `npm run lint`, `tsc --noEmit`, `npm run build`

Task procedures belong in `.claude/skills/`. Directory conventions belong in `<subdir>/CLAUDE.md`.
