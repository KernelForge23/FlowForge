# FlowForge deployment

FlowForge deploys as two free-tier services:

- React/Vite frontend on Vercel
- FastAPI backend on Render
- Supabase provides PostgreSQL and authentication

## Supabase

Create a Supabase project and enable email/password authentication. Add the deployed frontend URL to the Supabase authentication URL configuration.

The backend needs:

```text
DATABASE_URL=<Supabase PostgreSQL connection string>
SUPABASE_URL=https://<project>.supabase.co
SUPABASE_ANON_KEY=<Supabase anonymous key>
GITHUB_WEBHOOK_SECRET=<optional GitHub webhook secret>
FRONTEND_ORIGIN=https://<vercel-project>.vercel.app
EMAIL_PROVIDER=resend
EMAIL_API_KEY=<Resend API key>
EMAIL_FROM=FlowForge <noreply@your-verified-domain.com>
GOOGLE_CLIENT_ID=<Google OAuth web client ID>
GOOGLE_CLIENT_SECRET=<Google OAuth web client secret>
GOOGLE_REDIRECT_URI=http://localhost:8000/api/integrations/gmail/callback
TOKEN_ENCRYPTION_KEY=<Fernet key>
```

Do not use the Supabase service-role key in the frontend or commit any credentials.
The email API key must remain a backend-only environment variable. Verify the sender domain with Resend before testing delivery.
For personal Gmail sending, configure the Google OAuth variables instead. Generate `TOKEN_ENCRYPTION_KEY` with `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"`.

## Render backend

Create a web service from the repository with:

```text
Root directory: backend
Build command: pip install -r requirements.txt
Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Set the backend environment variables above in the Render dashboard. Verify:

```text
GET https://<render-service>/health
```

Render free services sleep after inactivity, so scheduled triggers are best-effort and cold starts are expected.

## Vercel frontend

Create a Vercel project using the `frontend` directory. Set:

```text
VITE_API_URL=https://<render-service>
VITE_SUPABASE_URL=https://<project>.supabase.co
VITE_SUPABASE_ANON_KEY=<Supabase anonymous key>
```

After deployment, use the production frontend URL in Supabase redirect settings and configure backend CORS for that origin before public use.

## Smoke test

1. Open the Vercel URL and sign in with a Supabase email/password user.
2. Create a manual workflow.
3. Select it and run it.
4. Confirm a `SUCCESS` execution appears after refresh.
5. Create a webhook workflow and send a signed GitHub webhook request if `GITHUB_WEBHOOK_SECRET` is configured.

Local development uses the templates in `backend/.env.example` and `frontend/.env.example`.

## Personal Gmail integration

1. In Google Cloud Console, create an OAuth Web application and enable the Gmail API.
2. Configure the OAuth consent screen and add the `gmail.send` scope.
3. Add `http://localhost:8000/api/integrations/gmail/callback` as an authorized redirect URI.
4. Set `EMAIL_PROVIDER=gmail`, the Google OAuth variables, and a generated token encryption key in the backend `.env`.
5. Start FlowForge, sign in, and click **Connect Gmail**.
6. Approve the limited Gmail sending permission.
7. Create an Email action. It sends from the connected Gmail account; no sender address or Gmail password is stored in the workflow.
8. Disconnect Gmail from the dashboard to remove the stored encrypted connection.

For production, use the HTTPS backend callback URL as the Google redirect URI and keep the client secret and token encryption key in the backend hosting provider only.

## GitHub repository dispatch demonstration

The repository includes `.github/workflows/flowforge-dispatch.yml`. It listens for the `flowforge` repository-dispatch event and creates a visible GitHub issue.

Configure the FlowForge GitHub action with:

```json
{
  "token": "<GitHub token>",
  "repository": "KernelForge23/FlowForge",
  "event_type": "flowforge",
  "body": {
    "source": "FlowForge dashboard"
  }
}
```

The token must be allowed to access the target repository and dispatch events. For a fine-grained token, grant access to `KernelForge23/FlowForge` and set **Contents: Read and write**; keep **Metadata: Read-only** enabled. The token is stored in the workflow configuration for this MVP; use a disposable test token and rotate it after demonstrations.

After running the workflow in FlowForge, open the repository's **Issues** tab. A new issue named **FlowForge event received** should appear.
