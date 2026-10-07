# FlowForge User Guide

FlowForge is a workflow automation tool built around a simple pipeline:

```text
TRIGGER  ->  CONDITION  ->  ACTION
```

- A **trigger** starts a workflow.
- A **condition** decides whether the workflow is allowed to continue.
- An **action** performs the work.

For example:

```text
When GitHub sends a webhook
    if repository equals "KernelForge23/FlowForge"
        send an HTTP request
```

This guide explains the behavior currently implemented in FlowForge and how
to configure each available option.

## 1. Before you begin

### Sign in

FlowForge uses Supabase Auth. Enter the email address and password of an
existing FlowForge account and select **Sign in**.

The current interface provides sign-in, but not self-service registration or
password recovery. For this MVP, an administrator must create or provision
users in the Supabase Auth project first.

After sign-in, each user sees and manages only their own workflows. A user
cannot use the API to read, edit, run, or delete another user's workflows.

### The dashboard

The dashboard contains:

1. The Gmail connection panel.
2. The workflow builder.
3. Your workflow list.
4. The selected workflow's execution history.

To create a workflow, fill in a name, choose a trigger, optionally add a
condition, choose an action, configure it, and select **Create workflow**.

The **Enabled** checkbox controls whether an external webhook can execute the
workflow. A disabled workflow is preserved as a draft but will not run from
the GitHub webhook endpoint.

## 2. How a workflow runs

Every event is normalized by the backend before the workflow engine evaluates
it. The engine performs these steps:

1. It receives an event, such as a dashboard manual run or GitHub webhook.
2. It checks whether the selected workflow's trigger matches that event.
3. It evaluates the workflow condition, if one exists.
4. If the trigger or condition does not match, the execution is recorded as
   `SKIPPED`.
5. If both match, the action runs.
6. The result is recorded in **Execution history** as a success or failure.

The browser configures and requests workflows. The backend executes actions.
Secrets such as GitHub tokens and provider keys are not written into the
execution result shown to the user.

## 3. Triggers

A trigger answers: **"What event should start this workflow?"**

### 3.1 Manual trigger

Select **Manual** in the workflow builder. This is the easiest trigger to
test.

After saving the workflow:

1. Select the workflow in the workflow list.
2. Select **Run now**.
3. FlowForge creates a manual event with the source `dashboard`.
4. The manual trigger matches it.
5. The condition, if present, is evaluated.
6. The configured action is executed.

Manual runs are useful for testing a new workflow before connecting GitHub or
another external service. The current dashboard does not provide a form for
custom manual payload fields; a manual run uses the dashboard test event.

### 3.2 GitHub webhook trigger

Select **GitHub webhook** in the builder. FlowForge then displays the webhook
URL and setup instructions.

The endpoint is:

```text
POST https://YOUR-BACKEND-DOMAIN/api/webhooks/github
```

For local development, the URL is normally:

```text
http://localhost:8000/api/webhooks/github
```

#### Configure GitHub

In the GitHub repository that should send events:

1. Open **Settings**.
2. Select **Webhooks**.
3. Select **Add webhook**.
4. Set the **Payload URL** to the FlowForge GitHub webhook URL.
5. Set **Content type** to `application/json`.
6. Enter the same secret configured as the backend's
   `GITHUB_WEBHOOK_SECRET`.
7. Select the GitHub events that should be delivered.
8. Save the webhook.
9. Make sure the FlowForge workflow is enabled.

GitHub signs the raw request body with the shared secret. FlowForge checks the
`X-Hub-Signature-256` header before parsing or executing the payload. If the
signature is invalid, the request is rejected with `401`.

When the webhook is received, FlowForge:

1. Verifies the signature.
2. Parses the JSON body.
3. Creates a `webhook` event whose source is `github`.
4. Sends that event to enabled webhook workflows.
5. Evaluates each workflow's condition against the top-level JSON fields.
6. Executes matching workflows.

The current webhook route accepts GitHub's JSON payload and applies it to all
enabled GitHub webhook workflows. If you have several enabled webhook
workflows, use conditions to ensure that each workflow responds only to the
events intended for it. For easier testing, use one enabled webhook workflow
at a time.

#### GitHub webhook example

Suppose GitHub sends:

```json
{
  "repository": "KernelForge23/FlowForge",
  "event": "push",
  "ref": "refs/heads/main"
}
```

A condition with:

