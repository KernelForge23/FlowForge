# Project Brief

Level C: these notes are the "what and why." Architecture details live in `tech_stack.md` and `code_patterns.md`.

## Product

- One-line vision: A modular workflow automation platform built around triggers, conditions, actions, and integrations.
- Target users: Developers and technically comfortable users
- Primary user story: A developer wants an email sent whenever a specific GitHub event occurs. They open FlowForge, create a workflow, pick a trigger, add conditions, configure an action and integration, save and activate. When the event arrives, the engine evaluates trigger and conditions, runs the action, and records history.
- Primary user outcome: Sign in → create workflow → trigger → execute → view the result on the deployed app.

## Scope

- Must ship: Workflow Builder; Triggers; Conditions; Actions and Integrations; Execution Engine and History (plus auth and deployment)
- Nice to have: Database integration; schedule trigger if time remains
- Not in v1: AI-generated workflows; visual drag-and-drop editor; large integration marketplace; advanced branching and loops; Slack/Discord/Teams; team RBAC; distributed workers

## Principles

- Solve the user story before adding polish.
- Prefer boring, maintainable choices.
- Keep generated docs short and current.
- Verify user-visible work in the real product surface.
- Build the OOP engine first; wrap the product around it second.
- Four-week priority if time is short: OOP architecture → engine → working integrations → history → UI polish → extra features.

## AI Position

V1 has no in-product AI. AI is a development assistant only. Natural-language workflow generation is V2.
