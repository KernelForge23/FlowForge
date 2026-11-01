"""Generate the auditable source appendix and typeset the viva master PDF.

This documentation helper reads an explicit allowlist of source/config files.
It never loads app settings, imports the application, or reads actual .env files.
Run with a Python environment containing reportlab and pypdf.
"""
from __future__ import annotations

import ast
import hashlib
import html
import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / "docs" / "viva"
PDF_DIR = ROOT / "output" / "pdf"

FILE_NOTES = {
    "backend/app/config.py": "Typed application settings. BaseSettings loads backend/.env by a file-relative absolute path and environment values; the guide never reads that file. Defaults are development choices, not proof that production is securely configured.",
    "backend/app/db.py": "Database engine and transaction-scoped dependency. SQLAlchemy engine is unrelated to WorkflowEngine. flush sends SQL in a transaction; get_session commits/rolls back/closes. create_all is initial table creation, not versioned migration management.",
    "backend/app/main.py": "Application composition root. Startup creates tables, CORS permits configured/local origins, and the API router mounts routes. The async lifespan contains synchronous initialization and yields control to the application's running phase.",
    "backend/app/api/auth.py": "Remote Supabase token verification and identity object. Empty supabase_url returns None for local mode. A configured service requires Bearer syntax, calls the remote user endpoint, and validates ID/email fields. This is not local JWT signature verification.",
    "backend/app/api/routes/health.py": "Thin liveness route with an injected health service. A successful response does not test database readiness or external provider connectivity.",
    "backend/app/api/routes/workflows.py": "Resource routes enforce ownership when authentication is configured, translate errors, and call service/repository operations. _detail returns action config, including any stored GitHub token. The run route maps all ValueErrors to 404, including disabled workflow errors.",
    "backend/app/api/routes/webhooks.py": "GitHub-only ingestion with optional configured HMAC verification. Raw bytes are authenticated before JSON parsing. Candidate selection spans all enabled webhook workflows; no tenant routing, delivery deduplication, request-size bound, or background queue exists.",
    "backend/app/api/routes/integrations.py": "Authenticated Gmail connect/status/disconnect and state-validated callback. State is hashed in storage, expires in ten minutes, and is marked used. Callback redirects with status/error query parameters. Disconnect is local deletion, not provider-side revocation.",
    "backend/app/core/event.py": "Dataclasses normalize an event envelope and hold per-run context. Each instance receives fresh dicts. lookup is top-level only, prioritizes context.data, and does not traverse dotted paths. Event.source and payload['source'] are distinct.",
    "backend/app/core/workflow.py": "Runtime object composition: name, Trigger, optional Condition, ordered Actions. It is not an ORM row and does not itself execute. Ordinary Python references are stored without runtime type enforcement.",
    "backend/app/core/engine.py": "The framework/ORM-independent execution algorithm. Trigger/condition gating happens before the action try block. Actions run in order and stop on first exception. Exception strings are preserved, not universally redacted. Empty action lists succeed with zero count.",
    "backend/app/core/factories.py": "Simple static factories turn recognized type/config data into Python objects. Composite condition construction recurses. Branches belong here rather than in the engine. This is not arbitrary class loading or eval.",
    "backend/app/core/actions/base.py": "Action's small abstract contract. Subclasses implement execute(context); an action produces a side effect or context mutation, while the engine creates the final result.",
    "backend/app/core/conditions/base.py": "Condition's abstract boolean contract. A concrete leaf or group can be used anywhere a Condition is expected.",
    "backend/app/core/triggers/base.py": "Trigger's abstract boolean contract. It checks an already delivered normalized event; a trigger class is not itself a network receiver or timer.",
    "backend/app/core/triggers/manual.py": "Manual matches type manual OR source manual. This is intentionally broader than matching only the type. It does not inspect payload.source.",
    "backend/app/core/triggers/webhook.py": "Webhook requires normalized type webhook and optionally restricts the source. None means no source restriction in the core object.",
    "backend/app/core/triggers/scheduled.py": "Only an event-type predicate. There is no timer, cron scheduling, job persistence, or automatic event generation in this file or the running application.",
    "backend/app/core/conditions/equals.py": "Equality leaf over a top-level context lookup. Missing fields become None; Python's equality semantics apply without universal strict type normalization.",
    "backend/app/core/conditions/comparison.py": "Inequality, ordering, and membership leaves. Ordering/membership TypeErrors become False. A missing field can still pass NotEquals. Contains checks dictionary keys, list elements, or string substrings depending on the candidate type.",
    "backend/app/core/conditions/composite.py": "Composite pattern. Child iterables are materialized as lists. all/any short-circuit and permit nested groups. Empty AND is True; empty OR is False.",
    "backend/app/core/actions/noop.py": "Deterministic side-effect recorder used for demonstration/tests. calls belongs to this runtime instance and is not a persistent execution history table.",
    "backend/app/core/actions/http.py": "Generic synchronous outbound JSON request. Public URL checks and disabled redirect following mitigate SSRF. Validation DNS is not pinned to connection DNS. Bounded immediate retries do not provide idempotency; no response-size cap or overall workflow deadline exists.",
    "backend/app/core/actions/github.py": "Outgoing GitHub action. The supported UI/demo path is repository dispatch, which can trigger the separate YAML workflow. Stored token is ordinary config. The extra issues/comments path lacks an issue number and is not a complete verified comment-creation feature.",
    "backend/app/core/actions/email.py": "Shared input validation with globally selected Resend/Gmail behavior. Resend has request-size checking/retries; Gmail delegates to GmailService and lacks the same send retry/message-size check. A basic regex is not proof that a mailbox exists.",
    "backend/app/models/base.py": "SQLAlchemy declarative Base, per-row UUID-string generator, and created_at mixin. server_default executes in the database; callable default=new_id is distinct from prematurely calling new_id().",
    "backend/app/models/entities.py": "Nine persisted entities, distinct from runtime/Pydantic objects. Relationships express navigation and ORM cascades; foreign keys/uniqueness express constraints. Gmail token columns hold ciphertext created by the service, while generic JSON config is not automatically encrypted.",
    "backend/app/schemas/workflows.py": "Pydantic API shapes. Names have length bounds; component config remains broad. Empty action lists are allowed. WorkflowUpdate replaces config rather than implementing partial PATCH. Response models distinguish summaries from full editable details.",
    "backend/app/schemas/health.py": "Pydantic response shape for the liveness endpoint: two strings, status and service.",
    "backend/app/repositories/workflow.py": "Focused SQLAlchemy lookups, additions, and owner/history listing. list methods are filtered and sorted but not paginated. Ownership authorization is checked by routes, not automatically by this class.",
    "backend/app/services/workflow.py": "Use-case coordinator. Saves configuration, validates factory construction, hydrates objects, enforces enabled before run, and stores the engine result. Timestamps are currently generated after execution and only action_count is persisted from the result.",
    "backend/app/services/gmail.py": "Google OAuth token exchange/profile, per-user encrypted connection storage, refresh, and MIME send. Hashing state, encrypting recoverable tokens, and base64url message encoding solve three different problems. Local disconnect does not revoke Google consent.",
    "backend/app/services/health.py": "Returns a fixed liveness response. It performs no database/provider checks.",
    "backend/tests/conftest.py": "Shared test fixtures use in-memory SQLite and temporarily disable configured auth/select Resend. TestClient drives the ASGI app. Dependency overrides in individual API tests supply the test database/user. Tests exercise mocked providers, not live delivery.",
    "frontend/src/main.tsx": "Browser entry point. Imports the active index.css, finds the root element, and renders App in development StrictMode. The non-null assertion is erased and does not check root existence at runtime.",
    "frontend/src/lib/supabase.ts": "Creates a browser Supabase client only when public URL/key values exist. VITE_ values are build-time public configuration; no backend secret belongs here.",
    "frontend/src/services/api.ts": "Shared typed fetch wrapper and endpoint methods. Generic assertions do not runtime-validate returned JSON. Tokens are propagated; 204 is handled without JSON parsing. There is no fetch cancellation timeout/retry/cache.",
    "frontend/src/App.tsx": "Single component for auth, Gmail, builder, list, and history. The builder loads/saves only the first condition and action, while the backend supports richer config. State/effects update the browser; the server executes workflows. No Router, Redux, Tailwind, or Axios is used.",
    "frontend/src/index.css": "Active product styling imported by main.tsx. Plain CSS implements cards, forms, grid/flex layout, status/errors, and a narrow-screen breakpoint at 720 CSS pixels. Naming Inter does not itself download the font.",
    "frontend/src/App.css": "INACTIVE starter stylesheet: App.tsx does not import this file. Its counter/hero/docs/ticks selectors and CSS variables are scaffold remnants, not workflow behavior. Notes explain the syntax without claiming these rules style the running product.",
    "frontend/package.json": "Actual package/script manifest. build performs tsc -b then Vite; lint is Oxlint. Caret/tilde ranges are compatible-version declarations, not exact installed versions. No npm test/typecheck script exists.",
    "frontend/vite.config.ts": "Vite configuration enabling the React plugin; not a Python server or the workflow engine.",
    "frontend/index.html": "Static HTML shell with an empty React root and a module entry. Browser receives generated production assets after Vite builds. Current title remains frontend.",
    "frontend/.oxlintrc.json": "Actual Oxlint settings; React hooks rules are enabled. Linting catches patterns distinct from TypeScript type checking.",
    "backend/requirements.txt": "Backend dependency lower bounds. These are not a reproducible exact version lock. The Python standard library is not installed from this list.",
    "backend/pytest.ini": "pytest import/discovery settings for normal backend execution.",
    ".github/workflows/flowforge-dispatch.yml": "Read-only explanation of the existing GitHub Actions demonstration. A repository_dispatch type flowforge runs a hosted job that creates an issue. Runtime GITHUB_TOKEN is distinct from FlowForge's dispatch token. No workflow/infrastructure changes were made.",
}