```text
Condition: Equals
Payload field: repository
Expected value: KernelForge23/FlowForge
```

matches this example. A condition with expected value `another/repository`
does not match, so the action is skipped.

> Important: the current field lookup checks top-level payload keys. Use
> `repository`, not a dotted path such as `repository.full_name`, unless the
> incoming payload itself contains a top-level key with that exact name.

### 3.3 Scheduled trigger

The backend engine includes a scheduled-trigger abstraction, but the current
dashboard does not expose a schedule editor or a scheduler service. Do not
expect a workflow created through the current UI to run automatically on a
timer.

Scheduled automation is intentionally not part of the reliable V1 user
journey because the free Render service can sleep after inactivity.

## 4. Conditions

A condition answers: **"Should this event continue to the action?"**

The current dashboard lets you choose one of these conditions:

- **Equals**
- **Not equals**
- **Contains**

The backend also has comparison implementations for **Greater than** and
**Less than**, plus `AND` and `OR` composite conditions. These are available
to the engine/factory layer but are not currently selectable in the dashboard
form.

If there is no condition, every event that matches the trigger proceeds to the
action.

### 4.1 Payload field

**Payload field** is the name of the value to inspect in the incoming event.

For a GitHub webhook, it is a top-level JSON key. Given:

```json
{
  "repository": "KernelForge23/FlowForge",
  "action": "opened",
  "ref": "refs/heads/main"
}
```

valid payload fields include:

```text
repository
action
ref
```

The field name is not the human-readable label of a GitHub event. It must
match a key in the actual JSON payload.

### 4.2 Expected value

**Expected value** is the value that FlowForge compares with the value found
in the payload field.

For example:

```text
Payload field: action
Expected value: opened
```

With the example payload above, the condition is true.

The comparison is exact for **Equals** and **Not equals**. It is not a
case-insensitive comparison:

```text
"opened" equals "opened"  -> true
"opened" equals "Opened"  -> false
```

### 4.3 Equals

**Equals** continues only when:

```text
payload[payload field] == expected value
```

Example:

```text
Condition: Equals
Payload field: repository
Expected value: KernelForge23/FlowForge
```

Use this when a workflow belongs to one repository, one event name, one
branch, or one exact status.

### 4.4 Not equals

**Not equals** continues when the payload value is different from the
expected value.

Example:

```text
Condition: Not equals
Payload field: action
Expected value: closed
```

This allows the action for every action except `closed`. If the field is
missing, its value is treated as different from the expected value, so use
this condition carefully with untrusted or changing payloads.

### 4.5 Contains

**Contains** checks whether the expected value occurs inside the payload
value.

Example:

```text
Condition: Contains
Payload field: ref
Expected value: main
```

This matches:

```text
refs/heads/main
```

because the string `main` occurs inside it.

Contains can also work with a list-valued payload field. For example, if the
payload contains:

```json
{
  "labels": ["bug", "priority"]
}
```

then an expected value of `bug` is contained in the list.

If the payload field is missing, or its value is not a compatible string/list
value, the condition evaluates to false rather than crashing the workflow.

### 4.6 Greater than and less than

The engine supports:

```text
Greater than
Less than
```

They compare the payload field using Python-style ordering. They are useful
for numeric values such as counts or sizes when the incoming value and the
configured expected value have compatible types.

The current builder does not offer these choices yet. They are engine
capabilities, not current dashboard controls.

### 4.7 AND and OR

The engine supports composite conditions:

- **AND** is true only when every child condition is true.
- **OR** is true when at least one child condition is true.

For example:

```text
repository equals KernelForge23/FlowForge
AND
ref contains refs/heads/main
```

This lets one workflow target a specific repository and branch. Composite
conditions are currently not configurable through the dashboard form.

## 5. Actions

An action answers: **"What should FlowForge do after the trigger and
condition pass?"**

The current dashboard offers:

1. No-op
2. HTTP request
3. GitHub dispatch
4. Email

### 5.1 No-op

The **No-op** action performs no network operation. It simply records that the
workflow reached the action stage.

Use it to:

- Test a trigger.
- Test a condition.
- Confirm that a webhook is reaching FlowForge.
- Demonstrate the workflow engine without configuring an external service.

It does not send a message, call an API, or modify GitHub.

### 5.2 HTTP request

The HTTP action sends a request to a public HTTP or HTTPS endpoint.

In the current UI, choose **HTTP request** and enter an action configuration
JSON object. The supported shape is:

