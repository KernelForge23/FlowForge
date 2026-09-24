# Product Requirements

Short build-facing summary of `docs/PRD-FlowForge-MVP.md`.

## Users

- Primary user: Developers and technically comfortable users
- Main problem: They repeatedly perform actions across GitHub, email, APIs, and databases using scripts or manual steps instead of a reusable WHEN → IF → THEN workflow.

## Must-Have Features

- Workflow Builder — create, select trigger, add conditions, add one or more actions, configure parameters, save/activate, edit, delete
- Trigger System — Manual, Webhook, Scheduled (best-effort); new types without changing the engine
- Condition System — equality, not equal, greater than, less than, contains, AND, OR; stop when conditions fail
- Action and Integration System — email, HTTP/webhook, GitHub (database if feasible); engine calls Action, not the vendor API
- Workflow Execution Engine and History — record status, errors, retries; users can inspect runs

## Nice-To-Have Features

- Database integration
- Schedule trigger if core engine is stable (Render sleep makes this unreliable)

## Out Of Scope (not in MVP)

- AI-generated workflows
- Drag-and-drop visual editor
- Large integration marketplace
- Slack/Discord/Teams
- Complex branching/loops
- Team collaboration
- Advanced analytics
- Enterprise RBAC
- Enterprise-scale distributed execution

## Success Signals

Numerical targets are TBD until real usage exists. Track:

- Activation: users creating their first workflow
- Engagement: workflows successfully executed
- Reliability: successful execution rate
- Retention: users returning to manage workflows
- Feedback: usability of the builder

Most important early signal: a real user can create and successfully execute a useful workflow.

## UI / UX

- Feel: Clean · Technical · Minimal · Professional
- Screens: landing, dashboard, workflow builder (WHEN / IF / THEN), execution history
- Basic responsive layout; no visual canvas in V1

## Constraints

- Timeline: 4 weeks
- Budget: ₹0 / $0; GitHub, Vercel, Render, Supabase free tiers
- Platform: Web
- No paid APIs, queues, or AI APIs in V1