TEST_PURPOSES = {
    "test_current_user_reads_supabase_identity": "Mock the remote user endpoint and verify identity mapping; this does not test all missing/invalid token paths.",
    "test_settings_load_backend_env_file_independent_of_working_directory": "Verify that the declared dotenv path is computed from the backend location; no dotenv contents are printed.",
    "test_factories_hydrate_nested_conditions_and_triggers": "Verify nested condition factory/evaluation. The object-type checks for trigger/action are weak because almost everything is an object.",
    "test_comparison_and_or_conditions": "Verify greater/less/not-equal and an OR result using deterministic context data.",
    "test_engine_skips_before_actions_when_trigger_or_condition_fails": "Verify both gating failures produce SKIPPED and never call the action.",
    "test_engine_executes_actions_in_order": "Check two actions ran once and count is two. The assertions do not independently record exact interleaving order.",
    "test_engine_preserves_safe_action_error": "Supply a failing duck-typed action and verify FAILED preserves the deliberately safe example error.",
    "test_gmail_action_sends_message_without_exposing_token": "Store encrypted fake tokens, mock the Gmail network call, verify safe metadata and no token in context data.",
    "test_gmail_service_rejects_missing_connection": "Verify an unconnected user cannot send through Gmail.",
    "test_gmail_connect_and_callback_store_user_connection": "Override session/identity and token exchange/profile to exercise OAuth connect/callback persistence without Google.",
    "test_health_ok": "Exercise liveness response fields through TestClient, not production readiness.",
    "test_http_action_rejects_private_addresses": "Verify loopback destination rejection without making the outbound request.",
    "test_http_action_rejects_unsupported_scheme": "Verify file URLs are not accepted as generic HTTP action destinations.",
    "test_http_action_records_status_without_response_body": "Mock the HTTP client and verify request destination and safe status metadata.",
    "test_github_action_sends_token_without_storing_it": "Verify a fake token enters the outbound Authorization header and only safe action metadata is recorded; it does not prove config encryption.",
    "test_email_action_sends_safe_metadata": "Mock Resend and verify request auth plus selected result metadata without provider secrets in context data.",
    "test_email_action_validates_recipients": "Verify malformed recipient config raises before any send.",
    "test_workflow_configuration_round_trip": "Construct ORM rows/relationships and verify retrieval of saved workflow configuration.",
    "test_manual_trigger_matches_manual_event": "Check a manual normalized event matches the concrete trigger through its base type.",
    "test_manual_trigger_rejects_webhook_event": "Check an ordinary GitHub webhook does not match ManualTrigger.",
    "test_equals_condition_true_and_false": "Check equality on matching and nonmatching context data.",
    "test_workflow_composition_executes_actions_via_base_type": "Compose objects, evaluate the parts, and call an action through the shared interface.",
    "test_create_load_and_run_workflow_api": "Exercise create/detail/manual-run HTTP endpoints with an overridden test database.",
    "test_github_webhook_runs_enabled_webhook_workflow": "Create an enabled webhook workflow and exercise ingestion with unsigned local-mode test data.",
    "test_github_webhook_requires_valid_signature": "Configure a fake secret and compare a missing-signature rejection with a correctly HMAC-signed request.",
    "test_workflow_can_be_updated_and_deleted": "Verify full configuration update and workflow deletion through routes.",
    "test_workflow_with_execution_can_be_deleted": "Regression proof that ORM cascading allows deletion after a persisted execution exists.",
    "test_create_load_run_records_execution": "Exercise service creation, hydration, execution, and history persistence together.",
}

APP_NOTES = {
 1:"Import the two React hooks used for state and lifecycle synchronization.",
 2:"Import only FormEvent's TypeScript type; it is erased from runtime output.",
 3:"Import the Supabase session type, distinct from a SQLAlchemy database Session.",
 4:"Import the shared endpoint client rather than repeating fetch wiring in each handler.",
 5:"Import domain/API types for compile-time checking; they do not validate server JSON at runtime.",
 6:"Import the nullable configured Supabase client.",
 8:"Arrow function returns a fresh configuration object; parentheses around the object distinguish it from a function block. The return type is the local Component type, not a React component.",
 9:"Read the public Vite API URL and fall back only for null/undefined; an empty string is preserved by ??.",
 10:"Remove one trailing slash with a regex and append the GitHub webhook route for setup instructions.",
 12:"Define the React function component. Its function body runs on each render; hooks preserve their own state between renders.",
 39:"Register the session synchronization effect. Its callback runs after React commits the component, with development StrictMode checks possible.",
 40:"If no Supabase client was configured, finish effect setup immediately.",
 41:"Request the SDK session asynchronously; destructure data from its result and update React session state. void discards the promise value, not its work.",
 42:"Subscribe to auth changes. The unused event argument is prefixed with an underscore; the callback installs the new session in state.",
 43:"Return an effect cleanup function to unsubscribe, avoiding stale auth subscriptions.",
 44:"End the effect with an empty dependency array: no state dependency reruns it during ordinary updates; StrictMode may still test setup/cleanup in development.",
 46:"Register a mount-time effect that interprets query parameters after an OAuth redirect.",
 47:"Construct the browser query parser from the current URL's search component.",
 48:"Read the gmail outcome parameter; missing query values are null.",
 49:"Read optional provider error detail from the URL.",
 50:"Only the error outcome enters this branch.",
 51:"Display supplied detail or a reason-based fallback. This direct state update inside the effect is the reported lint warning.",
 52:"Replace the current history URL without navigating, removing callback query parameters from the visible URL.",
 54:"End the callback-query effect; empty dependencies make it mount-oriented.",
 56:"Start an effect synchronizing the workflow list with the signed-in user ID.",
 57:"Only refresh when an authenticated user ID exists; the async helper handles its own errors.",
 58:"Rerun when the user ID changes, rather than whenever every session object reference changes.",
 60:"Start a separate user-dependent Gmail status synchronization effect.",
 61:"Do not request Gmail connection status without a signed-in user.",
 62:"Fetch status, pass success directly to the state setter, and fall back to disconnected on failure; this path intentionally hides the specific status error.",
 64:"Depend on user ID so status refreshes when identities change.",
 66:"Define an async list-refresh helper; parameter type is string and its inferred return is a Promise.",
 68:"Await the API list and replace workflows state with the returned summaries.",
 70:"Narrow the caught value with instanceof Error before reading message, otherwise use a safe fallback.",
 74:"Define the form submit handler with React's FormEvent type.",
 75:"Prevent the browser's normal form navigation/reload.",
 76:"Guard against missing public authentication configuration.",
 77:"Show an actionable configuration message without printing any key value.",
 80:"Mark the UI busy, disabling relevant buttons on the next render.",
 81:"Clear the previously displayed error.",
 82:"Send email/password to Supabase's authentication client and rename its returned error field to loginError.",
 83:"Clear the busy state after the awaited login response. This handler does not wrap the await in try/finally for unexpected rejections.",
 84:"Show the SDK-reported login error, if one was returned.",
 87:"Load a detailed workflow into builder state, or reset the builder when passed null.",
 88:"Store the selected detail object; selection controls edit mode and Run now.",
 89:"Load name, defaulting to an empty string only when selection/name is nullish.",
 90:"Load enabled while preserving a real false; ?? avoids replacing false with true.",
 91:"Use the saved trigger type, or manual as the new-workflow default.",
 92:"Take only the first condition. Additional backend conditions are not represented by this editor.",
 93:"Update the optional condition selection.",
 94:"Read config.field only if it is a string; unknown config requires runtime narrowing.",
 95:"Read config.value only if it is a string. Numeric/boolean API condition values are not round-tripped faithfully here.",
 96:"Take only the first action or a newly allocated no-op config. Saving an API-created multi-action workflow through this editor can discard extra actions.",
 97:"Load the action discriminator used by conditional form rendering.",
 98:"Pretty-print config with two-space JSON indentation for the generic configuration textarea.",
 99:"Populate the GitHub password input from stored config when it is a string; masking does not mean the API redacted/encrypted it.",
 100:"Load the target owner/repository string after type checking.",
 101:"Load the event type or default flowforge; this must match a target repository workflow listener.",
 102:"Pretty-print client payload, defaulting nullish body to a fresh empty object for display.",
 103:"If recipients are an array, use a type-predicate filter to keep strings and join them for the comma-separated input. A single string config is not loaded into this input by this expression.",
 104:"Load an email subject only when its config value is a string.",
 105:"Load the plain text email body after type narrowing.",
 106:"Load optional HTML after type narrowing.",
 109:"Define selection handling for a summary row; summary lacks full component config.",
 110:"Clear an old error before loading the selected workflow.",
 112:"Fetch full detail using the summary's ID.",
 113:"Populate editor state from the fetched detail.",
 114:"Fetch and display the selected workflow's persisted executions. This is a request, not a real-time subscription.",
 116:"Show either the caught Error message or a selection-specific fallback.",
 120:"Define the create/update form handler; its behavior depends on whether selected is null.",
 121:"Stop native form navigation so saving stays within the SPA.",
 122:"Exit for missing identity or a blank trimmed name. The payload later uses the original name string rather than the trimmed one.",
 123:"Declare a mutable local object whose values remain unknown until action-specific checks narrow them.",
 124:"Choose dedicated email-field validation and configuration.",
 125:"Split at commas, trim whitespace, and remove empty recipients with filter(Boolean). This is formatting; the backend validates addresses too.",
 126:"Require recipients, a nonblank subject, and at least one nonblank text/HTML body in the UI.",
 127:"Report the email validation requirement and leave the workflow unsaved.",
 130:"Begin construction of the email action config object.",
 131:"Store the normalized recipients array under the provider-independent to key.",
 132:"Save the trimmed subject.",
 133:"Conditionally spread a text property only if emailText is truthy.",
 134:"Conditionally spread an html property only if emailHtml is truthy.",
 136:"Choose GitHub-specific validation rather than the generic JSON textarea.",
 137:"Require nonblank token, repository, and event type before attempting save.",
 138:"Show the missing GitHub configuration error.",
 142:"Parse the client payload string but assign the result to unknown so its shape must be checked.",
 143:"Require a non-null, non-array object. JavaScript's typeof null is object, so the explicit null check matters.",
 144:"Throw a local validation error that the surrounding catch will display.",
 146:"Begin the dedicated GitHub config object.",
 147:"Store the trimmed token in config. This MVP later persists it as ordinary JSON.",
 148:"Store the trimmed owner/repository value.",
 149:"Store the trimmed dispatch event type.",
 150:"Use the validated object as client_payload data through the GitHub action's body setting.",
 153:"Display JSON parse/shape error with a GitHub-specific fallback.",
 156:"For no-op or generic HTTP, parse the generic action configuration string.",
 158:"Parse user-entered JSON and keep its type unknown until the following guard.",
 159:"Reject primitives, null, and arrays as the top-level configuration value.",
 160:"Assert the checked object shape for TypeScript. The as assertion itself adds no runtime check.",
 162:"Display parse/shape errors and avoid sending malformed config to the API.",
 166:"Build the condition array from whether a condition is selected.",
 167:"Create exactly one condition with a string expected value when enabled in this UI.",
 168:"Otherwise send an empty condition array, meaning no condition gate.",
 169:"Begin the workflow payload object shared by create and update.",
 170:"Use object-property shorthand to include name state.",
 171:"Include the enabled boolean state.",
 172:"For a webhook trigger, restrict source to github; manual config is empty.",
 173:"Include the just-constructed zero/one condition array.",
 174:"Include exactly one action configuration; backend multiple-action capability is not exposed here.",
 176:"Set busy before the save request to prevent ordinary duplicate button submissions.",
 177:"Clear old errors before calling the backend.",
 179:"A selected workflow means replacement update rather than creation.",
 180:"Send PUT through the API wrapper for the selected ID.",
 182:"For creation, add authenticated user_id and spread the common payload into a new object.",
 184:"Refresh the user's list after a successful save.",
 185:"Clear name state (loadBuilder(null) below also resets it).",
 186:"Reset the selection/builder to new-workflow mode.",
 188:"Display a save-specific error without throwing through the UI event callback.",
 189:"Finally executes whether save succeeded or failed.",
 190:"Clear busy so controls are usable again.",
 194:"Define the async workflow-deletion event operation.",
 195:"Exit when no selection exists or the user declines the browser confirmation. Template interpolation shows the workflow name.",
 196:"Mark deletion busy.",
 198:"Request deletion of the selected workflow and its configured ORM dependents.",
 199:"Refresh the list only if an identity is still present.",
 200:"Clear the selection and reset editor defaults.",
 201:"Clear history that belonged to the deleted workflow.",
 203:"Show deletion errors.",
 205:"Always clear deletion's busy state.",
 209:"Define the manual-run event handler.",
 210:"Ignore a run request if no workflow is selected.",
 211:"Mark run busy to disable ordinary repeat clicks.",
 212:"Clear an old error before executing.",
 214:"Send payload.source=dashboard. The backend separately sets the normalized Event type/source to manual.",
 215:"Reload persisted history after the run response. It is not continuously refreshed for external webhooks.",
 217:"Display request-level run errors; FAILED/SKIPPED can still arrive in an HTTP-successful execution response.",
 219:"Clear busy even if the request/history refresh fails.",
 223:"Define Gmail disconnect handling.",
 224:"Mark disconnect busy.",
 226:"Ask the backend to delete the current user's stored Gmail connection.",
 227:"Update the UI to disconnected with no email. This does not revoke provider consent.",
 229:"Display disconnect errors.",
 231:"Always clear disconnect's busy state.",
 235:"Define Gmail authorization initiation.",
 236:"Mark connection startup busy.",
 237:"Clear an old error before initiating OAuth.",
 239:"Ask the backend for an authorization URL tied to a stored state and the authenticated user.",
 240:"Navigate the browser to Google consent. This intentionally leaves the FlowForge page.",
 242:"Display startup errors if the backend cannot prepare the flow.",
 243:"Clear busy on failure; on success navigation takes over instead of a finally reset.",
 247:"Without an established session, render the sign-in branch rather than the dashboard.",
 248:"Return begins the sign-in JSX expression; returning ends this render branch.",
 249:"Semantic main region with a CSS class for centered authentication layout.",
 250:"Card section for the login content; className is JSX's class attribute spelling.",
 251:"Brand text; it is static UI content, not a backend operation.",
 252:"Static introductory heading inside the auth card.",
 253:"Instructional copy describing sign-in's purpose.",
 254:"Form submits through the login function; passing the function does not execute it during render.",
 255:"Controlled required email input. onChange copies the browser field value into email state; type=email adds browser-level validation hints.",
 256:"Controlled required password input. type=password masks display but does not encrypt state.",
 257:"Default submit button is disabled while busy and uses a ternary label.",
 259:"Short-circuit rendering shows the error paragraph only for a truthy error value. React escapes the interpolated text.",
 265:"Return the signed-in dashboard's JSX tree.",
 266:"Semantic app main region; max width/layout comes from active CSS.",
 267:"Header region groups branding and sign-out control.",
 268:"Static brand and description in a grouping div.",
 269:"Pass a click callback that invokes optional Supabase signOut; void discards its promise value. There is no explicit rejection display in this handler.",
 271:"Start the main content section.",
 272:"Display workflow heading and eyebrow label.",
 273:"Start the Gmail connection card.",
 274:"Flex header layout for connection text and controls.",
 275:"Choose connected email text or instructions with a ternary expression.",
 276:"Render the relevant Connect/Disconnect button based on gmail.connected; callbacks defer execution until clicked and busy disables them.",
 279:"Start the CSS grid holding builder/list and selected workflow history.",
 280:"Start the workflow builder card.",
 281:"Choose Edit workflow versus Create workflow according to selected.",
 282:"Bind form submission to saveWorkflow.",
 283:"Controlled required name input.",
 284:"Controlled select exposes Manual and GitHub webhook only. ScheduledTrigger exists in the backend but is absent here.",
 285:"Only for webhook type, render setup instructions and the computed URL. Displaying a secret variable's name is not revealing its value.",
 286:"Controlled boolean checkbox uses checked and event.target.checked rather than value.",
 287:"Controlled condition select supports none/equals/contains/not-equal. Selection constructs a fresh Component or null; ?? preserves valid non-null strings.",
 288:"Only render field/value inputs when a condition exists. Both values are strings; no numeric/group editor is provided.",
 289:"Controlled action select exposes no-op, HTTP, GitHub dispatch, and email.",
 290:"Nested JSX ternaries render provider-specific fields: email recipient/content controls, GitHub token/repository/event/payload controls, or generic HTTP JSON. Fragments group fields without extra wrappers; each input is controlled. A password field only masks the GitHub token visually.",
 291:"Submit saves; Cancel/Delete explicitly use type=button so they do not submit. Optional edit controls render inside a Fragment. Busy changes submit label and disables it.",
 293:"Container for saved workflow summary buttons.",
 294:"Show an empty-state message when the list is empty.",
 295:"Map summaries to buttons with stable ID keys. A template string adds selected CSS styling; click fetches detail/history; the label shows ACTIVE/DRAFT from enabled.",
 298:"Start selected workflow detail/history card.",
 299:"Use optional chaining and nullish fallbacks for heading/action description. Show Run now only if selected; its callback requests backend manual execution.",
 300:"Static execution history subheading.",
 301:"Show selection instructions only when no workflow is selected.",
 302:"If selected but history is empty, show a no-executions message.",
 303:"Map execution rows using stable IDs; display status, optional stored error, and an eight-character ID preview. This does not show provider action_results because those are not persisted by the service.",
 306:"Show request/UI errors below the dashboard. This message is distinct from each execution's stored error.",
 312:"Export App as this module's default so main.tsx can import it without braces.",
}