```json
{
  "url": "https://example.com/flowforge-hook",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "X-Workflow": "github-event"
  },
  "body": {
    "message": "FlowForge workflow ran"
  }
}
```

Supported methods are:

```text
GET, POST, PUT, PATCH, DELETE
```

The body can be a JSON object, array, string, number, or boolean. The backend
rejects malformed or unsupported configurations.

Safety behavior:

- Only `http` and `https` URLs are accepted.
- Private, loopback, link-local, reserved, and unspecified IP addresses are
  blocked to reduce SSRF risk.
- Requests have a timeout.
- Payload size is bounded.
- Temporary network failures receive bounded retries.
- Redirects are not followed.
- A non-success HTTP response records an action failure.

Use an endpoint that is prepared to receive the selected HTTP method and JSON
body. Do not put API secrets in a workflow body or custom header unless you
understand that workflow configuration is stored in the database.

### 5.3 GitHub dispatch

The **GitHub dispatch** action tells GitHub to emit a custom
`repository_dispatch` event for a repository. It does not create a commit,
open a pull request, or run an arbitrary command by itself.

The action sends this GitHub API request:

```text
POST https://api.github.com/repos/OWNER/REPOSITORY/dispatches
```

The request body is equivalent to:

```json
{
  "event_type": "flowforge",
  "client_payload": {
    "environment": "production",
    "workflow": "release-notification"
  }
}
```

#### Configure GitHub dispatch in FlowForge

Choose **GitHub dispatch**, then fill in:

1. **GitHub token**
   A GitHub personal access token permitted to dispatch events to the target
   repository. Use the smallest practical scope. For a fine-grained token,
   grant the target repository the required repository contents permission
   described by GitHub for dispatching workflows. The UI masks this field,
   and the backend does not expose the token in execution results.

2. **Repository**
   The exact owner/name pair:

   ```text
   KernelForge23/FlowForge
   ```

3. **Event type**
   A non-empty custom string, for example:

   ```text
   flowforge
   release-ready
   deploy-production
   ```

4. **Client payload (JSON)**
   A JSON object containing data that GitHub Actions can use.

Example:

```json
{
  "environment": "production",
  "source": "flowforge",
  "repository": "KernelForge23/FlowForge"
}
```

#### Receive the dispatch in GitHub Actions

The target repository needs a workflow listening for `repository_dispatch`.
For example:

```yaml
name: FlowForge dispatch receiver

on:
  repository_dispatch:
    types: [deploy-production]

jobs:
  receive:
    runs-on: ubuntu-latest
    steps:
      - name: Print dispatch data
        run: |
          echo "Environment: ${{ github.event.client_payload.environment }}"
          echo "Source: ${{ github.event.client_payload.source }}"
```

The `types` value must equal the FlowForge **Event type**. The payload is
available to GitHub Actions under:

```text
github.event.client_payload
```

If the event type is `deploy-production`, the action above can start a
deployment job, call a reusable workflow, or perform another repository
operation defined in GitHub Actions.

#### What happens when GitHub dispatch runs

1. FlowForge validates the repository format and required token.
2. FlowForge sends the event to GitHub.
3. GitHub authenticates the token and checks repository permissions.
4. GitHub creates the `repository_dispatch` event.
5. Matching GitHub Actions workflows start.
6. FlowForge records the HTTP status from GitHub, without exposing the token.

A successful FlowForge execution means GitHub accepted the dispatch request.
It does not guarantee that every downstream GitHub Actions step succeeded;
inspect the Actions tab in the target repository for that result.

### 5.4 Email

The **Email** action sends an email through the configured provider. The
deployment can use the backend email provider configuration or the user's
connected Gmail account, depending on the deployment settings.

First, use the **Gmail connection** panel when the dashboard says Gmail is
required. Complete the Google authorization flow and return to FlowForge.
The panel should show the connected account.

Then configure:

- **Recipients**: comma-separated email addresses.
- **Subject**: a subject between 1 and 200 characters.
- **Text body**: plain-text content.
- **HTML body**: optional HTML content.

At least one recipient, a subject, and either text or HTML content are
required.

Example:

```text
Recipients: owner@example.com, team@example.com
Subject: FlowForge GitHub event received
Text body: A matching GitHub event was received.
HTML body: <p>A matching GitHub event was received.</p>
```

The action validates recipient addresses, limits the recipient count and
message size, applies bounded retries for temporary provider failures, and
records safe provider metadata rather than credentials.

