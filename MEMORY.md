# Memory

Update this after major decisions, completed phases, or bugs that future agents need to know about. Keep it short. This file travels with the repo; tool-side memories do not.

## Current State

- Current task: Part 4 agent configuration for Cursor, Claude Code, Codex, and Gemini
- Current phase: Foundation
- Next step: After user approval, Week 1 slice — FastAPI layout, Postgres models, Trigger/Condition/Action abstractions
- Blocked by: none

## Decisions

- 2026-09-23 FlowForge: Trigger → Condition → Action, 4-week ₹0 MVP, user level C
- 2026-09-23 Stack: React+Vite+Tailwind, FastAPI+SQLAlchemy, Supabase Postgres/Auth, Vercel+Render
- 2026-09-23 No in-product AI; HTTP action is the extensibility valve; schedule is best-effort
- 2026-09-23 Product docs live under `docs/` (research, PRD, Tech Design)
- 2026-09-23 AI coding tools: Claude Code, Cursor, Codex, Gemini/Antigravity legacy

## AI / Tooling Decisions

- 2026-09-23 No product model provider, retention setting, or AI eval suite in V1

## Known Issues

- Render free-tier cold starts make reliable cron unrealistic in V1
- Generic HTTP actions need SSRF protections from day one

## Completed

- [x] Research, PRD, Tech Design
- [x] Agent instruction files (Part 4)
- [ ] Core data model
- [ ] Auth
- [ ] Core MVP flow
- [ ] Launch checks