STATE_MEANINGS = {
 "session":"Supabase identity/session or null before sign-in/session loading", "email":"login email text", "password":"login password text held in browser state", "workflows":"saved workflow summaries", "selected":"full selected workflow or null for creation mode", "executions":"selected workflow's persisted history", "name":"builder workflow name", "triggerType":"builder trigger discriminator", "condition":"optional builder condition configuration", "conditionField":"top-level payload/context key", "conditionValue":"string expected condition value", "actionType":"builder action discriminator", "actionConfig":"generic action config as editable JSON text", "githubToken":"GitHub credential input, masked only by input presentation", "githubRepository":"target owner/repository", "githubEventType":"repository dispatch event discriminator", "githubPayload":"client payload as JSON text", "emailTo":"comma-separated recipient input", "emailSubject":"email subject input", "emailText":"plain text email input", "emailHtml":"optional HTML email input", "enabled":"whether the saved workflow may execute", "error":"displayed request/UI error or null", "busy":"whether a UI operation is in progress", "gmail":"Gmail connection status and email only, without OAuth token values",
}

API_NOTES = {
 3:"Define the compile-time workflow summary object type. It contains no trigger/action config.",
 10:"Define the reusable component-configuration type; this is not React.Component.",
 12:"Record<string, unknown> permits string keys but requires narrowing values before assuming operations.",
 15:"Intersect Workflow's summary fields with the following detail fields.",
 17:"Conditions is an array in the API even though this UI edits only the first.",
 18:"Actions is an ordered array in the API even though this UI edits only the first.",
 21:"Describe persisted execution JSON, distinct from a runtime EngineResult class.",
 27:"An execution error can be a string or explicitly null.",
 30:"Public Gmail status contains only connection flag and account email.",
 35:"Describe the backend connect response containing Google's consent destination.",
 39:"Read the public backend URL with a localhost development fallback.",
 41:"Define an async generic request wrapper: T is the expected response type, RequestInit is the optional native fetch options type, and the result is Promise<T>.",
 42:"Safely call a configured Supabase client; if absent, supply a compatible null-session data shape. Destructure data from the awaited/default result.",
 43:"Read the access token only if there is a session.",
 44:"Call native fetch with the configured origin plus API path.",
 45:"Spread caller method/body/options before constructing the explicit headers below.",
 46:"Begin the headers object.",
 47:"Set JSON request content type by default.",
 48:"Conditionally add a Bearer header when a token exists. The template expression constructs the header value.",
 49:"Spread caller headers last so matching defaults can be overridden. This assumes compatible spreadable headers rather than normalizing every HeadersInit variant.",
 52:"fetch does not reject just because a server returns 4xx/5xx, so explicitly inspect response.ok.",
 53:"Try parsing error JSON; if it is not JSON, replace the parse rejection with an empty object.",
 54:"Throw a useful detail string if provided, or a generic error. Structured validation-detail arrays are not formatted by this wrapper.",
 56:"204 has no body: return undefined asserted as T instead of parsing JSON.",
 57:"Return JSON with an asserted generic promise type. This is not runtime schema validation.",
 60:"Export a collection of endpoint functions sharing request/token/error behavior.",
 61:"List method accepts a user ID; backend must independently verify ownership.",
 62:"URL-encode the query value and expect an array of summary objects.",
 63:"Retrieve full editable detail for one ID.",
 64:"Creation accepts unknown payload; the server's Pydantic schema is the runtime trust boundary.",
 65:"POST JSON-serialized config and expect a workflow summary.",
 66:"Replacement update accepts a workflow ID and payload.",
 67:"PUT to the selected resource and expect full detail.",
 68:"Specify replacement update HTTP method.",
 69:"Serialize the replacement payload into request body text.",
 71:"Define deletion for one workflow ID.",
 72:"Expect no meaningful return value for a DELETE that responds with 204.",
 73:"Manual run accepts a dictionary payload with unknown values.",
 74:"Expect an execution record from the run operation.",
 75:"Use POST for the run request.",
 76:"Wrap custom event input inside the ManualRunRequest payload field and serialize it.",
 78:"Retrieve persisted execution history; no streaming/subscription is established.",
 79:"Retrieve only the Gmail connection flag/account email.",
 80:"Ask the server to prepare an OAuth state and authorization URL.",
 81:"Delete the local Gmail connection; this endpoint's default response differs from the workflow 204 route but the wrapper still parses it.",
}

