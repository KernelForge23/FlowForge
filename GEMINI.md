# GEMINI.md — Antigravity / Gemini Legacy Configuration for FlowForge

Last generated: 2026-09-23. Verify current Google agent CLI/IDE support before relying on Gemini CLI directly.

## Project Context

**App:** FlowForge  
**Stack:** React + TypeScript + Vite + Tailwind / Python + FastAPI + SQLAlchemy / PostgreSQL + Supabase Auth / Vercel + Render  
**Stage:** MVP Development  
**User Level:** C (in-between)

## Directives

1. **Master plan:** Always read `AGENTS.md` first.
2. **Documentation:** Refer to `agent_docs/` and `docs/`.
3. **Plan-first:** Propose a brief plan and wait for approval before coding.
4. **Incremental build:** One small feature at a time. Test frequently.
5. **Pre-commit:** If hooks exist, run them; fix failures.
6. **Verification:** Commands in `agent_docs/testing.md` only.
7. **Communication:** Be concise. Ask when needed.
8. **Google-agent checks:** Use `/memory show`, `/memory refresh`, `/tools`, `/chat save <tag>`, and `/compress` where the current tool supports them.
9. **Tool approvals:** Keep `.gemini/settings.json` conservative. Do not enable always-allow/YOLO modes.

## Commands

- Setup: `npm create vite@latest frontend -- --template react-ts && python -m venv .venv`
- Dev: `npm run dev`
- Test: `pytest`
- Lint/typecheck/build: `npm run lint`, `tsc --noEmit`, `npm run build`