If Gmail is configured, the workflow must belong to an authenticated user
with a connected Gmail account. Disconnecting Gmail causes Gmail-backed email
actions to fail until the account is connected again.

## 6. A complete beginner workflow

This example sends an HTTP request when a GitHub push webhook for the
FlowForge repository arrives.

### Step 1: Create the workflow

1. Sign in.
2. Enter the name:

   ```text
   FlowForge main branch notification
   ```

3. Choose **GitHub webhook**.
4. Leave **Enabled** checked.

### Step 2: Add the condition

Choose **Equals** and enter:

```text
Payload field: repository
Expected value: KernelForge23/FlowForge
```

This prevents pushes from unrelated repositories from running the action.

### Step 3: Configure the action

Choose **HTTP request** and enter:

```json
{
  "url": "https://example.com/flowforge-hook",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "message": "A matching FlowForge webhook was received"
  }
}
```

Select **Create workflow**.

### Step 4: Configure GitHub

Copy the webhook URL displayed by FlowForge into the GitHub repository
webhook settings, choose JSON content type, configure the shared secret, and
select the desired GitHub events.

### Step 5: Test

Push a matching event. Then select the workflow in FlowForge and inspect
**Execution history**.

Possible outcomes:

- `SUCCESS`: the action completed.
- `SKIPPED`: the trigger or condition did not match, or the workflow was
  disabled.
- A failure status with an error: the action or provider returned an error.

The execution error is displayed in the history row when available.

## 7. Troubleshooting

### "Authentication required" or sign-in fails

- Confirm that the user exists in Supabase Auth.
- Confirm the frontend has the correct production Supabase URL and
  anonymous/publishable key.
- Confirm the frontend and backend use the same Supabase project.

### The workflow list is empty

- Confirm you are signed in with the intended account.
- A workflow belongs to the account that created it.
- Confirm the backend is using the production PostgreSQL `DATABASE_URL`, not
  an ephemeral SQLite file.

### A webhook returns 401

- Confirm the GitHub webhook secret exactly matches
  `GITHUB_WEBHOOK_SECRET`.
- Confirm GitHub is sending `application/json`.
- Do not manually alter the request body when testing the signature.

### A webhook is received but execution is skipped

- Confirm the workflow is enabled.
- Confirm the trigger is **GitHub webhook**, not **Manual**.
- Check the exact top-level payload field name.
- Check capitalization and spelling of the expected value.
- Use a condition that matches the real GitHub payload.

### GitHub dispatch fails

- Confirm the repository is exactly `owner/name`.
- Confirm the token has access to that repository.
- Confirm the event type is non-empty.
- Confirm the receiving GitHub Actions workflow listens for
  `repository_dispatch` and the same event type.
- Inspect the target repository's GitHub Actions page after FlowForge reports
  that GitHub accepted the request.

### Email fails

- Confirm Gmail is connected when Gmail is the configured provider.
- Confirm recipients are valid email addresses.
- Confirm subject and text or HTML content are present.
- Confirm the deployment has the required provider credentials and sender
  configuration.

### The first request is slow

The free Render backend can sleep after inactivity. The first request after a
sleep may be a cold start. This is expected for the free-tier deployment and
does not mean the workflow definition is invalid.

## 8. Current feature boundaries

The engine contains more abstractions than the current dashboard exposes.
Specifically:

- The dashboard currently creates one condition and one action per workflow.
- `AND` and `OR` composite conditions exist in the backend but are not yet
  selectable in the form.
- Greater-than and less-than comparisons exist in the backend but are not yet
  selectable in the form.
- Scheduled triggers exist in the engine but there is no current schedule
  editor or reliable scheduler service.
- The GitHub UI is configured for repository dispatch. Other backend GitHub
  endpoints are implementation details, not current dashboard choices.

These boundaries are documented so that the user guide describes the
implemented product rather than promising unfinished controls.

## 9. Security and safe usage

- Do not share your FlowForge password, Supabase token, Gmail authorization,
  or GitHub token.
- Use a dedicated, least-privileged GitHub token for each integration.
- Treat workflow configuration as sensitive when it contains external
  endpoint URLs or provider details.
- Keep `GITHUB_WEBHOOK_SECRET` private.
- Never place private network URLs in HTTP actions.
- Prefer a test repository and test recipient while learning.
- Inspect execution history after each new integration.