EXACT = {
 "backend/app/core/engine.py": {
 8:"Create a string-valued enum so statuses have symbolic identity and serializable string values (Python 3.11+ StrEnum).",
 14:"Generate a result data object whose fields cannot normally be reassigned after construction; this is shallow immutability.",
 17:"Default completed-action count to zero; skipped runs need not specify it.",
 22:"Public engine operation receives runtime composition, normalized event, and optional owner; no database session enters this method.",
 23:"Call the concrete Trigger polymorphically and negate its boolean result; if it does not match, enter the early-return branch.",
 24:"End execution immediately as SKIPPED with the trigger reason; no context/actions are created/run yet.",
 26:"Construct a fresh per-run context, carrying event and owner identity for user-specific actions such as Gmail.",
 27:"Short-circuit the None check before calling evaluate. A false concrete condition enters the skip branch.",
 28:"End as SKIPPED with a condition reason; action_count retains its default zero.",
 30:"Initialize the number of actions that have returned normally.",
 31:"Begin exception handling for the action loop only; trigger/condition failures above are outside this block.",
 32:"Visit each runtime Action in the stored/configured order.",
 33:"Dynamic dispatch calls this concrete action's execute with the shared execution context; the engine has no provider-type branch.",
 34:"Increase the count only after execute returns; the failing action itself is not counted as completed.",
 35:"Catch an Exception from action iteration/execution; later actions stop. BaseException subclasses such as KeyboardInterrupt are not covered.",
 37:"Mark attempted action execution as FAILED, distinguishing it from rule-based SKIPPED.",
 38:"Preserve the number of previously completed actions; no external side effects are rolled back.",
 39:"Preserve the exception's string or fall back if empty. This relies on safe action errors, not automatic redaction.",
 41:"If all actions return, finish SUCCESS with their count; an empty list yields SUCCESS with zero.",
 },
 "backend/app/core/event.py":{
 12:"Create a fresh payload dictionary per Event via default_factory; Any permits varied JSON-like input without strict field typing.",
 13:"Use a deferred lambda to capture a new timezone-aware UTC timestamp at each Event construction.",
 19:"Store the owning user ID when supplied, enabling per-user integration lookup; None supports pure core/local tests.",
 20:"Create fresh mutable data for each execution context; actions can append selected results here.",
 23:"Test key presence in context data rather than truthiness of its value, so even a stored None/False overrides payload.",
 24:"Return the exact context-data value when the key exists.",
 25:"Otherwise perform a top-level payload get, returning None if absent; dots are literal characters here.",
 },
 "backend/app/services/workflow.py":{
 8:"Alias the runtime composition class as RuntimeWorkflow to distinguish it from the ORM Workflow imported next.",
 42:"Flush child/parent configuration into the current transaction without committing it.",
 43:"Build component objects to reject unsupported/bad configuration before the request can commit.",
 60:"Replace the stored condition collection; delete-orphan cascade removes disconnected old rows on flush.",
 64:"Replace the action collection and rebuild position values, rather than partially merging actions.",
 82:"Validate trigger factory construction without executing a workflow.",
 86:"Validate an action's constructor. Gmail's service is absent here; its actual presence is checked during execution.",
 88:"Return both the persisted row and a separate executable runtime composition.",
 93:"For several condition rows, construct one implicit AND configuration around their type/config representations.",
 95:"The conditional expression selects the implicit AND path only when there is more than one top-level row.",
 99:"For one condition construct it directly; for no conditions use None so the engine has no gate.",
 105:"Inject a session-bound GmailService into hydrated actions; the factory uses it for email.",
 119:"Normalize a manual request into a manual envelope; source strings inside payload remain separate data.",
 123:"Hydrate before checking enabled, so invalid configuration can fail before the disabled-policy check.",
 125:"Raise for a disabled workflow rather than creating a SKIPPED execution row.",
 126:"Invoke the engine synchronously and bind owner identity from stored data, not an untrusted run-payload owner.",
 130:"Assign start time after the engine already returned; currently not a true measured start timestamp.",
 131:"Assign completion time immediately afterward; subtracting these timestamps misses action duration.",
 132:"Persist raw event payload without a general redaction filter.",
 133:"Persist only action_count; action_results appended by concrete actions are not included in this stored result.",
 134:"Persist the engine error string; custom actions must avoid sensitive exceptions.",
 },
 "backend/app/core/actions/email.py":{
 12:"Compile a basic anchored email-shape regex. Raw string syntax preserves backslashes for the regex; this is not full email-standard validation.",
 16:"Require a string and check the address extracted by parseaddr with a full match. The original value is returned, not the parsed address.",
 29:"This condition checks for absent Gmail service but the following assignment changes nothing.",
 30:"Redundant assignment of None to a value already None; actual rejection occurs in execute.",
 34:"Validate sender only for Resend; Gmail sends from the account connection and keeps sender as None here.",
 59:"For Gmail, require both the injected service and a workflow owner in context before attempting a send.",
 69:"Append the Gmail result to transient context data, not directly to the execution table.",
 89:"Bound serialized Resend request bytes. This check is below the earlier Gmail return and therefore does not bound Gmail messages.",
 92:"Default two retries means three total attempts; there is no backoff delay.",
 },
 "backend/app/core/actions/http.py":{
 18:"Resolve hostname to socket addresses before request construction. Default resolver port is 443 even for HTTP; the eventual client still uses URL semantics.",
 22:"Tuple index 4 is sockaddr; its first item is the resolved IP string. Convert it to an ipaddress object for classification.",
 23:"Reject these nonpublic/local classifications for every returned address. This is not connection-address pinning or a complete egress policy.",
 39:"Read header pairs from configured mapping-like data. A nonmapping truthy value can raise before a safe ValueError is produced.",
 43:"Keep selected JSON-compatible body types; None and unsupported values become an empty object.",
 46:"Pre-serialize an outbound JSON request so its actual encoded request content can be sized.",
 50:"Attempt up to max_retries + 1 times, counting the initial attempt separately from retries.",
 52:"Create/close a synchronous client for each attempt and prohibit following redirects. Timeout is not one overall workflow deadline.",
 58:"Stop for every status below 500 (including 429 and redirects) or at the final allowed attempt.",
 62:"Reject HTTPX client/server error responses. A 3xx is not is_error, so it can currently count as success despite redirects being unfollowed.",
 },
}

CALL_HINTS = {
 "create_engine":"create SQLAlchemy's database engine/connection manager",
 "sessionmaker":"build a factory for database Session objects",
 "Base.metadata.create_all":"create currently missing mapped database tables (not migrate existing schemas)",
 "Base.metadata.drop_all":"drop the fixture's isolated test tables during cleanup",
 "SessionLocal":"allocate a database unit-of-work session",
 "session.add":"stage an ORM object for persistence in the current session",
 "self.session.add":"stage an ORM object for persistence in this service's session",
 "db_session.add":"stage a fixture object in the isolated test database",
 "session.flush":"send pending SQL in the current transaction without committing",
 "self.session.flush":"flush pending SQL without a final commit",
 "db_session.flush":"flush the test transaction so IDs/config are available",
 "session.commit":"commit the current database transaction",
 "db_session.commit":"commit fixture setup within the isolated test database",
 "session.rollback":"undo the current database transaction on a propagated exception",
 "session.close":"release the Session's resources",
 "self.session.delete":"mark an ORM object for deletion; configured cascades may delete dependents",
 "session.get":"look up a mapped row by primary key",
 "self.session.get":"look up a mapped row by primary key in this session",
 "db_session.get":"look up the persisted fixture row by primary key",
 "httpx.get":"make a synchronous outbound HTTP GET (mocked where the test replaces it)",
 "httpx.post":"make a synchronous outbound HTTP POST (mocked where the test replaces it)",
 "httpx.Request":"construct an outbound HTTP request and serialize its configured body",
 "httpx.Client":"create a synchronous HTTP client whose context manager closes resources",
 "client.send":"send the prepared HTTPX request using this client",
 "client.post":"send POST through this client (TestClient in API tests, HTTPX in actions)",
 "client.get":"issue GET through this client (an in-process app request in API tests)",
 "client.put":"issue a replacement PUT request through the API test client",
 "client.delete":"issue DELETE through the API test client",
 "hmac.new":"compute a keyed message-authentication object over the supplied bytes",
 "hmac.compare_digest":"compare authentication strings while reducing timing leakage",
 "hashlib.sha256":"create a SHA-256 hash object, not reversible encryption",
 "secrets.token_urlsafe":"generate cryptographically strong random URL-safe text",
 "json.loads":"parse JSON bytes/text into Python data, raising for invalid syntax",
 "urlparse":"parse the URL into components such as scheme, hostname, and port",
 "urlencode":"encode a dictionary into URL query parameters",
 "socket.getaddrinfo":"resolve a hostname to possible network socket addresses",
 "ipaddress.ip_address":"parse an IPv4/IPv6 address for classification",
 "datetime.now":"capture the current time, using supplied UTC timezone where given",
 "timedelta":"construct a duration used in expiry arithmetic",
 "Fernet":"construct authenticated symmetric encryption with the configured key",
 "Fernet.generate_key":"generate a new secret Fernet key (fake/ephemeral test key here)",
 "EmailMessage":"construct a MIME-aware email message object",
 "formataddr":"format the display-name/address header safely using the email library",
 "base64.urlsafe_b64encode":"represent message bytes as URL-safe base64; this is encoding, not encryption",
 "Depends":"declare a FastAPI dependency to be resolved for each request context",
 "Header":"declare that FastAPI obtains this parameter from a request header",
 "Field":"declare Pydantic field defaults/validation metadata",
 "mapped_column":"declare a persisted SQLAlchemy column, constraints, and default behavior",
 "relationship":"declare ORM object navigation/cascade/order behavior",
 "ForeignKey":"declare a reference to the named table column",
 "Field.default_factory":"supply fresh mutable default values",
 "field":"configure a dataclass field, including its per-instance default factory",
 "super":"access parent class behavior (if used)",
 "isinstance":"perform an actual runtime type check",
 "len":"measure collection/string/serialized byte length as appropriate to its argument",
 "enumerate":"iterate as zero-based position/item pairs",
 "range":"produce the integer attempt indices without allocating every integer in a list",
 "all":"short-circuit False at the first false child; empty input yields True",
 "any":"short-circuit True at the first true child; empty input yields False",
 "list":"materialize an iterable into a list",
 "str":"convert a value to its string representation",
 "tuple":"construct a tuple",
 "Mock":"create a programmable test double rather than a real provider response",
 "MagicMock":"create a mock supporting magic methods such as context-manager entry",
 "patch":"temporarily replace the name used by code under test",
 "pytest.raises":"assert that the enclosed operation raises the expected exception",
 "monkeypatch.setattr":"temporarily replace an attribute for this test and restore it afterward",
 "assert_called_once":"assert the mock was invoked exactly once",
 "HTTPException":"construct an HTTP-level rejection with a status and user-facing detail",
 "RuntimeError":"construct an execution/integration failure exception",
 "ValueError":"construct an invalid value/configuration exception",
 "RedirectResponse":"construct an HTTP browser redirect rather than JSON data",
 "EngineResult":"construct the engine's final status/count/error data object",
 "Execution":"construct a persisted execution ORM object, not commit it yet",
 "Event":"construct a normalized input-event envelope",
 "ExecutionContext":"construct per-run state, keeping input event and mutable data separate",
 "RuntimeWorkflow":"compose hydrated trigger/condition/actions into a runtime workflow",
 "Workflow":"construct the imported Workflow class; the imports identify ORM versus runtime role",
 "AuthenticatedUser":"construct the immutable verified identity data object",
 "GmailService":"construct a session-bound Gmail integration service",
 "WorkflowService":"construct the use-case service with its database session",
 "WorkflowRepository":"construct the persistence helper using the supplied session",
 "HealthResponse":"construct/validate the health response fields",
 "WorkflowDetailResponse":"construct/validate editable workflow response data",
 "WorkflowCreate":"construct/validate workflow creation input",
 "ComponentConfig":"construct/validate a component's type/config envelope",
}


