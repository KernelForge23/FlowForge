# Testing

## Required Before Completion

- Relevant tests pass.
- Typecheck/build passes when frontend exists.
- User-visible changes are checked in a browser when applicable.
- No tests skipped or weakened without approval.
- Evidence is reported in the final response.

## Commands

- All tests: `pytest`
- Single test: `pytest path/to/test_file.py -k name`
- Typecheck: `tsc --noEmit`
- Lint: `npm run lint`
- Build: `npm run build`
- Browser/device: frontend + backend locally, then sign-in → create workflow → manual run → history at http://localhost:5173 (and a narrow viewport)

## What To Test

| Change type | Minimum check |
|-------------|---------------|
| Pure logic | Unit test engine, triggers, conditions, actions, factories |
| API/data flow | Workflow CRUD, run, webhooks, ownership |
| UI behavior | Builder, dashboard, history in the browser |
| Auth, migrations, deployment | Human review plus a focused test |
| HTTP action safety | Reject private/loopback URLs and oversize payloads |

Highest priority: WorkflowEngine, trigger/condition evaluation, action execution, factories, auth boundaries, webhook handling.

Example engine proof (why this matters): construct GitHubTrigger + repository condition + HTTPAction, feed a matching event, assert the action ran and a SUCCESS execution was stored. That proves the OOP pipeline without the UI.

## AI Checks

Not applicable in V1.