def label(node: ast.AST | None) -> str:
    return ast.unparse(node) if node is not None else "None"


def expression(node: ast.AST) -> str:
    """Explain an expression's operation, keeping original identifiers auditable."""
    raw = label(node)
    if isinstance(node, ast.Call):
        name = label(node.func)
        hint = CALL_HINTS.get(name)
        tail = name.rsplit(".", 1)[-1]
        if hint is None and name.endswith(".model_validate"):
            hint = "validate/serialize the input with this Pydantic response model; from_attributes reads ORM attributes"
        if hint is None:
            hint = {
              "get":"read a mapping key with a default (or call this object's get method as identified by the receiver)",
              "append":"mutate the receiver list by adding one item at its end",
              "setdefault":"get an existing dictionary entry or insert and return its default",
              "encode":"convert text into bytes using the default UTF-8 encoding",
              "decode":"convert bytes into text using the default UTF-8 encoding",
              "hexdigest":"format the digest as hexadecimal text",
              "encrypt":"encrypt token bytes with authenticated symmetric Fernet encryption",
              "decrypt":"authenticate and decrypt stored Fernet token bytes",
              "json":"decode this response's JSON body, potentially raising on invalid data",
              "filter":"add a SQL filter predicate to this ORM query",
              "filter_by":"add equality filters by named ORM attributes",
              "order_by":"specify SQL result ordering without sorting all rows in Python",
              "all":"materialize all matching query rows (not paginated)",
              "one_or_none":"require zero or one matching row and reject duplicates",
              "desc":"request descending SQL ordering by this column",
              "is_":"construct an SQL IS predicate rather than Python identity comparison",
              "replace":"replace the specified datetime field/timezone or string segment, according to receiver",
              "strip":"remove leading/trailing whitespace",
              "rstrip":"remove specified trailing characters from a string",
              "upper":"normalize a string to uppercase",
              "count":"count occurrences of the supplied substring",
              "fullmatch":"require the regex to match the entire candidate string",
              "evaluate":"invoke the selected Condition's boolean behavior polymorphically",
              "should_execute":"invoke the selected Trigger's match behavior polymorphically",
              "execute":"invoke this runtime engine/action operation; concrete dispatch depends on the receiver",
              "create":"construct a component through a factory, or call a service create use case as identified by receiver",
              "set_content":"add a plain text MIME body to the email message",
              "add_alternative":"add the optional HTML MIME alternative",
              "as_bytes":"serialize MIME headers/body into wire-format bytes",
              "clear":"remove temporary test dependency overrides or collection entries",
              "send":"invoke the receiver's delivery/send operation",
              "hash_state":"compute the SHA-256 comparison hash of an OAuth state string",
              "oauth_url":"construct Google's consent URL from settings and state",
              "exchange_code":"exchange a one-time authorization code for tokens and expiry",
              "profile":"look up the authorized Google account email",
              "save_connection":"encrypt and store this user's Gmail tokens",
              "disconnect":"delete the user's local Gmail connection",
              "connection":"look up the user's stored Gmail connection without returning token values to the frontend",
              "load_runtime":"hydrate persisted configuration into a separate runtime composition",
              "run_event":"run a normalized event through hydration/engine/history persistence synchronously",
              "run_manual":"wrap a request payload in a normalized manual Event and run it",
              "_validate_runtime":"construct supported component objects to validate configuration",
              "assert_called_once":"assert this test mock was called once",
            }.get(tail)
        return (hint + ": `" + raw + "`") if hint else "call `" + name + "` with the displayed positional/named arguments: `" + raw + "`"
    if isinstance(node, ast.Compare):
        return "evaluate the comparison/membership/identity test `" + raw + "`; this produces the branch/assertion's truth value"
    if isinstance(node, ast.BoolOp):
        return "evaluate the short-circuit boolean expression `" + raw + "`; later terms run only when needed"
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return "negate the truth value of `" + label(node.operand) + "`"
    if isinstance(node, ast.ListComp):
        return "construct a new list by applying the displayed expression for each item in the comprehension: `" + raw + "`"
    if isinstance(node, ast.GeneratorExp):
        return "lazily yield the displayed expression for each item: `" + raw + "`"
    if isinstance(node, ast.IfExp):
        return "choose `" + label(node.body) + "` when `" + label(node.test) + "` is true, otherwise `" + label(node.orelse) + "`"
    if isinstance(node, ast.Dict):
        return "construct a dictionary mapping the displayed keys to values: `" + raw + "`"
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return "construct a " + type(node).__name__.lower() + " containing the displayed values: `" + raw + "`"
    if isinstance(node, ast.Constant):
        return "use literal value `" + raw + "` (" + type(node.value).__name__ + ")"
    if isinstance(node, ast.Attribute):
        return "read attribute `" + node.attr + "` from `" + label(node.value) + "`"
    if isinstance(node, ast.Subscript):
        return "look up/index `" + label(node.value) + "` using `" + label(node.slice) + "`; missing keys/out-of-range indices can raise"
    if isinstance(node, ast.Lambda):
        return "define a deferred anonymous function `" + raw + "`; its body runs when called"
    if isinstance(node, ast.JoinedStr):
        return "construct an f-string, interpolating expressions at runtime: `" + raw + "`"
    if isinstance(node, ast.BinOp):
        return "compute `" + raw + "` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values"
    if isinstance(node, ast.Await):
        return "await coroutine `" + label(node.value) + "`, yielding this coroutine until the asynchronous operation completes"
    return "read/evaluate `" + raw + "`"


def statement(node: ast.AST, path: str) -> str:
    if isinstance(node, ast.ImportFrom):
        names = ", ".join(x.name + (" as " + x.asname if x.asname else "") for x in node.names)
        return f"Import {names} from `{node.module}`. Imported names become available in this module; aliases distinguish roles where used."
    if isinstance(node, ast.Import):
        return "Import module(s) " + ", ".join("`" + x.name + "`" for x in node.names) + ". Top-level module code runs on first import."
    if isinstance(node, ast.ClassDef):
        bases = ", ".join(label(x) for x in node.bases)
        return f"Define class `{node.name}`" + (f" inheriting `{bases}`" if bases else "") + ". The indented suite defines its attributes/methods; defining a class does not instantiate it."
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = label(node.args)
        extra = TEST_PURPOSES.get(node.name, "")
        return f"Define {'async ' if isinstance(node, ast.AsyncFunctionDef) else ''}function/method `{node.name}({args})`" + (f" with intended return type `{label(node.returns)}`" if node.returns else "") + ". " + extra + (" `self` is supplied by an ordinary bound method call." if node.args.args and node.args.args[0].arg == "self" else "")
    if isinstance(node, ast.Assign):
        targets = ", ".join(label(x) for x in node.targets)
        return f"Assign to `{targets}`: " + expression(node.value) + ". Assignment stores a value/reference; it is not an equality test."
    if isinstance(node, ast.AnnAssign):
        text = f"Declare `{label(node.target)}` with intended type `{label(node.annotation)}`"
        if isinstance(node.value, ast.Call) and label(node.value.func) == "mapped_column":
            details=[]
            for arg in node.value.args:
                if isinstance(arg,ast.Call) and label(arg.func)=="ForeignKey":
                    details.append("foreign-key reference to `"+str(ast.literal_eval(arg.args[0]))+"`")
                elif isinstance(arg,ast.Call) and label(arg.func)=="String":
                    details.append("string column with declared maximum length "+label(arg.args[0])+" (exact enforcement depends on the database)")
                elif isinstance(arg,ast.Call) and label(arg.func)=="DateTime":
                    details.append("timestamp column requesting timezone support")
                elif label(arg)=="JSON":details.append("JSON configuration/data column; JSON storage does not automatically encrypt its values")
                elif label(arg)=="Text":details.append("text column suitable for longer values/ciphertext")
                elif label(arg)=="Integer":details.append("integer column")
                else:details.append("SQL type/constraint `"+label(arg)+"`")
            flags={"primary_key":"identifies a row uniquely", "unique":"disallows duplicate non-null values", "nullable":"controls whether SQL NULL is permitted", "default":"supplies an application-side insert default; a callable is invoked when needed", "server_default":"supplies a database-side insert default", "onupdate":"supplies a value when this row is updated"}
            for kw in node.value.keywords:details.append(f"`{kw.arg}={label(kw.value)}` {flags.get(kw.arg,'configures the column')}")
            return text+" and map it to persistence: "+"; ".join(details)+". SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column."
        if isinstance(node.value, ast.Call) and label(node.value.func)=="relationship":
            details=[]
            for kw in node.value.keywords:
                detail={"back_populates":"names the reverse ORM relationship", "uselist":"False requests one related object rather than a collection", "cascade":"all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent", "order_by":"orders loaded related actions by their persisted position"}.get(kw.arg,"configures this object relationship")
                details.append(f"`{kw.arg}={label(kw.value)}` {detail}")
            return text+" as ORM object navigation, not another physical column. "+("; ".join(details)+"." if details else "SQLAlchemy infers the relationship from mapped types/foreign keys.")
        return text + (" and initialize it: " + expression(node.value) if node.value else "; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class") + "."
    if isinstance(node, ast.Return):
        return ("Return from this function: " + expression(node.value) if node.value else "Return immediately without a value (None), skipping the remaining function body") + "."
    if isinstance(node, ast.If):
        return "Enter the following indented branch only if you " + expression(node.test) + "."
    if isinstance(node, ast.For):
        return f"Iterate over `{label(node.iter)}`, binding each item/pair to `{label(node.target)}`. The indented body runs once per item unless it returns/raises/breaks."
    if isinstance(node, ast.Try):
        return "Begin a protected block. Matching except clauses handle raised exceptions; finally performs cleanup regardless of success/failure."
    if isinstance(node, ast.ExceptHandler):
        return "Catch " + ("`" + label(node.type) + "`" if node.type else "the raised exception") + (" as `" + node.name + "`" if node.name else "") + "; execute this error branch instead of continuing the failed statement."
    if isinstance(node, (ast.With, ast.AsyncWith)):
        return "Enter context manager(s): " + "; ".join(expression(x.context_expr) + (" bound as `" + label(x.optional_vars) + "`" if x.optional_vars else "") for x in node.items) + ". Exit cleanup also runs when the body raises."
    if isinstance(node, ast.Raise):
        return "Raise " + (expression(node.exc) if node.exc else "the currently handled exception again") + ("; `from` controls exception cause/chaining: `" + label(node.cause) + "`" if node.cause else "") + ". Normal execution at this point stops."
    if isinstance(node, ast.Assert):
        return "Test assertion: " + expression(node.test) + ". If false, pytest reports a failure; it is evidence for this property, not every possible behavior."
    if isinstance(node, ast.AugAssign):
        return f"Update `{label(node.target)}` with `{label(node)}`; here the completed-action count increases only after a normal action return."
    if isinstance(node, ast.Expr):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return "Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself."
        if isinstance(node.value, ast.Yield):
            return "Yield " + ("`" + label(node.value.value) + "` to the dependency/fixture caller" if node.value.value else "control to the running application") + "; code after yield is resumed during normal lifecycle/cleanup."
        return "Perform the expression for its effect: " + expression(node.value) + "."
    if isinstance(node, ast.Pass):
        return "Empty placeholder body required by Python syntax; SQLAlchemy's base class supplies inherited behavior here."
    if isinstance(node, ast.Continue):
        return "Skip the rest of this loop iteration and move to the next item/attempt."
    if isinstance(node, ast.Break):
        return "Leave the nearest loop immediately; execution continues after the loop."
    return "Statement syntax: `" + label(node) + "`."


def python_notes(path: str, lines: list[str]) -> dict[int, str]:
    tree = ast.parse("\n".join(lines))
    nodes = [n for n in ast.walk(tree) if isinstance(n, (ast.stmt, ast.ExceptHandler)) and hasattr(n, "lineno")]
    notes = {}
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s:
            notes[i] = "Blank line: visual separation only; Python block membership is determined by indentation of actual statements."
            continue
        if i in EXACT.get(path, {}):
            notes[i] = EXACT[path][i]
            continue
        if s.startswith("#"):
            notes[i] = "Comment for maintainers/tooling, not executable Python: " + s[1:].strip()
            continue
        if s.startswith("@"):
            notes[i] = {
             "@staticmethod":"Decorate the following factory/helper so it does not receive an implicit self instance argument.",
             "@abstractmethod":"Mark the next method as required by the ABC mechanism before a subclass can normally be instantiated.",
             "@dataclass":"Generate dataclass initialization/representation/equality from annotated fields.",
             "@dataclass(frozen=True)":"Generate a dataclass and disallow ordinary field reassignment after initialization (shallow protection).",
             "@asynccontextmanager":"Transform the following async generator into a lifespan context manager with setup before yield and cleanup afterward.",
            }.get(s, "Apply/register the following definition with decorator `" + s + "`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.")
            continue
        if s in ("else:", "finally:", "try:"):
            notes[i] = {"else:":"Alternative branch when the preceding if condition is false, or the try completed without its expected exception (inspect the enclosing block).", "finally:":"Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.", "try:":"Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup."}[s]
            continue
        candidates = [n for n in nodes if n.lineno <= i <= getattr(n, "end_lineno", n.lineno)]
        if not candidates:
            notes[i] = "Continue the surrounding declaration/import; punctuation groups its arguments/items without introducing another runtime operation."
            continue
        n = min(candidates, key=lambda n: (getattr(n, "end_lineno", n.lineno)-n.lineno, -n.lineno))
        if i == n.lineno:
            notes[i] = statement(n, path)
        elif s in (")", "]", "}", "),", "],", "},", ") -> None:"):
            notes[i] = f"Close the grouped expression/declaration introduced at L{n.lineno}; delimiters/commas complete the same statement rather than execute a separate operation."
        elif isinstance(n, ast.ImportFrom):
            notes[i] = f"Continue the parenthesized import from `{n.module}` with name(s) `{s.rstrip(',')}`."
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and i < (n.body[0].lineno if n.body else i):
            notes[i] = "Continue the function signature: `" + s + "`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body."
        else:
            part = s.rstrip(",")
            notes[i] = f"Continue the statement starting at L{n.lineno} with `{part}`. " + statement(n, path)
    return notes


def ts_notes(path: str, lines: list[str]) -> dict[int, str]:
    result = {}
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s:
            result[i] = "Blank line: separates related declarations/statements; no runtime operation."
        elif path.endswith("App.tsx") and i in APP_NOTES:
            result[i] = APP_NOTES[i]
        elif path.endswith("App.tsx") and "= useState" in s:
            m = re.search(r"const \[(\w+), (\w+)\] = (.*)", s)
            result[i] = f"Create React state `{m[1]}` for {STATE_MEANINGS[m[1]]}; destructuring also names its setter `{m[2]}`. `{m[3]}` declares initial state and any explicit generic type. Calling the setter requests another render."
        elif path.endswith("services/api.ts") and i in API_NOTES:
            result[i] = API_NOTES[i]
        elif s.startswith("import"):
            result[i] = "Import the displayed module/export into this ES module" + (" as compile-time-only types (erased from browser code)." if s.startswith("import type") else ". Relative paths refer to project files; package names resolve installed dependencies.")
        elif path.endswith("main.tsx"):
            result[i] = {6:"Find the HTML root and create a React DOM root, then call render. `!` is a non-null assertion, not a runtime existence check.",7:"Wrap descendants in StrictMode for extra development lifecycle checks.",8:"Render the App function component with JSX; this is not an immediate ordinary function call written as App().",9:"Close the StrictMode element and separate render arguments with the trailing comma.",10:"Close the render call."}.get(i,"Complete the root rendering expression.")
        elif path.endswith("lib/supabase.ts"):
            result[i] = {3:"Read the public Supabase URL embedded by Vite from exposed build environment.",4:"Read the public Supabase anonymous/publishable key; a privileged service-role key must never be used here.",6:"Export a real client only when both values are truthy; otherwise export null so callers can guard missing configuration."}.get(i,"Separate public client configuration declarations.")
        elif re.match(r"\w+: (string|boolean|Record|Component|Workflow)",s):
            key,kind=s.split(":",1)
            result[i]=f"Declare compile-time property `{key}` with type `{kind.strip()}`. This describes expected shape; it does not create a runtime validator."
        elif s.startswith("//"):
            result[i]="Comment/reference for developers; not executed: "+s[2:].strip()
        elif s.startswith("export default defineConfig"):
            result[i]="Export Vite's configuration using defineConfig for tool typing/conventions."
        elif "plugins: [react()]" in s:
            result[i]="Enable the React Vite plugin; this is build/development integration, not a backend route."
        elif s.startswith("} catch"):
            result[i]="End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely."
        elif s.startswith("} finally"):
            result[i]="Begin unconditional cleanup, used to clear busy after either success or error."
        elif s=="try {":
            result[i]="Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally."
        elif s=="return":
            result[i]="Exit this handler without saving/executing the remaining operations."
        elif s.startswith("</"):
            result[i]="Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation."
        elif s in ("}", "})", "})()", "},", "})", ")", "))", "]", "})", "})", "}", "})", "}, []):", "})") or re.fullmatch(r"[\}\]\),;]+",s):
            result[i]="Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line."
        else:
            result[i]="Continue the surrounding typed module/configuration expression: `"+s+"`. The exact operation is introduced by the preceding function/object declaration; punctuation preserves that grouping."
    return result


CSS_MEANINGS = {
 "font-family":"choose an ordered font fallback stack; listing a font does not download it",
 "color":"set foreground/text color", "background":"set background shorthand", "background-color":"set background color",
 "font-synthesis":"control whether the browser synthesizes missing font styles", "text-rendering":"provide text rendering hints",
 "box-sizing":"choose whether declared dimensions include border/padding", "margin":"set outer spacing (one to four sides or auto centering)",
 "margin-top":"set space above", "margin-bottom":"set space below", "margin-right":"set space to the right",
 "min-width":"set a lower bound on width", "width":"set element width", "max-width":"cap element width",
 "height":"set element height", "min-height":"set a lower bound on height", "font":"inherit or set the composite font style",
 "border":"set border width/style/color", "border-radius":"round the corners", "padding":"set internal spacing",
 "cursor":"select pointer feedback", "opacity":"set overall transparency", "display":"choose grid/flex/block display behavior",
 "place-items":"align items in both relevant axes", "place-content":"align the layout's content in both axes",
 "justify-content":"distribute/align items along the layout's main/inline axis", "align-items":"align items on the cross/block axis",
 "border-bottom":"set the lower border", "border-top":"set the upper border", "border-right":"set the right border",
 "box-shadow":"draw an outer shadow without changing layout dimensions", "font-size":"set text size",
 "line-height":"set spacing/height of text lines", "text-transform":"change displayed capitalization",
 "letter-spacing":"set spacing between characters", "font-weight":"select font weight",
 "gap":"set space between grid/flex items", "grid-template-columns":"define grid column tracks",
 "flex":"set the grow/shrink/basis shorthand", "flex-grow":"allow expansion within a flex container",
 "flex-wrap":"allow flex items to wrap", "flex-direction":"choose row/column flow",
 "text-align":"align inline text inside its box", "outline":"draw a focus/selection outline outside the border",
 "outline-offset":"move an outline away from the box", "overflow-wrap":"allow long text such as URLs to break",
 "transition":"animate changes of named properties over a duration", "position":"choose normal/relative/absolute positioning",
 "inset-inline":"set logical left/right offsets according to writing direction", "z-index":"set stacking priority within applicable stacking contexts",
 "top":"set top offset for positioned content", "left":"set left offset", "right":"set right offset",
 "transform":"apply a visual transformation (does not redefine normal document layout)",
 "list-style":"control list markers", "text-decoration":"set underline/other text decoration",
 "content":"generate pseudo-element content", "border-color":"set border colors", "border-left-color":"set left border color",
 "border-right-color":"set right border color",
}


def css_notes(lines: list[str]) -> dict[int,str]:
    out={}
    for i,line in enumerate(lines,1):
        s=line.strip()
        if not s: out[i]="Blank formatting line; no CSS rule."
        elif s=="}": out[i]="Close the current selector or media-query block."
        else:
            props=re.findall(r"([a-z][a-z-]*)\s*:\s*([^;{}]+)(?:;|(?=}))",s)
            details=[f"`{k}: {v.strip()}`: {CSS_MEANINGS.get(k,'set this CSS property according to the displayed value')}" for k,v in props if k!="max-width" or not s.startswith("@media")]
            if s.startswith("@media"):
                prefix="Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. "
            elif "{" in s:
                selector=s.split("{",1)[0]
                prefix=f"Selector `{selector}` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. "
            elif s.endswith(","):
                prefix="Continue the comma-separated selector group; the next selector shares the rule. "
            elif s.endswith("{"):
                prefix="Begin a nested rule. "
            else: prefix="Continue this style rule. "
            out[i]=prefix+("; ".join(details)+"." if details else "The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.")
    return out


CONFIG_KEYS = {
 "name":"package identifier", "private":"prevent accidental npm publication", "version":"package metadata version, not the React version", "type":"ES module interpretation when module",
 "scripts":"named npm commands", "dev":"run the Vite development server", "build":"type-check referenced TS projects, then build only if that succeeds", "lint":"run the installed Oxlint checker", "preview":"serve the already built frontend locally",
 "dependencies":"packages required by runtime application imports", "devDependencies":"tooling/type packages used while developing/building",
 "files":"root file list; empty here because projects are referenced below", "references":"TypeScript project references used by tsc -b", "path":"relative referenced project configuration",
 "compilerOptions":"TypeScript compiler settings", "tsBuildInfoFile":"location for incremental build metadata", "target":"modern JavaScript output/type-check target", "lib":"ambient API declarations to include, such as DOM", "module":"module interpretation/output target", "types":"ambient declaration packages, not runtime imports",
 "allowArbitraryExtensions":"permit arbitrary-extension imports when declaration resolution permits them", "skipLibCheck":"skip checking dependency declaration files, not all application checking", "moduleResolution":"how the compiler resolves imports", "allowImportingTsExtensions":"allow imports naming .ts/.tsx extensions with compatible emit settings", "verbatimModuleSyntax":"preserve ordinary module syntax while removing type-only imports", "moduleDetection":"treat files as modules according to force setting", "noEmit":"type-check without emitting JavaScript; Vite owns the asset build", "jsx":"use the modern React JSX transform", "noUnusedLocals":"report unused local declarations", "noUnusedParameters":"report unused parameters subject to compiler conventions", "erasableSyntaxOnly":"restrict TS features to forms erasable without runtime language transformation", "noFallthroughCasesInSwitch":"report accidental switch case fallthrough", "include":"source paths included in this project",
 "$schema":"editor/schema reference for configuration validation", "plugins":"enable named linter plugins", "rules":"configure individual linter rules", "react/rules-of-hooks":"enforce valid React hook call placement", "react/only-export-components":"warn about exports affecting fast refresh conventions", "allowConstantExport":"permit constant exports under this rule",
}


def config_notes(path: str,lines:list[str])->dict[int,str]:
    out={}
    for i,line in enumerate(lines,1):
        s=line.strip()
        if not s: out[i]="Blank formatting line."
        elif path.endswith("requirements.txt"):
            out[i]="Declare install requirement `"+s+"`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative."
        elif path.endswith(".ini"):
            out[i]={"[pytest]":"Start pytest's configuration section.","pythonpath = .":"Add the configured backend directory to imports for app package resolution.","testpaths = tests":"Use tests as the normal test discovery directory."}.get(s,"Configure pytest using the displayed key/value.")
        elif path.endswith(".html"):
            out[i]={1:"Declare HTML5 parsing mode.",2:"Start the HTML document and identify English as its language.",3:"Start metadata rather than visible body content.",4:"Declare UTF-8 text encoding.",5:"Link the public SVG favicon asset; it is a UI icon, not workflow execution logic.",6:"Use device width and initial scale for responsive mobile rendering.",7:"Set the browser tab title; the current scaffold title is frontend.",8:"Close document metadata.",9:"Start visible/document body content.",10:"Provide the root DOM mount point into which React renders App.",11:"Load main.tsx as an ES module through Vite's development/build handling.",12:"Close body.",13:"Close HTML document."}[i]
        elif path.endswith(".yml"):
            notes={1:"Name this GitHub Actions workflow in the repository UI.",3:"Start event trigger definitions.",4:"Listen for externally initiated repository_dispatch events.",5:"Only match event_type flowforge; a different FlowForge event type will not start this job.",7:"Declare workflow token permissions.",8:"Allow the Actions runtime token to create repository issues; this is not the external dispatch token.",10:"Define jobs executed after a matching dispatch.",11:"Name the single issue-creation job.",12:"Choose a GitHub-hosted Ubuntu runner; no workflow code is running inside FlowForge's backend process.",13:"Start ordered job steps.",14:"Name the issue-creation step.",15:"Declare environment variables for the step rather than embedding payload data directly as shell source.",16:"Expose GitHub's short-lived job token as GH_TOKEN for gh CLI authentication; this placeholder is not a literal credential value.",17:"Pass the dispatched source field into a quoted shell environment variable.",18:"Serialize the client payload to JSON text and pass it through an environment variable.",19:"Use a YAML literal multiline scalar for the shell commands below.",20:"Invoke gh issue create; backslash continues the shell command to the next line.",21:"Target the current GitHub repository, quoting the shell variable expansion.",22:"Set a fixed visible issue title.",23:"Build an issue body with printf using payload variables as data arguments, then pass the resulting string as one quoted --body argument. Command substitution executes printf; it does not evaluate payload text as new shell code."}
            out[i]=notes[i]
        else:
            m=re.search(r'"([^\"]+)"\s*:',s)
            if m:
                k=m[1]
                if k.startswith("@") or k in {"react","react-dom","typescript","vite","oxlint"}:
                    out[i]=f"Declare `{k}` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20."
                else: out[i]=f"Set `{k}`: {CONFIG_KEYS.get(k,'the displayed configuration value controls the containing tool/package option')}."
            elif s.startswith("/*") or s.startswith("//"):out[i]="JSON-with-comments developer note, not an executable operation. TypeScript config accepts comments even though strict JSON does not."
            else:out[i]="Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries."
    return out


def source_paths()->list[Path]:
    backend=sorted((ROOT/"backend/app").rglob("*.py"))
    tests=sorted((ROOT/"backend/tests").glob("*.py"))
    front=sorted(p for p in (ROOT/"frontend/src").rglob("*") if p.suffix in {".ts",".tsx",".css"})
    extras=["backend/requirements.txt","backend/pytest.ini","frontend/package.json","frontend/index.html","frontend/vite.config.ts","frontend/tsconfig.json","frontend/tsconfig.app.json","frontend/tsconfig.node.json","frontend/.oxlintrc.json",".github/workflows/flowforge-dispatch.yml"]
    return backend+tests+front+[ROOT/p for p in extras]


def generate_appendix()->dict:
    paths=source_paths()
    intro=["# FlowForge: complete line-by-line source companion", "", "Snapshot: 31 October 2026. Read beside FlowForge-Master-Guide.md. This appendix is an explanation of the checked-in implementation, including its limitations; no application code was changed.", "", "Every selected file appears with its original numbered source and one note for every physical line. Blank lines are explicitly identified as formatting. Start with each file's purpose note, read the source, then use the L-number notes. Long expressions continue over several physical lines: continuation notes identify the originating statement rather than pretending punctuation is an independent operation.", "", "Python notes use syntax-aware parsing; file-specific and critical-line explanations add behavior and caveats. TypeScript/JSX notes explain the state, callbacks, guards, and rendered controls. CSS notes explain selectors and individual properties. This source snapshot is checked by SHA-256 fingerprints; later code edits can invalidate line references.", "", "## Navigation", ""]
    for p in paths:
        rel=p.relative_to(ROOT).as_posix();anchor=re.sub(r"[^a-z0-9-]","",rel.lower().replace("/","-").replace(".",""))
        intro.append(f"- [{rel}](#{anchor})")
    stats={"snapshot":"2026-10-31","files":[],"total_lines":0,"nonblank_lines":0}
    out=intro
    for p in paths:
        rel=p.relative_to(ROOT).as_posix();data=p.read_bytes();lines=data.decode("utf-8-sig").splitlines()
        digest=hashlib.sha256(data).hexdigest()
        notes=python_notes(rel,lines) if p.suffix==".py" else css_notes(lines) if p.suffix==".css" else ts_notes(rel,lines) if p.suffix in {".ts",".tsx"} else config_notes(rel,lines)
        assert set(notes)==set(range(1,len(lines)+1)),rel
        purpose=FILE_NOTES.get(rel)
        if purpose is None:
            if "/tests/" in rel: purpose="Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior."
            elif p.name=="__init__.py":purpose="Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security."
            elif "tsconfig" in p.name:purpose="TypeScript project configuration. Root references split browser and tooling concerns. No explicit strict:true is enabled in these configs. The build uses tsc -b to follow references."
            else:raise AssertionError("Missing file purpose: "+rel)
        anchor=re.sub(r"[^a-z0-9-]","",rel.lower().replace("/","-").replace(".",""))
        out.extend(["",f'<a id="{anchor}"></a>',f"## {rel}","",purpose,"",f"Source fingerprint: `{digest}`. Physical lines: {len(lines)}.","","### Numbered source","", "```"+({".py":"python",".ts":"typescript",".tsx":"tsx",".css":"css",".json":"json",".html":"html",".yml":"yaml"}.get(p.suffix,"text"))])
        out.extend(f"{i:04d} | {line}" for i,line in enumerate(lines,1))
        out.extend(["```","","### Every-line explanation",""])
        for i in range(1,len(lines)+1):out.extend([f"**L{i:04d}.** {notes[i]}",""])
        stats["files"].append({"path":rel,"sha256":digest,"lines":len(lines),"nonblank":sum(bool(s.strip()) for s in lines),"annotated_lines":len(notes)})
        stats["total_lines"]+=len(lines);stats["nonblank_lines"]+=sum(bool(s.strip()) for s in lines)
    out.extend(["## Non-code assets and deliberate exclusions","","frontend/src/assets/hero.png is a raster image; react.svg/vite.svg are starter vector assets. They are not imported by the current App. frontend/public/favicon.svg is linked by index.html. frontend/public/icons.svg is a static vector asset without workflow execution behavior. Binary/image data and SVG path coordinates are not Python/TypeScript algorithms and are not copied here.","","The coverage set deliberately excludes actual .env files, database files, credentials, private logs, dependency packages, generated dist files, lockfile entries, and agent/tool configuration. Their exclusion does not mean hidden implementation features were inferred. The master guide explains public configuration variable names and deployment concepts without reading secret values.","",f"Coverage total: {len(paths)} files; {stats['total_lines']} physical lines; {stats['nonblank_lines']} nonblank lines. Each selected physical line has exactly one explanatory note."])
    (DEST/"FlowForge-Line-by-Line.md").write_text("\n".join(out)+"\n",encoding="utf-8")
    (DEST/"resources/source-coverage.json").write_text(json.dumps(stats,indent=2)+"\n",encoding="utf-8")
    return stats


def create_pdf()->Path:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, CondPageBreak, Table, TableStyle, Preformatted
    from reportlab.platypus.tableofcontents import TableOfContents

    fonts=Path("C:/Windows/Fonts")
    for name,file in [("Study","segoeui.ttf"),("Study-Bold","segoeuib.ttf"),("Study-Italic","segoeuii.ttf"),("Study-Mono","consola.ttf")]:
        pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
    pdfmetrics.registerFontFamily("Study",normal="Study",bold="Study-Bold",italic="Study-Italic",boldItalic="Study-Bold")
    navy=colors.HexColor("#10243A");blue=colors.HexColor("#1565A6");muted=colors.HexColor("#56667A");light=colors.HexColor("#EAF1F7")
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name="BodyStudy",fontName="Study",fontSize=9.5,leading=14,spaceAfter=7,textColor=navy))
    styles.add(ParagraphStyle(name="ChapterStudy",fontName="Study-Bold",fontSize=19,leading=24,spaceBefore=20,spaceAfter=14,textColor=navy,keepWithNext=True))
    styles.add(ParagraphStyle(name="SubStudy",fontName="Study-Bold",fontSize=12,leading=16,spaceBefore=12,spaceAfter=7,textColor=blue,keepWithNext=True))
    styles.add(ParagraphStyle(name="SmallStudy",fontName="Study",fontSize=8,leading=11,spaceAfter=4,textColor=muted))
    styles.add(ParagraphStyle(name="TableStudy",fontName="Study",fontSize=8,leading=11,textColor=navy))
    styles.add(ParagraphStyle(name="TableHeadStudy",parent=styles["TableStudy"],fontName="Study-Bold",textColor=colors.white))
    styles.add(ParagraphStyle(name="CodeStudy",fontName="Study-Mono",fontSize=7.2,leading=10,spaceBefore=5,spaceAfter=9,backColor=light,borderPadding=8))
    styles.add(ParagraphStyle(name="CoverStudy",fontName="Study-Bold",fontSize=38,leading=43,textColor=navy,spaceAfter=18))
    styles.add(ParagraphStyle(name="DeckStudy",fontName="Study",fontSize=16,leading=23,textColor=blue,spaceAfter=18))
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle(name="TOCStudy",fontName="Study",fontSize=9,leading=14,leftIndent=0,firstLineIndent=0,spaceBefore=4,textColor=navy)]
    PDF_DIR.mkdir(parents=True,exist_ok=True)
    output=PDF_DIR/"FlowForge-Viva-Master-Guide.pdf"

    class StudyDoc(BaseDocTemplate):
        def afterFlowable(self,flowable):
            if isinstance(flowable,Paragraph) and flowable.style.name=="ChapterStudy":
                title=flowable.getPlainText();key="chapter-"+re.sub(r"\W+","-",title)
                self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,level=0,closed=False)
                if not title.startswith("Contents"):
                    self.notify("TOCEntry",(0,title,self.page,key))

    def page_frame(canvas,doc):
        canvas.saveState();w,h=doc.pagesize
        if doc.page>1:
            canvas.setStrokeColor(colors.HexColor("#C9D6E2"));canvas.line(43,h-36,w-43,h-36)
            canvas.setFont("Study",8);canvas.setFillColor(muted);canvas.drawString(43,h-28,"FLOWFORGE  /  VIVA MASTER GUIDE")
        canvas.setFont("Study",8);canvas.setFillColor(muted);canvas.drawString(43,27,"Source-based study edition  |  31 October 2026")
        canvas.drawRightString(w-43,27,str(doc.page));canvas.restoreState()

    doc=StudyDoc(str(output),pagesize=(595.28,841.89),rightMargin=43,leftMargin=43,topMargin=52,bottomMargin=45,title="FlowForge Viva Master Guide",author="FlowForge project study materials")
    doc.addPageTemplates(PageTemplate(id="study",frames=[Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id="body",leftPadding=0,bottomPadding=0,rightPadding=0,topPadding=0)],onPage=page_frame))

    def inline(text):
        text=text.replace("\u2014"," - ").replace("\u2013","-").replace("\u2011","-").replace("\\|","|")
        text=re.sub(r"`([^`]+)`",lambda m:"<font name='Study-Mono'>"+html.escape(m[1])+"</font>",text)
        # Protect generated code font tags while escaping ordinary paragraph text.
        protected=[]
        def hold(m):protected.append(m[0]);return f"ZZCODE{len(protected)-1}ZZ"
        text=re.sub(r"<font name='Study-Mono'>.*?</font>",hold,text)
        text=html.escape(text)
        text=re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)",lambda m:f'<link href="{html.escape(html.unescape(m[2]),quote=True)}" color="#1565A6">{m[1]}</link>',text)
        text=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",text)
        for i,p in enumerate(protected):text=text.replace(f"ZZCODE{i}ZZ",p)
        return text

    story=[Spacer(1,75),Paragraph("FLOWFORGE",styles["CoverStudy"]),Paragraph("The complete viva<br/>master guide",styles["CoverStudy"]),Paragraph("From your first web concepts to the engine's design, source behavior, and difficult follow-up questions.",styles["DeckStudy"]),Spacer(1,20),Paragraph("BEGINNER FRIENDLY  /  SOURCE VERIFIED  /  100 VIVA QUESTIONS",styles["SmallStudy"]),Spacer(1,18),Paragraph("28 chapters covering architecture, Python, OOP, APIs, databases, authentication, React, TypeScript, integrations, security, tests, demonstrations, and rapid revision.",styles["BodyStudy"]),Paragraph("Read alongside the separate line-by-line source companion. Implementation facts, planned capabilities, test evidence, and known limitations are distinguished throughout.",styles["BodyStudy"]),Spacer(1,25),Paragraph("Prepared from the repository snapshot of 31 October 2026.<br/>No production deployment verification is claimed.",styles["SmallStudy"]),PageBreak(),Paragraph("Contents",styles["ChapterStudy"]),toc,PageBreak()]
    lines=(DEST/"FlowForge-Master-Guide.md").read_text(encoding="utf-8").splitlines();i=0;first=True
    while i<len(lines):
        line=lines[i]
        if line.startswith("# "):i+=1;continue
        if not line.strip():i+=1;continue
        if line.startswith("## "):
            if not first:story.append(CondPageBreak(doc.height * .72))
            first=False;story.append(Paragraph(inline(line[3:]),styles["ChapterStudy"]));i+=1;continue
        if line.startswith("### "):
            story.append(Paragraph(inline(line[4:]),styles["SubStudy"]));i+=1;continue
        if line.startswith("```"):
            code=[];i+=1
            while i<len(lines) and not lines[i].startswith("```"):
                for s in textwrap.wrap(lines[i],width=91,replace_whitespace=False,drop_whitespace=False,break_long_words=True,break_on_hyphens=False) or [""]:code.append(s)
                i+=1
            story.append(Preformatted("\n".join(code),styles["CodeStudy"]));i+=1;continue
        if line.startswith("|"):
            rows=[]
            while i<len(lines) and lines[i].startswith("|"):
                cells=[c.strip() for c in re.split(r"(?<!\\)\|",lines[i].strip().strip("|"))]
                if not all(re.fullmatch(r"[: -]+",c) for c in cells):rows.append(cells)
                i+=1
            count=max(map(len,rows));ratios={2:[.29,.71],3:[.24,.36,.40],4:[.18,.13,.34,.35]}.get(count,[1/count]*count)
            data=[[Paragraph(inline(c),styles["TableHeadStudy"] if r==0 else styles["TableStudy"]) for c in row] for r,row in enumerate(rows)]
            table=Table(data,colWidths=[doc.width*x for x in ratios],repeatRows=1,hAlign="LEFT")
            table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),navy),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,light]),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),("LINEBELOW",(0,0),(-1,0),.5,navy)]))
            story.extend([table,Spacer(1,10)]);continue
        bullet=re.match(r"^(\d+\.|-) (.*)",line)
        if bullet:
            marker=bullet[1];body=bullet[2]
            style=ParagraphStyle(name="ListStudy",parent=styles["BodyStudy"],leftIndent=17,firstLineIndent=-14)
            story.append(Paragraph(inline(marker+" "+body),style));i+=1;continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r"^(#|\||```|\d+\. |\- )",lines[i]):paragraph.append(lines[i]);i+=1
        story.append(Paragraph(inline(" ".join(paragraph)),styles["BodyStudy"]))
    doc.multiBuild(story)
    return output


if __name__=="__main__":
    stats=generate_appendix()
    output=create_pdf()
    from pypdf import PdfReader
    reader=PdfReader(str(output))
    full="\n".join(p.extract_text() or "" for p in reader.pages)
    for expected in ("100. Can you handle any possible question?","28. Source map", "28 passed", "1. How to study"):
        assert expected in full, "Missing PDF content: "+expected
    assert all((p.extract_text() or "").strip() for p in reader.pages),"Unexpected blank PDF page"
    result={"covered_files":len(stats["files"]),"physical_lines":stats["total_lines"],"nonblank_lines":stats["nonblank_lines"],"master_words":len((DEST/"FlowForge-Master-Guide.md").read_text(encoding="utf-8").split()),"appendix_words":len((DEST/"FlowForge-Line-by-Line.md").read_text(encoding="utf-8").split()),"pdf_pages":len(reader.pages),"pdf":str(output)}
    (DEST/"resources/build-results.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
