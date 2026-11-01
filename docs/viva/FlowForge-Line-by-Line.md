# FlowForge: complete line-by-line source companion

Snapshot: 31 October 2026. Read beside FlowForge-Master-Guide.md. This appendix is an explanation of the checked-in implementation, including its limitations; no application code was changed.

Every selected file appears with its original numbered source and one note for every physical line. Blank lines are explicitly identified as formatting. Start with each file's purpose note, read the source, then use the L-number notes. Long expressions continue over several physical lines: continuation notes identify the originating statement rather than pretending punctuation is an independent operation.

Python notes use syntax-aware parsing; file-specific and critical-line explanations add behavior and caveats. TypeScript/JSX notes explain the state, callbacks, guards, and rendered controls. CSS notes explain selectors and individual properties. This source snapshot is checked by SHA-256 fingerprints; later code edits can invalidate line references.

## Navigation

- [backend/app/__init__.py](#backend-app-initpy)
- [backend/app/api/__init__.py](#backend-app-api-initpy)
- [backend/app/api/auth.py](#backend-app-api-authpy)
- [backend/app/api/routes/__init__.py](#backend-app-api-routes-initpy)
- [backend/app/api/routes/health.py](#backend-app-api-routes-healthpy)
- [backend/app/api/routes/integrations.py](#backend-app-api-routes-integrationspy)
- [backend/app/api/routes/webhooks.py](#backend-app-api-routes-webhookspy)
- [backend/app/api/routes/workflows.py](#backend-app-api-routes-workflowspy)
- [backend/app/config.py](#backend-app-configpy)
- [backend/app/core/__init__.py](#backend-app-core-initpy)
- [backend/app/core/actions/__init__.py](#backend-app-core-actions-initpy)
- [backend/app/core/actions/base.py](#backend-app-core-actions-basepy)
- [backend/app/core/actions/email.py](#backend-app-core-actions-emailpy)
- [backend/app/core/actions/github.py](#backend-app-core-actions-githubpy)
- [backend/app/core/actions/http.py](#backend-app-core-actions-httppy)
- [backend/app/core/actions/noop.py](#backend-app-core-actions-nooppy)
- [backend/app/core/conditions/__init__.py](#backend-app-core-conditions-initpy)
- [backend/app/core/conditions/base.py](#backend-app-core-conditions-basepy)
- [backend/app/core/conditions/comparison.py](#backend-app-core-conditions-comparisonpy)
- [backend/app/core/conditions/composite.py](#backend-app-core-conditions-compositepy)
- [backend/app/core/conditions/equals.py](#backend-app-core-conditions-equalspy)
- [backend/app/core/engine.py](#backend-app-core-enginepy)
- [backend/app/core/event.py](#backend-app-core-eventpy)
- [backend/app/core/factories.py](#backend-app-core-factoriespy)
- [backend/app/core/triggers/__init__.py](#backend-app-core-triggers-initpy)
- [backend/app/core/triggers/base.py](#backend-app-core-triggers-basepy)
- [backend/app/core/triggers/manual.py](#backend-app-core-triggers-manualpy)
- [backend/app/core/triggers/scheduled.py](#backend-app-core-triggers-scheduledpy)
- [backend/app/core/triggers/webhook.py](#backend-app-core-triggers-webhookpy)
- [backend/app/core/workflow.py](#backend-app-core-workflowpy)
- [backend/app/db.py](#backend-app-dbpy)
- [backend/app/main.py](#backend-app-mainpy)
- [backend/app/models/__init__.py](#backend-app-models-initpy)
- [backend/app/models/base.py](#backend-app-models-basepy)
- [backend/app/models/entities.py](#backend-app-models-entitiespy)
- [backend/app/repositories/__init__.py](#backend-app-repositories-initpy)
- [backend/app/repositories/workflow.py](#backend-app-repositories-workflowpy)
- [backend/app/schemas/__init__.py](#backend-app-schemas-initpy)
- [backend/app/schemas/health.py](#backend-app-schemas-healthpy)
- [backend/app/schemas/workflows.py](#backend-app-schemas-workflowspy)
- [backend/app/services/__init__.py](#backend-app-services-initpy)
- [backend/app/services/gmail.py](#backend-app-services-gmailpy)
- [backend/app/services/health.py](#backend-app-services-healthpy)
- [backend/app/services/workflow.py](#backend-app-services-workflowpy)
- [backend/tests/conftest.py](#backend-tests-conftestpy)
- [backend/tests/test_auth.py](#backend-tests-testauthpy)
- [backend/tests/test_config.py](#backend-tests-testconfigpy)
- [backend/tests/test_engine.py](#backend-tests-testenginepy)
- [backend/tests/test_gmail.py](#backend-tests-testgmailpy)
- [backend/tests/test_health.py](#backend-tests-testhealthpy)
- [backend/tests/test_integrations.py](#backend-tests-testintegrationspy)
- [backend/tests/test_models.py](#backend-tests-testmodelspy)
- [backend/tests/test_oop.py](#backend-tests-testooppy)
- [backend/tests/test_workflow_api.py](#backend-tests-testworkflowapipy)
- [backend/tests/test_workflow_service.py](#backend-tests-testworkflowservicepy)
- [frontend/src/App.css](#frontend-src-appcss)
- [frontend/src/App.tsx](#frontend-src-apptsx)
- [frontend/src/index.css](#frontend-src-indexcss)
- [frontend/src/lib/supabase.ts](#frontend-src-lib-supabasets)
- [frontend/src/main.tsx](#frontend-src-maintsx)
- [frontend/src/services/api.ts](#frontend-src-services-apits)
- [backend/requirements.txt](#backend-requirementstxt)
- [backend/pytest.ini](#backend-pytestini)
- [frontend/package.json](#frontend-packagejson)
- [frontend/index.html](#frontend-indexhtml)
- [frontend/vite.config.ts](#frontend-viteconfigts)
- [frontend/tsconfig.json](#frontend-tsconfigjson)
- [frontend/tsconfig.app.json](#frontend-tsconfigappjson)
- [frontend/tsconfig.node.json](#frontend-tsconfignodejson)
- [frontend/.oxlintrc.json](#frontend-oxlintrcjson)
- [.github/workflows/flowforge-dispatch.yml](#github-workflows-flowforge-dispatchyml)

<a id="backend-app-initpy"></a>
## backend/app/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6`. Physical lines: 1.

### Numbered source

```python
0001 | 
```

### Every-line explanation

**L0001.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.


<a id="backend-app-api-initpy"></a>
## backend/app/api/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6`. Physical lines: 1.

### Numbered source

```python
0001 | 
```

### Every-line explanation

**L0001.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.


<a id="backend-app-api-authpy"></a>
## backend/app/api/auth.py

Remote Supabase token verification and identity object. Empty supabase_url returns None for local mode. A configured service requires Bearer syntax, calls the remote user endpoint, and validates ID/email fields. This is not local JWT signature verification.

Source fingerprint: `2e3c73cfdb8a22f5e4711948af909ea1a5d543c41d9c13533f3638c91406a9dc`. Physical lines: 41.

### Numbered source

```python
0001 | from dataclasses import dataclass
0002 | from typing import Annotated
0003 | 
0004 | import httpx
0005 | from fastapi import Header, HTTPException
0006 | 
0007 | from app.config import settings
0008 | 
0009 | 
0010 | @dataclass(frozen=True)
0011 | class AuthenticatedUser:
0012 |     id: str
0013 |     email: str
0014 | 
0015 | 
0016 | def current_user(
0017 |     authorization: Annotated[str | None, Header()] = None,
0018 | ) -> AuthenticatedUser | None:
0019 |     if not settings.supabase_url:
0020 |         return None
0021 |     if not authorization or not authorization.startswith("Bearer "):
0022 |         raise HTTPException(status_code=401, detail="Authentication required")
0023 |     try:
0024 |         response = httpx.get(
0025 |             f"{settings.supabase_url.rstrip('/')}/auth/v1/user",
0026 |             headers={
0027 |                 "Authorization": authorization,
0028 |                 "apikey": settings.supabase_anon_key,
0029 |             },
0030 |             timeout=5.0,
0031 |         )
0032 |     except httpx.HTTPError as exc:
0033 |         raise HTTPException(status_code=503, detail="Authentication service unavailable") from exc
0034 |     if response.status_code != 200:
0035 |         raise HTTPException(status_code=401, detail="Invalid authentication token")
0036 |     data = response.json()
0037 |     user_id = data.get("id")
0038 |     email = data.get("email")
0039 |     if not isinstance(user_id, str) or not isinstance(email, str):
0040 |         raise HTTPException(status_code=401, detail="Invalid authentication response")
0041 |     return AuthenticatedUser(id=user_id, email=email)
```

### Every-line explanation

**L0001.** Import dataclass from `dataclasses`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Annotated from `typing`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import module(s) `httpx`. Top-level module code runs on first import.

**L0005.** Import Header, HTTPException from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Generate a dataclass and disallow ordinary field reassignment after initialization (shallow protection).

**L0011.** Define class `AuthenticatedUser`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0012.** Declare `id` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0013.** Declare `email` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Define function/method `current_user(authorization: Annotated[str | None, Header()]=None)` with intended return type `AuthenticatedUser | None`. 

**L0017.** Continue the function signature: `authorization: Annotated[str | None, Header()] = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0018.** Continue the function signature: `) -> AuthenticatedUser | None:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0019.** Enter the following indented branch only if you negate the truth value of `settings.supabase_url`.

**L0020.** Return from this function: use literal value `None` (NoneType).

**L0021.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not authorization or not authorization.startswith('Bearer ')`; later terms run only when needed.

**L0022.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=401, detail='Authentication required')`. Normal execution at this point stops.

**L0023.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0024.** Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get(f"{settings.supabase_url.rstrip('/')}/auth/v1/user", headers={'Authorization': authorization, 'apikey': settings.supabase_anon_key}, timeout=5.0)`. Assignment stores a value/reference; it is not an equality test.

**L0025.** Continue the statement starting at L24 with `f"{settings.supabase_url.rstrip('/')}/auth/v1/user"`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get(f"{settings.supabase_url.rstrip('/')}/auth/v1/user", headers={'Authorization': authorization, 'apikey': settings.supabase_anon_key}, timeout=5.0)`. Assignment stores a value/reference; it is not an equality test.

**L0026.** Continue the statement starting at L24 with `headers={`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get(f"{settings.supabase_url.rstrip('/')}/auth/v1/user", headers={'Authorization': authorization, 'apikey': settings.supabase_anon_key}, timeout=5.0)`. Assignment stores a value/reference; it is not an equality test.

**L0027.** Continue the statement starting at L24 with `"Authorization": authorization`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get(f"{settings.supabase_url.rstrip('/')}/auth/v1/user", headers={'Authorization': authorization, 'apikey': settings.supabase_anon_key}, timeout=5.0)`. Assignment stores a value/reference; it is not an equality test.

**L0028.** Continue the statement starting at L24 with `"apikey": settings.supabase_anon_key`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get(f"{settings.supabase_url.rstrip('/')}/auth/v1/user", headers={'Authorization': authorization, 'apikey': settings.supabase_anon_key}, timeout=5.0)`. Assignment stores a value/reference; it is not an equality test.

**L0029.** Close the grouped expression/declaration introduced at L24; delimiters/commas complete the same statement rather than execute a separate operation.

**L0030.** Continue the statement starting at L24 with `timeout=5.0`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get(f"{settings.supabase_url.rstrip('/')}/auth/v1/user", headers={'Authorization': authorization, 'apikey': settings.supabase_anon_key}, timeout=5.0)`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Close the grouped expression/declaration introduced at L24; delimiters/commas complete the same statement rather than execute a separate operation.

**L0032.** Catch `httpx.HTTPError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0033.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=503, detail='Authentication service unavailable')`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0034.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response.status_code != 200`; this produces the branch/assertion's truth value.

**L0035.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=401, detail='Invalid authentication token')`. Normal execution at this point stops.

**L0036.** Assign to `data`: decode this response's JSON body, potentially raising on invalid data: `response.json()`. Assignment stores a value/reference; it is not an equality test.

**L0037.** Assign to `user_id`: read a mapping key with a default (or call this object's get method as identified by the receiver): `data.get('id')`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Assign to `email`: read a mapping key with a default (or call this object's get method as identified by the receiver): `data.get('email')`. Assignment stores a value/reference; it is not an equality test.

**L0039.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(user_id, str) or not isinstance(email, str)`; later terms run only when needed.

**L0040.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=401, detail='Invalid authentication response')`. Normal execution at this point stops.

**L0041.** Return from this function: construct the immutable verified identity data object: `AuthenticatedUser(id=user_id, email=email)`.


<a id="backend-app-api-routes-initpy"></a>
## backend/app/api/routes/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `6b4b950cfe4355ea621c411a7206fa85b3c7f2d391da9f39b81278884e295e48`. Physical lines: 9.

### Numbered source

```python
0001 | from fastapi import APIRouter
0002 | 
0003 | from app.api.routes import health, integrations, webhooks, workflows
0004 | 
0005 | api_router = APIRouter()
0006 | api_router.include_router(health.router)
0007 | api_router.include_router(workflows.router)
0008 | api_router.include_router(webhooks.router)
0009 | api_router.include_router(integrations.router)
```

### Every-line explanation

**L0001.** Import APIRouter from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import health, integrations, webhooks, workflows from `app.api.routes`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Assign to `api_router`: call `APIRouter` with the displayed positional/named arguments: `APIRouter()`. Assignment stores a value/reference; it is not an equality test.

**L0006.** Perform the expression for its effect: call `api_router.include_router` with the displayed positional/named arguments: `api_router.include_router(health.router)`.

**L0007.** Perform the expression for its effect: call `api_router.include_router` with the displayed positional/named arguments: `api_router.include_router(workflows.router)`.

**L0008.** Perform the expression for its effect: call `api_router.include_router` with the displayed positional/named arguments: `api_router.include_router(webhooks.router)`.

**L0009.** Perform the expression for its effect: call `api_router.include_router` with the displayed positional/named arguments: `api_router.include_router(integrations.router)`.


<a id="backend-app-api-routes-healthpy"></a>
## backend/app/api/routes/health.py

Thin liveness route with an injected health service. A successful response does not test database readiness or external provider connectivity.

Source fingerprint: `44311259bda12fb6a8283603ca0a7e8f208e5e050809103d1368fd66779c6e6f`. Physical lines: 15.

### Numbered source

```python
0001 | from fastapi import APIRouter, Depends
0002 | 
0003 | from app.schemas.health import HealthResponse
0004 | from app.services.health import HealthService
0005 | 
0006 | router = APIRouter(tags=["health"])
0007 | 
0008 | 
0009 | def get_health_service() -> HealthService:
0010 |     return HealthService()
0011 | 
0012 | 
0013 | @router.get("/health", response_model=HealthResponse)
0014 | def health(service: HealthService = Depends(get_health_service)) -> HealthResponse:
0015 |     return service.status()
```

### Every-line explanation

**L0001.** Import APIRouter, Depends from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import HealthResponse from `app.schemas.health`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import HealthService from `app.services.health`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Assign to `router`: call `APIRouter` with the displayed positional/named arguments: `APIRouter(tags=['health'])`. Assignment stores a value/reference; it is not an equality test.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Define function/method `get_health_service()` with intended return type `HealthService`. 

**L0010.** Return from this function: call `HealthService` with the displayed positional/named arguments: `HealthService()`.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Apply/register the following definition with decorator `@router.get("/health", response_model=HealthResponse)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0014.** Define function/method `health(service: HealthService=Depends(get_health_service))` with intended return type `HealthResponse`. 

**L0015.** Return from this function: call `service.status` with the displayed positional/named arguments: `service.status()`.


<a id="backend-app-api-routes-integrationspy"></a>
## backend/app/api/routes/integrations.py

Authenticated Gmail connect/status/disconnect and state-validated callback. State is hashed in storage, expires in ten minutes, and is marked used. Callback redirects with status/error query parameters. Disconnect is local deletion, not provider-side revocation.

Source fingerprint: `fd2f91a0997f60272f604c29db0dd8febaeb216284debd9820daf9322d0d3ad8`. Physical lines: 104.

### Numbered source

```python
0001 | from datetime import datetime, timedelta, timezone
0002 | from urllib.parse import urlencode
0003 | 
0004 | from fastapi import APIRouter, Depends, HTTPException
0005 | from fastapi.responses import RedirectResponse
0006 | from sqlalchemy.orm import Session
0007 | 
0008 | from app.api.auth import AuthenticatedUser, current_user
0009 | from app.config import settings
0010 | from app.db import get_session
0011 | from app.models import GmailOAuthState, User
0012 | from app.services.gmail import GmailService, new_oauth_state
0013 | 
0014 | router = APIRouter(prefix="/api/integrations/gmail", tags=["integrations"])
0015 | 
0016 | 
0017 | def _require_user(user: AuthenticatedUser | None) -> AuthenticatedUser:
0018 |     if user is None:
0019 |         raise HTTPException(status_code=401, detail="Authentication required")
0020 |     return user
0021 | 
0022 | 
0023 | @router.get("/connect")
0024 | def connect_gmail(
0025 |     session: Session = Depends(get_session),
0026 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0027 | ) -> dict[str, str]:
0028 |     user = _require_user(authenticated_user)
0029 |     if session.get(User, user.id) is None:
0030 |         session.add(User(id=user.id, email=user.email))
0031 |         session.flush()
0032 |     state = new_oauth_state()
0033 |     session.add(
0034 |         GmailOAuthState(
0035 |             state_hash=GmailService.hash_state(state),
0036 |             user_id=user.id,
0037 |             expires_at=datetime.now(timezone.utc) + timedelta(minutes=10),
0038 |         )
0039 |     )
0040 |     try:
0041 |         destination = GmailService(session).oauth_url(state)
0042 |     except RuntimeError as exc:
0043 |         raise HTTPException(status_code=503, detail=str(exc)) from exc
0044 |     return {"authorization_url": destination}
0045 | 
0046 | 
0047 | @router.get("/callback")
0048 | def gmail_callback(
0049 |     code: str | None = None,
0050 |     state: str | None = None,
0051 |     error: str | None = None,
0052 |     session: Session = Depends(get_session),
0053 | ) -> RedirectResponse:
0054 |     params = {"gmail": "error"}
0055 |     if error or not code or not state:
0056 |         params["reason"] = "authorization_cancelled"
0057 |     else:
0058 |         oauth_state = (
0059 |             session.query(GmailOAuthState)
0060 |             .filter_by(state_hash=GmailService.hash_state(state))
0061 |             .one_or_none()
0062 |         )
0063 |         now = datetime.now(timezone.utc)
0064 |         expires_at = oauth_state.expires_at if oauth_state is not None else None
0065 |         if expires_at is not None and expires_at.tzinfo is None:
0066 |             expires_at = expires_at.replace(tzinfo=timezone.utc)
0067 |         if oauth_state is None or oauth_state.used_at is not None or expires_at < now:
0068 |             params["reason"] = "invalid_authorization_state"
0069 |         else:
0070 |             oauth_state.used_at = now
0071 |             try:
0072 |                 service = GmailService(session)
0073 |                 access_token, refresh_token, expires_at = service.exchange_code(code)
0074 |                 email = service.profile(access_token)
0075 |                 service.save_connection(
0076 |                     oauth_state.user_id, email, access_token, refresh_token, expires_at
0077 |                 )
0078 |                 params = {"gmail": "connected"}
0079 |             except RuntimeError as exc:
0080 |                 params["reason"] = "authorization_failed"
0081 |                 params["detail"] = str(exc)
0082 |     return RedirectResponse(
0083 |         f"{settings.frontend_origin}/?{urlencode(params)}",
0084 |         status_code=302,
0085 |     )
0086 | 
0087 | 
0088 | @router.get("/status")
0089 | def gmail_status(
0090 |     session: Session = Depends(get_session),
0091 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0092 | ) -> dict[str, object]:
0093 |     user = _require_user(authenticated_user)
0094 |     connection = GmailService(session).connection(user.id)
0095 |     return {"connected": connection is not None, "email": connection.email if connection else None}
0096 | 
0097 | 
0098 | @router.delete("")
0099 | def disconnect_gmail(
0100 |     session: Session = Depends(get_session),
0101 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0102 | ) -> None:
0103 |     user = _require_user(authenticated_user)
0104 |     GmailService(session).disconnect(user.id)
```

### Every-line explanation

**L0001.** Import datetime, timedelta, timezone from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import urlencode from `urllib.parse`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import APIRouter, Depends, HTTPException from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import RedirectResponse from `fastapi.responses`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import Session from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Import AuthenticatedUser, current_user from `app.api.auth`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Import get_session from `app.db`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Import GmailOAuthState, User from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0012.** Import GmailService, new_oauth_state from `app.services.gmail`. Imported names become available in this module; aliases distinguish roles where used.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Assign to `router`: call `APIRouter` with the displayed positional/named arguments: `APIRouter(prefix='/api/integrations/gmail', tags=['integrations'])`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Define function/method `_require_user(user: AuthenticatedUser | None)` with intended return type `AuthenticatedUser`. 

**L0018.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `user is None`; this produces the branch/assertion's truth value.

**L0019.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=401, detail='Authentication required')`. Normal execution at this point stops.

**L0020.** Return from this function: read/evaluate `user`.

**L0021.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0022.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0023.** Apply/register the following definition with decorator `@router.get("/connect")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0024.** Define function/method `connect_gmail(session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `dict[str, str]`. 

**L0025.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0026.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0027.** Continue the function signature: `) -> dict[str, str]:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0028.** Assign to `user`: call `_require_user` with the displayed positional/named arguments: `_require_user(authenticated_user)`. Assignment stores a value/reference; it is not an equality test.

**L0029.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `session.get(User, user.id) is None`; this produces the branch/assertion's truth value.

**L0030.** Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(User(id=user.id, email=user.email))`.

**L0031.** Perform the expression for its effect: send pending SQL in the current transaction without committing: `session.flush()`.

**L0032.** Assign to `state`: call `new_oauth_state` with the displayed positional/named arguments: `new_oauth_state()`. Assignment stores a value/reference; it is not an equality test.

**L0033.** Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(GmailOAuthState(state_hash=GmailService.hash_state(state), user_id=user.id, expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)))`.

**L0034.** Continue the statement starting at L33 with `GmailOAuthState(`. Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(GmailOAuthState(state_hash=GmailService.hash_state(state), user_id=user.id, expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)))`.

**L0035.** Continue the statement starting at L33 with `state_hash=GmailService.hash_state(state)`. Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(GmailOAuthState(state_hash=GmailService.hash_state(state), user_id=user.id, expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)))`.

**L0036.** Continue the statement starting at L33 with `user_id=user.id`. Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(GmailOAuthState(state_hash=GmailService.hash_state(state), user_id=user.id, expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)))`.

**L0037.** Continue the statement starting at L33 with `expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)`. Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(GmailOAuthState(state_hash=GmailService.hash_state(state), user_id=user.id, expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)))`.

**L0038.** Close the grouped expression/declaration introduced at L33; delimiters/commas complete the same statement rather than execute a separate operation.

**L0039.** Close the grouped expression/declaration introduced at L33; delimiters/commas complete the same statement rather than execute a separate operation.

**L0040.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0041.** Assign to `destination`: construct Google's consent URL from settings and state: `GmailService(session).oauth_url(state)`. Assignment stores a value/reference; it is not an equality test.

**L0042.** Catch `RuntimeError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0043.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=503, detail=str(exc))`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0044.** Return from this function: construct a dictionary mapping the displayed keys to values: `{'authorization_url': destination}`.

**L0045.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0046.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0047.** Apply/register the following definition with decorator `@router.get("/callback")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0048.** Define function/method `gmail_callback(code: str | None=None, state: str | None=None, error: str | None=None, session: Session=Depends(get_session))` with intended return type `RedirectResponse`. 

**L0049.** Continue the function signature: `code: str | None = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0050.** Continue the function signature: `state: str | None = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0051.** Continue the function signature: `error: str | None = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0052.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0053.** Continue the function signature: `) -> RedirectResponse:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0054.** Assign to `params`: construct a dictionary mapping the displayed keys to values: `{'gmail': 'error'}`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `error or not code or (not state)`; later terms run only when needed.

**L0056.** Assign to `params['reason']`: use literal value `'authorization_cancelled'` (str). Assignment stores a value/reference; it is not an equality test.

**L0057.** Alternative branch when the preceding if condition is false, or the try completed without its expected exception (inspect the enclosing block).

**L0058.** Assign to `oauth_state`: require zero or one matching row and reject duplicates: `session.query(GmailOAuthState).filter_by(state_hash=GmailService.hash_state(state)).one_or_none()`. Assignment stores a value/reference; it is not an equality test.

**L0059.** Continue the statement starting at L58 with `session.query(GmailOAuthState)`. Assign to `oauth_state`: require zero or one matching row and reject duplicates: `session.query(GmailOAuthState).filter_by(state_hash=GmailService.hash_state(state)).one_or_none()`. Assignment stores a value/reference; it is not an equality test.

**L0060.** Continue the statement starting at L58 with `.filter_by(state_hash=GmailService.hash_state(state))`. Assign to `oauth_state`: require zero or one matching row and reject duplicates: `session.query(GmailOAuthState).filter_by(state_hash=GmailService.hash_state(state)).one_or_none()`. Assignment stores a value/reference; it is not an equality test.

**L0061.** Continue the statement starting at L58 with `.one_or_none()`. Assign to `oauth_state`: require zero or one matching row and reject duplicates: `session.query(GmailOAuthState).filter_by(state_hash=GmailService.hash_state(state)).one_or_none()`. Assignment stores a value/reference; it is not an equality test.

**L0062.** Close the grouped expression/declaration introduced at L58; delimiters/commas complete the same statement rather than execute a separate operation.

**L0063.** Assign to `now`: capture the current time, using supplied UTC timezone where given: `datetime.now(timezone.utc)`. Assignment stores a value/reference; it is not an equality test.

**L0064.** Assign to `expires_at`: choose `oauth_state.expires_at` when `oauth_state is not None` is true, otherwise `None`. Assignment stores a value/reference; it is not an equality test.

**L0065.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `expires_at is not None and expires_at.tzinfo is None`; later terms run only when needed.

**L0066.** Assign to `expires_at`: replace the specified datetime field/timezone or string segment, according to receiver: `expires_at.replace(tzinfo=timezone.utc)`. Assignment stores a value/reference; it is not an equality test.

**L0067.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `oauth_state is None or oauth_state.used_at is not None or expires_at < now`; later terms run only when needed.

**L0068.** Assign to `params['reason']`: use literal value `'invalid_authorization_state'` (str). Assignment stores a value/reference; it is not an equality test.

**L0069.** Alternative branch when the preceding if condition is false, or the try completed without its expected exception (inspect the enclosing block).

**L0070.** Assign to `oauth_state.used_at`: read/evaluate `now`. Assignment stores a value/reference; it is not an equality test.

**L0071.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0072.** Assign to `service`: construct a session-bound Gmail integration service: `GmailService(session)`. Assignment stores a value/reference; it is not an equality test.

**L0073.** Assign to `(access_token, refresh_token, expires_at)`: exchange a one-time authorization code for tokens and expiry: `service.exchange_code(code)`. Assignment stores a value/reference; it is not an equality test.

**L0074.** Assign to `email`: look up the authorized Google account email: `service.profile(access_token)`. Assignment stores a value/reference; it is not an equality test.

**L0075.** Perform the expression for its effect: encrypt and store this user's Gmail tokens: `service.save_connection(oauth_state.user_id, email, access_token, refresh_token, expires_at)`.

**L0076.** Continue the statement starting at L75 with `oauth_state.user_id, email, access_token, refresh_token, expires_at`. Perform the expression for its effect: encrypt and store this user's Gmail tokens: `service.save_connection(oauth_state.user_id, email, access_token, refresh_token, expires_at)`.

**L0077.** Close the grouped expression/declaration introduced at L75; delimiters/commas complete the same statement rather than execute a separate operation.

**L0078.** Assign to `params`: construct a dictionary mapping the displayed keys to values: `{'gmail': 'connected'}`. Assignment stores a value/reference; it is not an equality test.

**L0079.** Catch `RuntimeError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0080.** Assign to `params['reason']`: use literal value `'authorization_failed'` (str). Assignment stores a value/reference; it is not an equality test.

**L0081.** Assign to `params['detail']`: convert a value to its string representation: `str(exc)`. Assignment stores a value/reference; it is not an equality test.

**L0082.** Return from this function: construct an HTTP browser redirect rather than JSON data: `RedirectResponse(f'{settings.frontend_origin}/?{urlencode(params)}', status_code=302)`.

**L0083.** Continue the statement starting at L82 with `f"{settings.frontend_origin}/?{urlencode(params)}"`. Return from this function: construct an HTTP browser redirect rather than JSON data: `RedirectResponse(f'{settings.frontend_origin}/?{urlencode(params)}', status_code=302)`.

**L0084.** Continue the statement starting at L82 with `status_code=302`. Return from this function: construct an HTTP browser redirect rather than JSON data: `RedirectResponse(f'{settings.frontend_origin}/?{urlencode(params)}', status_code=302)`.

**L0085.** Close the grouped expression/declaration introduced at L82; delimiters/commas complete the same statement rather than execute a separate operation.

**L0086.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0087.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0088.** Apply/register the following definition with decorator `@router.get("/status")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0089.** Define function/method `gmail_status(session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `dict[str, object]`. 

**L0090.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0091.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0092.** Continue the function signature: `) -> dict[str, object]:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0093.** Assign to `user`: call `_require_user` with the displayed positional/named arguments: `_require_user(authenticated_user)`. Assignment stores a value/reference; it is not an equality test.

**L0094.** Assign to `connection`: look up the user's stored Gmail connection without returning token values to the frontend: `GmailService(session).connection(user.id)`. Assignment stores a value/reference; it is not an equality test.

**L0095.** Return from this function: construct a dictionary mapping the displayed keys to values: `{'connected': connection is not None, 'email': connection.email if connection else None}`.

**L0096.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0097.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0098.** Apply/register the following definition with decorator `@router.delete("")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0099.** Define function/method `disconnect_gmail(session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `None`. 

**L0100.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0101.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0102.** Close the grouped expression/declaration introduced at L99; delimiters/commas complete the same statement rather than execute a separate operation.

**L0103.** Assign to `user`: call `_require_user` with the displayed positional/named arguments: `_require_user(authenticated_user)`. Assignment stores a value/reference; it is not an equality test.

**L0104.** Perform the expression for its effect: delete the user's local Gmail connection: `GmailService(session).disconnect(user.id)`.


<a id="backend-app-api-routes-webhookspy"></a>
## backend/app/api/routes/webhooks.py

GitHub-only ingestion with optional configured HMAC verification. Raw bytes are authenticated before JSON parsing. Candidate selection spans all enabled webhook workflows; no tenant routing, delivery deduplication, request-size bound, or background queue exists.

Source fingerprint: `a12c24e7c266c9cfb89c7ecef4c98da6c1326833b89e2211f01ec06a3484283b`. Physical lines: 58.

### Numbered source

```python
0001 | import hashlib
0002 | import hmac
0003 | import json
0004 | 
0005 | from fastapi import APIRouter, Depends, Header, HTTPException, Request
0006 | from sqlalchemy.orm import Session
0007 | 
0008 | from app.core.event import Event
0009 | from app.config import settings
0010 | from app.db import get_session
0011 | from app.models import Workflow
0012 | from app.schemas.workflows import ExecutionResponse
0013 | from app.services.workflow import WorkflowService
0014 | 
0015 | router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])
0016 | 
0017 | 
0018 | @router.post("/{provider}", response_model=list[ExecutionResponse])
0019 | async def receive_webhook(
0020 |     provider: str,
0021 |     request: Request,
0022 |     session: Session = Depends(get_session),
0023 |     x_hub_signature_256: str | None = Header(default=None),
0024 | ) -> list[ExecutionResponse]:
0025 |     if provider != "github":
0026 |         raise HTTPException(status_code=404, detail="Unsupported webhook provider")
0027 |     raw_body = await request.body()
0028 |     if settings.github_webhook_secret:
0029 |         expected = "sha256=" + hmac.new(
0030 |             settings.github_webhook_secret.encode(),
0031 |             raw_body,
0032 |             hashlib.sha256,
0033 |         ).hexdigest()
0034 |         if not x_hub_signature_256 or not hmac.compare_digest(x_hub_signature_256, expected):
0035 |             raise HTTPException(status_code=401, detail="Invalid webhook signature")
0036 |     try:
0037 |         payload = json.loads(raw_body)
0038 |     except json.JSONDecodeError as exc:
0039 |         raise HTTPException(status_code=400, detail="Webhook payload must be valid JSON") from exc
0040 |     if not isinstance(payload, dict):
0041 |         raise HTTPException(status_code=400, detail="Webhook payload must be an object")
0042 |     service = WorkflowService(session)
0043 |     executions = []
0044 |     workflows = (
0045 |         session.query(Workflow)
0046 |         .filter(Workflow.enabled.is_(True))
0047 |         .all()
0048 |     )
0049 |     for workflow in workflows:
0050 |         if workflow.trigger is None or workflow.trigger.trigger_type != "webhook":
0051 |             continue
0052 |         executions.append(
0053 |             service.run_event(
0054 |                 workflow.id,
0055 |                 Event(type="webhook", source="github", payload=payload),
0056 |             )
0057 |         )
0058 |     return [ExecutionResponse.model_validate(item, from_attributes=True) for item in executions]
```

### Every-line explanation

**L0001.** Import module(s) `hashlib`. Top-level module code runs on first import.

**L0002.** Import module(s) `hmac`. Top-level module code runs on first import.

**L0003.** Import module(s) `json`. Top-level module code runs on first import.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import APIRouter, Depends, Header, HTTPException, Request from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import Session from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Import Event from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Import get_session from `app.db`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Import Workflow from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0012.** Import ExecutionResponse from `app.schemas.workflows`. Imported names become available in this module; aliases distinguish roles where used.

**L0013.** Import WorkflowService from `app.services.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Assign to `router`: call `APIRouter` with the displayed positional/named arguments: `APIRouter(prefix='/api/webhooks', tags=['webhooks'])`. Assignment stores a value/reference; it is not an equality test.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0018.** Apply/register the following definition with decorator `@router.post("/{provider}", response_model=list[ExecutionResponse])`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0019.** Define async function/method `receive_webhook(provider: str, request: Request, session: Session=Depends(get_session), x_hub_signature_256: str | None=Header(default=None))` with intended return type `list[ExecutionResponse]`. 

**L0020.** Continue the function signature: `provider: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0021.** Continue the function signature: `request: Request,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0022.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0023.** Continue the function signature: `x_hub_signature_256: str | None = Header(default=None),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0024.** Continue the function signature: `) -> list[ExecutionResponse]:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0025.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `provider != 'github'`; this produces the branch/assertion's truth value.

**L0026.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail='Unsupported webhook provider')`. Normal execution at this point stops.

**L0027.** Assign to `raw_body`: await coroutine `request.body()`, yielding this coroutine until the asynchronous operation completes. Assignment stores a value/reference; it is not an equality test.

**L0028.** Enter the following indented branch only if you read attribute `github_webhook_secret` from `settings`.

**L0029.** Assign to `expected`: compute `'sha256=' + hmac.new(settings.github_webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0030.** Continue the statement starting at L29 with `settings.github_webhook_secret.encode()`. Assign to `expected`: compute `'sha256=' + hmac.new(settings.github_webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0031.** Continue the statement starting at L29 with `raw_body`. Assign to `expected`: compute `'sha256=' + hmac.new(settings.github_webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0032.** Continue the statement starting at L29 with `hashlib.sha256`. Assign to `expected`: compute `'sha256=' + hmac.new(settings.github_webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0033.** Continue the statement starting at L29 with `).hexdigest()`. Assign to `expected`: compute `'sha256=' + hmac.new(settings.github_webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0034.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not x_hub_signature_256 or not hmac.compare_digest(x_hub_signature_256, expected)`; later terms run only when needed.

**L0035.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=401, detail='Invalid webhook signature')`. Normal execution at this point stops.

**L0036.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0037.** Assign to `payload`: parse JSON bytes/text into Python data, raising for invalid syntax: `json.loads(raw_body)`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Catch `json.JSONDecodeError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0039.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=400, detail='Webhook payload must be valid JSON')`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0040.** Enter the following indented branch only if you negate the truth value of `isinstance(payload, dict)`.

**L0041.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=400, detail='Webhook payload must be an object')`. Normal execution at this point stops.

**L0042.** Assign to `service`: construct the use-case service with its database session: `WorkflowService(session)`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Assign to `executions`: construct a list containing the displayed values: `[]`. Assignment stores a value/reference; it is not an equality test.

**L0044.** Assign to `workflows`: materialize all matching query rows (not paginated): `session.query(Workflow).filter(Workflow.enabled.is_(True)).all()`. Assignment stores a value/reference; it is not an equality test.

**L0045.** Continue the statement starting at L44 with `session.query(Workflow)`. Assign to `workflows`: materialize all matching query rows (not paginated): `session.query(Workflow).filter(Workflow.enabled.is_(True)).all()`. Assignment stores a value/reference; it is not an equality test.

**L0046.** Continue the statement starting at L44 with `.filter(Workflow.enabled.is_(True))`. Assign to `workflows`: materialize all matching query rows (not paginated): `session.query(Workflow).filter(Workflow.enabled.is_(True)).all()`. Assignment stores a value/reference; it is not an equality test.

**L0047.** Continue the statement starting at L44 with `.all()`. Assign to `workflows`: materialize all matching query rows (not paginated): `session.query(Workflow).filter(Workflow.enabled.is_(True)).all()`. Assignment stores a value/reference; it is not an equality test.

**L0048.** Close the grouped expression/declaration introduced at L44; delimiters/commas complete the same statement rather than execute a separate operation.

**L0049.** Iterate over `workflows`, binding each item/pair to `workflow`. The indented body runs once per item unless it returns/raises/breaks.

**L0050.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `workflow.trigger is None or workflow.trigger.trigger_type != 'webhook'`; later terms run only when needed.

**L0051.** Skip the rest of this loop iteration and move to the next item/attempt.

**L0052.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `executions.append(service.run_event(workflow.id, Event(type='webhook', source='github', payload=payload)))`.

**L0053.** Continue the statement starting at L52 with `service.run_event(`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `executions.append(service.run_event(workflow.id, Event(type='webhook', source='github', payload=payload)))`.

**L0054.** Continue the statement starting at L52 with `workflow.id`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `executions.append(service.run_event(workflow.id, Event(type='webhook', source='github', payload=payload)))`.

**L0055.** Continue the statement starting at L52 with `Event(type="webhook", source="github", payload=payload)`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `executions.append(service.run_event(workflow.id, Event(type='webhook', source='github', payload=payload)))`.

**L0056.** Close the grouped expression/declaration introduced at L52; delimiters/commas complete the same statement rather than execute a separate operation.

**L0057.** Close the grouped expression/declaration introduced at L52; delimiters/commas complete the same statement rather than execute a separate operation.

**L0058.** Return from this function: construct a new list by applying the displayed expression for each item in the comprehension: `[ExecutionResponse.model_validate(item, from_attributes=True) for item in executions]`.


<a id="backend-app-api-routes-workflowspy"></a>
## backend/app/api/routes/workflows.py

Resource routes enforce ownership when authentication is configured, translate errors, and call service/repository operations. _detail returns action config, including any stored GitHub token. The run route maps all ValueErrors to 404, including disabled workflow errors.

Source fingerprint: `bb8d83fb8006c38ba9f51f8a9c056095338a287b7bdce646119b127ae10e2619`. Physical lines: 152.

### Numbered source

```python
0001 | from fastapi import APIRouter, Depends, HTTPException, status
0002 | from sqlalchemy.orm import Session
0003 | 
0004 | from app.db import get_session
0005 | from app.api.auth import AuthenticatedUser, current_user
0006 | from app.models import User
0007 | from app.schemas.workflows import (
0008 |     ExecutionResponse,
0009 |     ManualRunRequest,
0010 |     WorkflowCreate,
0011 |     WorkflowDetailResponse,
0012 |     WorkflowResponse,
0013 |     WorkflowUpdate,
0014 | )
0015 | from app.services.workflow import WorkflowService
0016 | 
0017 | router = APIRouter(prefix="/api/workflows", tags=["workflows"])
0018 | 
0019 | 
0020 | def _detail(workflow) -> WorkflowDetailResponse:
0021 |     return WorkflowDetailResponse(
0022 |         id=workflow.id,
0023 |         user_id=workflow.user_id,
0024 |         name=workflow.name,
0025 |         enabled=workflow.enabled,
0026 |         trigger=(
0027 |             {"type": workflow.trigger.trigger_type, "config": workflow.trigger.config}
0028 |             if workflow.trigger else {"type": "manual", "config": {}}
0029 |         ),
0030 |         conditions=[
0031 |             {"type": item.condition_type, "config": item.config}
0032 |             for item in workflow.conditions
0033 |         ],
0034 |         actions=[
0035 |             {"type": item.action_type, "config": item.config}
0036 |             for item in workflow.actions
0037 |         ],
0038 |     )
0039 | 
0040 | 
0041 | @router.get("", response_model=list[WorkflowResponse])
0042 | def list_workflows(
0043 |     user_id: str,
0044 |     session: Session = Depends(get_session),
0045 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0046 | ) -> list[WorkflowResponse]:
0047 |     if authenticated_user is not None and authenticated_user.id != user_id:
0048 |         raise HTTPException(status_code=403, detail="Workflow ownership violation")
0049 |     workflows = WorkflowService(session).repository.list_for_user(user_id)
0050 |     return [WorkflowResponse.model_validate(item, from_attributes=True) for item in workflows]
0051 | 
0052 | 
0053 | @router.post("", response_model=WorkflowResponse, status_code=status.HTTP_201_CREATED)
0054 | def create_workflow(
0055 |     request: WorkflowCreate,
0056 |     session: Session = Depends(get_session),
0057 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0058 | ) -> WorkflowResponse:
0059 |     if authenticated_user is not None and authenticated_user.id != request.user_id:
0060 |         raise HTTPException(status_code=403, detail="Workflow ownership violation")
0061 |     try:
0062 |         if authenticated_user is not None and session.get(User, authenticated_user.id) is None:
0063 |             session.add(User(id=authenticated_user.id, email=authenticated_user.email))
0064 |             session.flush()
0065 |         workflow = WorkflowService(session).create(request)
0066 |     except ValueError as exc:
0067 |         raise HTTPException(status_code=400, detail=str(exc)) from exc
0068 |     return WorkflowResponse.model_validate(workflow, from_attributes=True)
0069 | 
0070 | 
0071 | @router.put("/{workflow_id}", response_model=WorkflowDetailResponse)
0072 | def update_workflow(
0073 |     workflow_id: str,
0074 |     request: WorkflowUpdate,
0075 |     session: Session = Depends(get_session),
0076 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0077 | ) -> WorkflowDetailResponse:
0078 |     workflow = WorkflowService(session).repository.get(workflow_id)
0079 |     if workflow is None:
0080 |         raise HTTPException(status_code=404, detail="Workflow not found")
0081 |     if authenticated_user is not None and workflow.user_id != authenticated_user.id:
0082 |         raise HTTPException(status_code=403, detail="Workflow ownership violation")
0083 |     try:
0084 |         updated = WorkflowService(session).update(workflow_id, request)
0085 |     except ValueError as exc:
0086 |         raise HTTPException(status_code=400, detail=str(exc)) from exc
0087 |     return _detail(updated)
0088 | 
0089 | 
0090 | @router.delete("/{workflow_id}", status_code=status.HTTP_204_NO_CONTENT)
0091 | def delete_workflow(
0092 |     workflow_id: str,
0093 |     session: Session = Depends(get_session),
0094 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0095 | ) -> None:
0096 |     workflow = WorkflowService(session).repository.get(workflow_id)
0097 |     if workflow is None:
0098 |         raise HTTPException(status_code=404, detail="Workflow not found")
0099 |     if authenticated_user is not None and workflow.user_id != authenticated_user.id:
0100 |         raise HTTPException(status_code=403, detail="Workflow ownership violation")
0101 |     try:
0102 |         WorkflowService(session).delete(workflow_id)
0103 |     except ValueError as exc:
0104 |         raise HTTPException(status_code=404, detail=str(exc)) from exc
0105 | 
0106 | 
0107 | @router.get("/{workflow_id}", response_model=WorkflowDetailResponse)
0108 | def get_workflow(
0109 |     workflow_id: str,
0110 |     session: Session = Depends(get_session),
0111 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0112 | ) -> WorkflowResponse:
0113 |     workflow = WorkflowService(session).repository.get(workflow_id)
0114 |     if workflow is None:
0115 |         raise HTTPException(status_code=404, detail="Workflow not found")
0116 |     if authenticated_user is not None and workflow.user_id != authenticated_user.id:
0117 |         raise HTTPException(status_code=403, detail="Workflow ownership violation")
0118 |     return _detail(workflow)
0119 | 
0120 | 
0121 | @router.get("/{workflow_id}/executions", response_model=list[ExecutionResponse])
0122 | def list_executions(
0123 |     workflow_id: str,
0124 |     session: Session = Depends(get_session),
0125 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0126 | ) -> list[ExecutionResponse]:
0127 |     workflow = WorkflowService(session).repository.get(workflow_id)
0128 |     if workflow is None:
0129 |         raise HTTPException(status_code=404, detail="Workflow not found")
0130 |     if authenticated_user is not None and workflow.user_id != authenticated_user.id:
0131 |         raise HTTPException(status_code=403, detail="Workflow ownership violation")
0132 |     executions = WorkflowService(session).repository.executions(workflow_id)
0133 |     return [ExecutionResponse.model_validate(item, from_attributes=True) for item in executions]
0134 | 
0135 | 
0136 | @router.post("/{workflow_id}/run", response_model=ExecutionResponse)
0137 | def run_workflow(
0138 |     workflow_id: str,
0139 |     request: ManualRunRequest,
0140 |     session: Session = Depends(get_session),
0141 |     authenticated_user: AuthenticatedUser | None = Depends(current_user),
0142 | ) -> ExecutionResponse:
0143 |     try:
0144 |         workflow = WorkflowService(session).repository.get(workflow_id)
0145 |         if workflow is None:
0146 |             raise ValueError("Workflow not found")
0147 |         if authenticated_user is not None and workflow.user_id != authenticated_user.id:
0148 |             raise HTTPException(status_code=403, detail="Workflow ownership violation")
0149 |         execution = WorkflowService(session).run_manual(workflow_id, request.payload)
0150 |     except ValueError as exc:
0151 |         raise HTTPException(status_code=404, detail=str(exc)) from exc
0152 |     return ExecutionResponse.model_validate(execution, from_attributes=True)
```

### Every-line explanation

**L0001.** Import APIRouter, Depends, HTTPException, status from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Session from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import get_session from `app.db`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import AuthenticatedUser, current_user from `app.api.auth`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import User from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import ExecutionResponse, ManualRunRequest, WorkflowCreate, WorkflowDetailResponse, WorkflowResponse, WorkflowUpdate from `app.schemas.workflows`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Continue the parenthesized import from `app.schemas.workflows` with name(s) `ExecutionResponse`.

**L0009.** Continue the parenthesized import from `app.schemas.workflows` with name(s) `ManualRunRequest`.

**L0010.** Continue the parenthesized import from `app.schemas.workflows` with name(s) `WorkflowCreate`.

**L0011.** Continue the parenthesized import from `app.schemas.workflows` with name(s) `WorkflowDetailResponse`.

**L0012.** Continue the parenthesized import from `app.schemas.workflows` with name(s) `WorkflowResponse`.

**L0013.** Continue the parenthesized import from `app.schemas.workflows` with name(s) `WorkflowUpdate`.

**L0014.** Close the grouped expression/declaration introduced at L7; delimiters/commas complete the same statement rather than execute a separate operation.

**L0015.** Import WorkflowService from `app.services.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Assign to `router`: call `APIRouter` with the displayed positional/named arguments: `APIRouter(prefix='/api/workflows', tags=['workflows'])`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Define function/method `_detail(workflow)` with intended return type `WorkflowDetailResponse`. 

**L0021.** Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0022.** Continue the statement starting at L21 with `id=workflow.id`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0023.** Continue the statement starting at L21 with `user_id=workflow.user_id`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0024.** Continue the statement starting at L21 with `name=workflow.name`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0025.** Continue the statement starting at L21 with `enabled=workflow.enabled`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0026.** Continue the statement starting at L21 with `trigger=(`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0027.** Continue the statement starting at L21 with `{"type": workflow.trigger.trigger_type, "config": workflow.trigger.config}`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0028.** Continue the statement starting at L21 with `if workflow.trigger else {"type": "manual", "config": {}}`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0029.** Close the grouped expression/declaration introduced at L21; delimiters/commas complete the same statement rather than execute a separate operation.

**L0030.** Continue the statement starting at L21 with `conditions=[`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0031.** Continue the statement starting at L21 with `{"type": item.condition_type, "config": item.config}`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0032.** Continue the statement starting at L21 with `for item in workflow.conditions`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0033.** Close the grouped expression/declaration introduced at L21; delimiters/commas complete the same statement rather than execute a separate operation.

**L0034.** Continue the statement starting at L21 with `actions=[`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0035.** Continue the statement starting at L21 with `{"type": item.action_type, "config": item.config}`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0036.** Continue the statement starting at L21 with `for item in workflow.actions`. Return from this function: construct/validate editable workflow response data: `WorkflowDetailResponse(id=workflow.id, user_id=workflow.user_id, name=workflow.name, enabled=workflow.enabled, trigger={'type': workflow.trigger.trigger_type, 'config': workflow.trigger.config} if workflow.trigger else {'type': 'manual', 'config': {}}, conditions=[{'type': item.condition_type, 'config': item.config} for item in workflow.conditions], actions=[{'type': item.action_type, 'config': item.config} for item in workflow.actions])`.

**L0037.** Close the grouped expression/declaration introduced at L21; delimiters/commas complete the same statement rather than execute a separate operation.

**L0038.** Close the grouped expression/declaration introduced at L21; delimiters/commas complete the same statement rather than execute a separate operation.

**L0039.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0040.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0041.** Apply/register the following definition with decorator `@router.get("", response_model=list[WorkflowResponse])`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0042.** Define function/method `list_workflows(user_id: str, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `list[WorkflowResponse]`. 

**L0043.** Continue the function signature: `user_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0044.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0045.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0046.** Continue the function signature: `) -> list[WorkflowResponse]:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0047.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and authenticated_user.id != user_id`; later terms run only when needed.

**L0048.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0049.** Assign to `workflows`: call `WorkflowService(session).repository.list_for_user` with the displayed positional/named arguments: `WorkflowService(session).repository.list_for_user(user_id)`. Assignment stores a value/reference; it is not an equality test.

**L0050.** Return from this function: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowResponse.model_validate(item, from_attributes=True) for item in workflows]`.

**L0051.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0052.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0053.** Apply/register the following definition with decorator `@router.post("", response_model=WorkflowResponse, status_code=status.HTTP_201_CREATED)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0054.** Define function/method `create_workflow(request: WorkflowCreate, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `WorkflowResponse`. 

**L0055.** Continue the function signature: `request: WorkflowCreate,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0056.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0057.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0058.** Continue the function signature: `) -> WorkflowResponse:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0059.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and authenticated_user.id != request.user_id`; later terms run only when needed.

**L0060.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0061.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0062.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and session.get(User, authenticated_user.id) is None`; later terms run only when needed.

**L0063.** Perform the expression for its effect: stage an ORM object for persistence in the current session: `session.add(User(id=authenticated_user.id, email=authenticated_user.email))`.

**L0064.** Perform the expression for its effect: send pending SQL in the current transaction without committing: `session.flush()`.

**L0065.** Assign to `workflow`: construct a component through a factory, or call a service create use case as identified by receiver: `WorkflowService(session).create(request)`. Assignment stores a value/reference; it is not an equality test.

**L0066.** Catch `ValueError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0067.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=400, detail=str(exc))`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0068.** Return from this function: validate/serialize the input with this Pydantic response model; from_attributes reads ORM attributes: `WorkflowResponse.model_validate(workflow, from_attributes=True)`.

**L0069.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0070.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0071.** Apply/register the following definition with decorator `@router.put("/{workflow_id}", response_model=WorkflowDetailResponse)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0072.** Define function/method `update_workflow(workflow_id: str, request: WorkflowUpdate, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `WorkflowDetailResponse`. 

**L0073.** Continue the function signature: `workflow_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0074.** Continue the function signature: `request: WorkflowUpdate,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0075.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0076.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0077.** Continue the function signature: `) -> WorkflowDetailResponse:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0078.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `WorkflowService(session).repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0079.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0080.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail='Workflow not found')`. Normal execution at this point stops.

**L0081.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and workflow.user_id != authenticated_user.id`; later terms run only when needed.

**L0082.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0083.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0084.** Assign to `updated`: call `WorkflowService(session).update` with the displayed positional/named arguments: `WorkflowService(session).update(workflow_id, request)`. Assignment stores a value/reference; it is not an equality test.

**L0085.** Catch `ValueError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0086.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=400, detail=str(exc))`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0087.** Return from this function: call `_detail` with the displayed positional/named arguments: `_detail(updated)`.

**L0088.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0089.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0090.** Apply/register the following definition with decorator `@router.delete("/{workflow_id}", status_code=status.HTTP_204_NO_CONTENT)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0091.** Define function/method `delete_workflow(workflow_id: str, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `None`. 

**L0092.** Continue the function signature: `workflow_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0093.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0094.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0095.** Close the grouped expression/declaration introduced at L91; delimiters/commas complete the same statement rather than execute a separate operation.

**L0096.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `WorkflowService(session).repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0097.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0098.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail='Workflow not found')`. Normal execution at this point stops.

**L0099.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and workflow.user_id != authenticated_user.id`; later terms run only when needed.

**L0100.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0101.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0102.** Perform the expression for its effect: call `WorkflowService(session).delete` with the displayed positional/named arguments: `WorkflowService(session).delete(workflow_id)`.

**L0103.** Catch `ValueError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0104.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail=str(exc))`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0105.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0106.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0107.** Apply/register the following definition with decorator `@router.get("/{workflow_id}", response_model=WorkflowDetailResponse)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0108.** Define function/method `get_workflow(workflow_id: str, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `WorkflowResponse`. 

**L0109.** Continue the function signature: `workflow_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0110.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0111.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0112.** Continue the function signature: `) -> WorkflowResponse:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0113.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `WorkflowService(session).repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0114.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0115.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail='Workflow not found')`. Normal execution at this point stops.

**L0116.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and workflow.user_id != authenticated_user.id`; later terms run only when needed.

**L0117.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0118.** Return from this function: call `_detail` with the displayed positional/named arguments: `_detail(workflow)`.

**L0119.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0120.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0121.** Apply/register the following definition with decorator `@router.get("/{workflow_id}/executions", response_model=list[ExecutionResponse])`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0122.** Define function/method `list_executions(workflow_id: str, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `list[ExecutionResponse]`. 

**L0123.** Continue the function signature: `workflow_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0124.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0125.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0126.** Continue the function signature: `) -> list[ExecutionResponse]:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0127.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `WorkflowService(session).repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0128.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0129.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail='Workflow not found')`. Normal execution at this point stops.

**L0130.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and workflow.user_id != authenticated_user.id`; later terms run only when needed.

**L0131.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0132.** Assign to `executions`: call `WorkflowService(session).repository.executions` with the displayed positional/named arguments: `WorkflowService(session).repository.executions(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0133.** Return from this function: construct a new list by applying the displayed expression for each item in the comprehension: `[ExecutionResponse.model_validate(item, from_attributes=True) for item in executions]`.

**L0134.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0135.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0136.** Apply/register the following definition with decorator `@router.post("/{workflow_id}/run", response_model=ExecutionResponse)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0137.** Define function/method `run_workflow(workflow_id: str, request: ManualRunRequest, session: Session=Depends(get_session), authenticated_user: AuthenticatedUser | None=Depends(current_user))` with intended return type `ExecutionResponse`. 

**L0138.** Continue the function signature: `workflow_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0139.** Continue the function signature: `request: ManualRunRequest,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0140.** Continue the function signature: `session: Session = Depends(get_session),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0141.** Continue the function signature: `authenticated_user: AuthenticatedUser | None = Depends(current_user),`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0142.** Continue the function signature: `) -> ExecutionResponse:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0143.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0144.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `WorkflowService(session).repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0145.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0146.** Raise construct an invalid value/configuration exception: `ValueError('Workflow not found')`. Normal execution at this point stops.

**L0147.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `authenticated_user is not None and workflow.user_id != authenticated_user.id`; later terms run only when needed.

**L0148.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=403, detail='Workflow ownership violation')`. Normal execution at this point stops.

**L0149.** Assign to `execution`: wrap a request payload in a normalized manual Event and run it: `WorkflowService(session).run_manual(workflow_id, request.payload)`. Assignment stores a value/reference; it is not an equality test.

**L0150.** Catch `ValueError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0151.** Raise construct an HTTP-level rejection with a status and user-facing detail: `HTTPException(status_code=404, detail=str(exc))`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0152.** Return from this function: validate/serialize the input with this Pydantic response model; from_attributes reads ORM attributes: `ExecutionResponse.model_validate(execution, from_attributes=True)`.


<a id="backend-app-configpy"></a>
## backend/app/config.py

Typed application settings. BaseSettings loads backend/.env by a file-relative absolute path and environment values; the guide never reads that file. Defaults are development choices, not proof that production is securely configured.

Source fingerprint: `f834bc21a612fb1ea56cb6e2c7c98a956ef69b6b0278e587de860e4ff755931e`. Physical lines: 31.

### Numbered source

```python
0001 | from pathlib import Path
0002 | 
0003 | from pydantic_settings import BaseSettings, SettingsConfigDict
0004 | 
0005 | 
0006 | class Settings(BaseSettings):
0007 |     model_config = SettingsConfigDict(
0008 |         env_file=Path(__file__).resolve().parents[1] / ".env",
0009 |         extra="ignore",
0010 |     )
0011 | 
0012 |     database_url: str = "sqlite:///./flowforge.db"
0013 |     supabase_url: str = ""
0014 |     supabase_anon_key: str = ""
0015 |     http_action_timeout_seconds: float = 10.0
0016 |     http_action_max_payload_bytes: int = 64_000
0017 |     http_action_max_retries: int = 2
0018 |     github_webhook_secret: str = ""
0019 |     frontend_origin: str = "http://localhost:5173"
0020 |     email_provider: str = "resend"
0021 |     email_api_key: str = ""
0022 |     email_from: str = ""
0023 |     email_max_recipients: int = 50
0024 |     email_max_message_bytes: int = 100_000
0025 |     google_client_id: str = ""
0026 |     google_client_secret: str = ""
0027 |     google_redirect_uri: str = "http://localhost:8000/api/integrations/gmail/callback"
0028 |     token_encryption_key: str = ""
0029 | 
0030 | 
0031 | settings = Settings()
```

### Every-line explanation

**L0001.** Import Path from `pathlib`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import BaseSettings, SettingsConfigDict from `pydantic_settings`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `Settings` inheriting `BaseSettings`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Assign to `model_config`: call `SettingsConfigDict` with the displayed positional/named arguments: `SettingsConfigDict(env_file=Path(__file__).resolve().parents[1] / '.env', extra='ignore')`. Assignment stores a value/reference; it is not an equality test.

**L0008.** Continue the statement starting at L7 with `env_file=Path(__file__).resolve().parents[1] / ".env"`. Assign to `model_config`: call `SettingsConfigDict` with the displayed positional/named arguments: `SettingsConfigDict(env_file=Path(__file__).resolve().parents[1] / '.env', extra='ignore')`. Assignment stores a value/reference; it is not an equality test.

**L0009.** Continue the statement starting at L7 with `extra="ignore"`. Assign to `model_config`: call `SettingsConfigDict` with the displayed positional/named arguments: `SettingsConfigDict(env_file=Path(__file__).resolve().parents[1] / '.env', extra='ignore')`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Close the grouped expression/declaration introduced at L7; delimiters/commas complete the same statement rather than execute a separate operation.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Declare `database_url` with intended type `str` and initialize it: use literal value `'sqlite:///./flowforge.db'` (str).

**L0013.** Declare `supabase_url` with intended type `str` and initialize it: use literal value `''` (str).

**L0014.** Declare `supabase_anon_key` with intended type `str` and initialize it: use literal value `''` (str).

**L0015.** Declare `http_action_timeout_seconds` with intended type `float` and initialize it: use literal value `10.0` (float).

**L0016.** Declare `http_action_max_payload_bytes` with intended type `int` and initialize it: use literal value `64000` (int).

**L0017.** Declare `http_action_max_retries` with intended type `int` and initialize it: use literal value `2` (int).

**L0018.** Declare `github_webhook_secret` with intended type `str` and initialize it: use literal value `''` (str).

**L0019.** Declare `frontend_origin` with intended type `str` and initialize it: use literal value `'http://localhost:5173'` (str).

**L0020.** Declare `email_provider` with intended type `str` and initialize it: use literal value `'resend'` (str).

**L0021.** Declare `email_api_key` with intended type `str` and initialize it: use literal value `''` (str).

**L0022.** Declare `email_from` with intended type `str` and initialize it: use literal value `''` (str).

**L0023.** Declare `email_max_recipients` with intended type `int` and initialize it: use literal value `50` (int).

**L0024.** Declare `email_max_message_bytes` with intended type `int` and initialize it: use literal value `100000` (int).

**L0025.** Declare `google_client_id` with intended type `str` and initialize it: use literal value `''` (str).

**L0026.** Declare `google_client_secret` with intended type `str` and initialize it: use literal value `''` (str).

**L0027.** Declare `google_redirect_uri` with intended type `str` and initialize it: use literal value `'http://localhost:8000/api/integrations/gmail/callback'` (str).

**L0028.** Declare `token_encryption_key` with intended type `str` and initialize it: use literal value `''` (str).

**L0029.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0030.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0031.** Assign to `settings`: call `Settings` with the displayed positional/named arguments: `Settings()`. Assignment stores a value/reference; it is not an equality test.


<a id="backend-app-core-initpy"></a>
## backend/app/core/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `71849a820b70d953f177023bbda28ef20cb00721d7b62815e632c483e1f710b6`. Physical lines: 17.

### Numbered source

```python
0001 | from app.core.actions import Action, NoOpAction
0002 | from app.core.conditions import Condition, EqualsCondition
0003 | from app.core.event import Event, ExecutionContext
0004 | from app.core.triggers import ManualTrigger, Trigger
0005 | from app.core.workflow import Workflow
0006 | 
0007 | __all__ = [
0008 |     "Action",
0009 |     "Condition",
0010 |     "EqualsCondition",
0011 |     "Event",
0012 |     "ExecutionContext",
0013 |     "ManualTrigger",
0014 |     "NoOpAction",
0015 |     "Trigger",
0016 |     "Workflow",
0017 | ]
```

### Every-line explanation

**L0001.** Import Action, NoOpAction from `app.core.actions`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Condition, EqualsCondition from `app.core.conditions`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import Event, ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import ManualTrigger, Trigger from `app.core.triggers`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import Workflow from `app.core.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0008.** Continue the statement starting at L7 with `"Action"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0009.** Continue the statement starting at L7 with `"Condition"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Continue the statement starting at L7 with `"EqualsCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Continue the statement starting at L7 with `"Event"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0012.** Continue the statement starting at L7 with `"ExecutionContext"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0013.** Continue the statement starting at L7 with `"ManualTrigger"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Continue the statement starting at L7 with `"NoOpAction"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Continue the statement starting at L7 with `"Trigger"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0016.** Continue the statement starting at L7 with `"Workflow"`. Assign to `__all__`: construct a list containing the displayed values: `['Action', 'Condition', 'EqualsCondition', 'Event', 'ExecutionContext', 'ManualTrigger', 'NoOpAction', 'Trigger', 'Workflow']`. Assignment stores a value/reference; it is not an equality test.

**L0017.** Close the grouped expression/declaration introduced at L7; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-core-actions-initpy"></a>
## backend/app/core/actions/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `ee85d99aa314b1bf452a52f13716b0bb170fcb7d927bc5e8294879297340e4e4`. Physical lines: 7.

### Numbered source

```python
0001 | from app.core.actions.base import Action
0002 | from app.core.actions.github import GitHubAction
0003 | from app.core.actions.http import HttpAction
0004 | from app.core.actions.email import EmailAction
0005 | from app.core.actions.noop import NoOpAction
0006 | 
0007 | __all__ = ["Action", "EmailAction", "GitHubAction", "HttpAction", "NoOpAction"]
```

### Every-line explanation

**L0001.** Import Action from `app.core.actions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import GitHubAction from `app.core.actions.github`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import HttpAction from `app.core.actions.http`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import EmailAction from `app.core.actions.email`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import NoOpAction from `app.core.actions.noop`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Assign to `__all__`: construct a list containing the displayed values: `['Action', 'EmailAction', 'GitHubAction', 'HttpAction', 'NoOpAction']`. Assignment stores a value/reference; it is not an equality test.


<a id="backend-app-core-actions-basepy"></a>
## backend/app/core/actions/base.py

Action's small abstract contract. Subclasses implement execute(context); an action produces a side effect or context mutation, while the engine creates the final result.

Source fingerprint: `3702061146e7accb47d449c87d58b525e24f70359ffe2187f91a3e05fe152efa`. Physical lines: 9.

### Numbered source

```python
0001 | from abc import ABC, abstractmethod
0002 | 
0003 | from app.core.event import ExecutionContext
0004 | 
0005 | 
0006 | class Action(ABC):
0007 |     @abstractmethod
0008 |     def execute(self, context: ExecutionContext) -> None:
0009 |         """Perform the side effect."""
```

### Every-line explanation

**L0001.** Import ABC, abstractmethod from `abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `Action` inheriting `ABC`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Mark the next method as required by the ABC mechanism before a subclass can normally be instantiated.

**L0008.** Define function/method `execute(self, context: ExecutionContext)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0009.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.


<a id="backend-app-core-actions-emailpy"></a>
## backend/app/core/actions/email.py

Shared input validation with globally selected Resend/Gmail behavior. Resend has request-size checking/retries; Gmail delegates to GmailService and lacks the same send retry/message-size check. A basic regex is not proof that a mailbox exists.

Source fingerprint: `33bea9070ca0b00a962d3c74c5570a31dcfe7e17566c9a4c2024076aebcfb251`. Physical lines: 120.

### Numbered source

```python
0001 | import re
0002 | from collections.abc import Mapping
0003 | from email.utils import parseaddr
0004 | 
0005 | import httpx
0006 | 
0007 | from app.config import settings
0008 | from app.core.actions.base import Action
0009 | from app.core.event import ExecutionContext
0010 | from app.services.gmail import GmailService
0011 | 
0012 | EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
0013 | 
0014 | 
0015 | def _validate_email(value: object, field: str) -> str:
0016 |     if not isinstance(value, str) or not EMAIL_PATTERN.fullmatch(parseaddr(value)[1]):
0017 |         raise ValueError(f"{field} must be a valid email address")
0018 |     return value
0019 | 
0020 | 
0021 | class EmailAction(Action):
0022 |     def __init__(
0023 |         self, config: Mapping[str, object], gmail_service: GmailService | None = None
0024 |     ) -> None:
0025 |         if settings.email_provider not in {"resend", "gmail"}:
0026 |             raise ValueError("Unsupported email provider")
0027 |         if settings.email_provider == "resend" and not settings.email_api_key:
0028 |             raise ValueError("Email provider is not configured")
0029 |         if settings.email_provider == "gmail" and gmail_service is None:
0030 |             gmail_service = None
0031 |         self.gmail_service = gmail_service
0032 | 
0033 |         sender = config.get("from", settings.email_from)
0034 |         self.sender = _validate_email(sender, "from") if settings.email_provider == "resend" else None
0035 |         recipients = config.get("to")
0036 |         if isinstance(recipients, str):
0037 |             recipients = [recipients]
0038 |         if not isinstance(recipients, list) or not recipients:
0039 |             raise ValueError("to must contain at least one recipient")
0040 |         if len(recipients) > settings.email_max_recipients:
0041 |             raise ValueError("Too many email recipients")
0042 |         self.recipients = [_validate_email(item, "recipient") for item in recipients]
0043 | 
0044 |         subject = config.get("subject")
0045 |         if not isinstance(subject, str) or not subject.strip() or len(subject) > 200:
0046 |             raise ValueError("subject must be between 1 and 200 characters")
0047 |         self.subject = subject
0048 |         text = config.get("text", "")
0049 |         html = config.get("html")
0050 |         if not isinstance(text, str) or not isinstance(html, (str, type(None))):
0051 |             raise ValueError("text and html must be strings")
0052 |         if not text and not html:
0053 |             raise ValueError("Email requires text or html content")
0054 |         self.text = text
0055 |         self.html = html
0056 | 
0057 |     def execute(self, context: ExecutionContext) -> None:
0058 |         if settings.email_provider == "gmail":
0059 |             if self.gmail_service is None or context.user_id is None:
0060 |                 raise RuntimeError("Gmail email action requires an authenticated workflow owner")
0061 |             result = self.gmail_service.send(
0062 |                 context.user_id,
0063 |                 self.recipients,
0064 |                 self.subject,
0065 |                 self.text,
0066 |                 self.html,
0067 |                 self.sender,
0068 |             )
0069 |             context.data.setdefault("action_results", []).append(result)
0070 |             return
0071 |         payload: dict[str, object] = {
0072 |             "from": self.sender,
0073 |             "to": self.recipients,
0074 |             "subject": self.subject,
0075 |         }
0076 |         if self.text:
0077 |             payload["text"] = self.text
0078 |         if self.html:
0079 |             payload["html"] = self.html
0080 |         request = httpx.Request(
0081 |             "POST",
0082 |             "https://api.resend.com/emails",
0083 |             headers={
0084 |                 "Authorization": f"Bearer {settings.email_api_key}",
0085 |                 "Content-Type": "application/json",
0086 |             },
0087 |             json=payload,
0088 |         )
0089 |         if len(request.content) > settings.email_max_message_bytes:
0090 |             raise ValueError("Email message is too large")
0091 |         response = None
0092 |         for attempt in range(settings.http_action_max_retries + 1):
0093 |             try:
0094 |                 with httpx.Client(timeout=settings.http_action_timeout_seconds) as client:
0095 |                     response = client.send(request)
0096 |             except httpx.TransportError:
0097 |                 if attempt == settings.http_action_max_retries:
0098 |                     raise RuntimeError("Email provider network request failed") from None
0099 |                 continue
0100 |             if response.status_code < 500 or attempt == settings.http_action_max_retries:
0101 |                 break
0102 |         if response is None:
0103 |             raise RuntimeError("Email provider did not return a response")
0104 |         if response.is_error:
0105 |             raise RuntimeError(f"Email provider returned status {response.status_code}")
0106 |         provider_id = None
0107 |         try:
0108 |             response_data = response.json()
0109 |             if isinstance(response_data, dict) and isinstance(response_data.get("id"), str):
0110 |                 provider_id = response_data["id"]
0111 |         except ValueError:
0112 |             pass
0113 |         result: dict[str, object] = {
0114 |             "type": "email",
0115 |             "provider": settings.email_provider,
0116 |             "status_code": response.status_code,
0117 |         }
0118 |         if provider_id:
0119 |             result["provider_id"] = provider_id
0120 |         context.data.setdefault("action_results", []).append(result)
```

### Every-line explanation

**L0001.** Import module(s) `re`. Top-level module code runs on first import.

**L0002.** Import Mapping from `collections.abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import parseaddr from `email.utils`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import module(s) `httpx`. Top-level module code runs on first import.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Import Action from `app.core.actions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Import GmailService from `app.services.gmail`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Compile a basic anchored email-shape regex. Raw string syntax preserves backslashes for the regex; this is not full email-standard validation.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Define function/method `_validate_email(value: object, field: str)` with intended return type `str`. 

**L0016.** Require a string and check the address extracted by parseaddr with a full match. The original value is returned, not the parsed address.

**L0017.** Raise construct an invalid value/configuration exception: `ValueError(f'{field} must be a valid email address')`. Normal execution at this point stops.

**L0018.** Return from this function: read/evaluate `value`.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Define class `EmailAction` inheriting `Action`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0022.** Define function/method `__init__(self, config: Mapping[str, object], gmail_service: GmailService | None=None)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0023.** Continue the function signature: `self, config: Mapping[str, object], gmail_service: GmailService | None = None`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0024.** Close the grouped expression/declaration introduced at L22; delimiters/commas complete the same statement rather than execute a separate operation.

**L0025.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `settings.email_provider not in {'resend', 'gmail'}`; this produces the branch/assertion's truth value.

**L0026.** Raise construct an invalid value/configuration exception: `ValueError('Unsupported email provider')`. Normal execution at this point stops.

**L0027.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `settings.email_provider == 'resend' and (not settings.email_api_key)`; later terms run only when needed.

**L0028.** Raise construct an invalid value/configuration exception: `ValueError('Email provider is not configured')`. Normal execution at this point stops.

**L0029.** This condition checks for absent Gmail service but the following assignment changes nothing.

**L0030.** Redundant assignment of None to a value already None; actual rejection occurs in execute.

**L0031.** Assign to `self.gmail_service`: read/evaluate `gmail_service`. Assignment stores a value/reference; it is not an equality test.

**L0032.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0033.** Assign to `sender`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('from', settings.email_from)`. Assignment stores a value/reference; it is not an equality test.

**L0034.** Validate sender only for Resend; Gmail sends from the account connection and keeps sender as None here.

**L0035.** Assign to `recipients`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('to')`. Assignment stores a value/reference; it is not an equality test.

**L0036.** Enter the following indented branch only if you perform an actual runtime type check: `isinstance(recipients, str)`.

**L0037.** Assign to `recipients`: construct a list containing the displayed values: `[recipients]`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(recipients, list) or not recipients`; later terms run only when needed.

**L0039.** Raise construct an invalid value/configuration exception: `ValueError('to must contain at least one recipient')`. Normal execution at this point stops.

**L0040.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `len(recipients) > settings.email_max_recipients`; this produces the branch/assertion's truth value.

**L0041.** Raise construct an invalid value/configuration exception: `ValueError('Too many email recipients')`. Normal execution at this point stops.

**L0042.** Assign to `self.recipients`: construct a new list by applying the displayed expression for each item in the comprehension: `[_validate_email(item, 'recipient') for item in recipients]`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0044.** Assign to `subject`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('subject')`. Assignment stores a value/reference; it is not an equality test.

**L0045.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(subject, str) or not subject.strip() or len(subject) > 200`; later terms run only when needed.

**L0046.** Raise construct an invalid value/configuration exception: `ValueError('subject must be between 1 and 200 characters')`. Normal execution at this point stops.

**L0047.** Assign to `self.subject`: read/evaluate `subject`. Assignment stores a value/reference; it is not an equality test.

**L0048.** Assign to `text`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('text', '')`. Assignment stores a value/reference; it is not an equality test.

**L0049.** Assign to `html`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('html')`. Assignment stores a value/reference; it is not an equality test.

**L0050.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(text, str) or not isinstance(html, (str, type(None)))`; later terms run only when needed.

**L0051.** Raise construct an invalid value/configuration exception: `ValueError('text and html must be strings')`. Normal execution at this point stops.

**L0052.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not text and (not html)`; later terms run only when needed.

**L0053.** Raise construct an invalid value/configuration exception: `ValueError('Email requires text or html content')`. Normal execution at this point stops.

**L0054.** Assign to `self.text`: read/evaluate `text`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Assign to `self.html`: read/evaluate `html`. Assignment stores a value/reference; it is not an equality test.

**L0056.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0057.** Define function/method `execute(self, context: ExecutionContext)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0058.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `settings.email_provider == 'gmail'`; this produces the branch/assertion's truth value.

**L0059.** For Gmail, require both the injected service and a workflow owner in context before attempting a send.

**L0060.** Raise construct an execution/integration failure exception: `RuntimeError('Gmail email action requires an authenticated workflow owner')`. Normal execution at this point stops.

**L0061.** Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0062.** Continue the statement starting at L61 with `context.user_id`. Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0063.** Continue the statement starting at L61 with `self.recipients`. Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0064.** Continue the statement starting at L61 with `self.subject`. Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0065.** Continue the statement starting at L61 with `self.text`. Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0066.** Continue the statement starting at L61 with `self.html`. Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0067.** Continue the statement starting at L61 with `self.sender`. Assign to `result`: invoke the receiver's delivery/send operation: `self.gmail_service.send(context.user_id, self.recipients, self.subject, self.text, self.html, self.sender)`. Assignment stores a value/reference; it is not an equality test.

**L0068.** Close the grouped expression/declaration introduced at L61; delimiters/commas complete the same statement rather than execute a separate operation.

**L0069.** Append the Gmail result to transient context data, not directly to the execution table.

**L0070.** Return immediately without a value (None), skipping the remaining function body.

**L0071.** Declare `payload` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'from': self.sender, 'to': self.recipients, 'subject': self.subject}`.

**L0072.** Continue the statement starting at L71 with `"from": self.sender`. Declare `payload` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'from': self.sender, 'to': self.recipients, 'subject': self.subject}`.

**L0073.** Continue the statement starting at L71 with `"to": self.recipients`. Declare `payload` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'from': self.sender, 'to': self.recipients, 'subject': self.subject}`.

**L0074.** Continue the statement starting at L71 with `"subject": self.subject`. Declare `payload` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'from': self.sender, 'to': self.recipients, 'subject': self.subject}`.

**L0075.** Close the grouped expression/declaration introduced at L71; delimiters/commas complete the same statement rather than execute a separate operation.

**L0076.** Enter the following indented branch only if you read attribute `text` from `self`.

**L0077.** Assign to `payload['text']`: read attribute `text` from `self`. Assignment stores a value/reference; it is not an equality test.

**L0078.** Enter the following indented branch only if you read attribute `html` from `self`.

**L0079.** Assign to `payload['html']`: read attribute `html` from `self`. Assignment stores a value/reference; it is not an equality test.

**L0080.** Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0081.** Continue the statement starting at L80 with `"POST"`. Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0082.** Continue the statement starting at L80 with `"https://api.resend.com/emails"`. Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0083.** Continue the statement starting at L80 with `headers={`. Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0084.** Continue the statement starting at L80 with `"Authorization": f"Bearer {settings.email_api_key}"`. Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0085.** Continue the statement starting at L80 with `"Content-Type": "application/json"`. Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0086.** Close the grouped expression/declaration introduced at L80; delimiters/commas complete the same statement rather than execute a separate operation.

**L0087.** Continue the statement starting at L80 with `json=payload`. Assign to `request`: construct an outbound HTTP request and serialize its configured body: `httpx.Request('POST', 'https://api.resend.com/emails', headers={'Authorization': f'Bearer {settings.email_api_key}', 'Content-Type': 'application/json'}, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0088.** Close the grouped expression/declaration introduced at L80; delimiters/commas complete the same statement rather than execute a separate operation.

**L0089.** Bound serialized Resend request bytes. This check is below the earlier Gmail return and therefore does not bound Gmail messages.

**L0090.** Raise construct an invalid value/configuration exception: `ValueError('Email message is too large')`. Normal execution at this point stops.

**L0091.** Assign to `response`: use literal value `None` (NoneType). Assignment stores a value/reference; it is not an equality test.

**L0092.** Default two retries means three total attempts; there is no backoff delay.

**L0093.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0094.** Enter context manager(s): create a synchronous HTTP client whose context manager closes resources: `httpx.Client(timeout=settings.http_action_timeout_seconds)` bound as `client`. Exit cleanup also runs when the body raises.

**L0095.** Assign to `response`: send the prepared HTTPX request using this client: `client.send(request)`. Assignment stores a value/reference; it is not an equality test.

**L0096.** Catch `httpx.TransportError`; execute this error branch instead of continuing the failed statement.

**L0097.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `attempt == settings.http_action_max_retries`; this produces the branch/assertion's truth value.

**L0098.** Raise construct an execution/integration failure exception: `RuntimeError('Email provider network request failed')`; `from` controls exception cause/chaining: `None`. Normal execution at this point stops.

**L0099.** Skip the rest of this loop iteration and move to the next item/attempt.

**L0100.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `response.status_code < 500 or attempt == settings.http_action_max_retries`; later terms run only when needed.

**L0101.** Leave the nearest loop immediately; execution continues after the loop.

**L0102.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response is None`; this produces the branch/assertion's truth value.

**L0103.** Raise construct an execution/integration failure exception: `RuntimeError('Email provider did not return a response')`. Normal execution at this point stops.

**L0104.** Enter the following indented branch only if you read attribute `is_error` from `response`.

**L0105.** Raise construct an execution/integration failure exception: `RuntimeError(f'Email provider returned status {response.status_code}')`. Normal execution at this point stops.

**L0106.** Assign to `provider_id`: use literal value `None` (NoneType). Assignment stores a value/reference; it is not an equality test.

**L0107.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0108.** Assign to `response_data`: decode this response's JSON body, potentially raising on invalid data: `response.json()`. Assignment stores a value/reference; it is not an equality test.

**L0109.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `isinstance(response_data, dict) and isinstance(response_data.get('id'), str)`; later terms run only when needed.

**L0110.** Assign to `provider_id`: look up/index `response_data` using `'id'`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0111.** Catch `ValueError`; execute this error branch instead of continuing the failed statement.

**L0112.** Empty placeholder body required by Python syntax; SQLAlchemy's base class supplies inherited behavior here.

**L0113.** Declare `result` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'type': 'email', 'provider': settings.email_provider, 'status_code': response.status_code}`.

**L0114.** Continue the statement starting at L113 with `"type": "email"`. Declare `result` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'type': 'email', 'provider': settings.email_provider, 'status_code': response.status_code}`.

**L0115.** Continue the statement starting at L113 with `"provider": settings.email_provider`. Declare `result` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'type': 'email', 'provider': settings.email_provider, 'status_code': response.status_code}`.

**L0116.** Continue the statement starting at L113 with `"status_code": response.status_code`. Declare `result` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'type': 'email', 'provider': settings.email_provider, 'status_code': response.status_code}`.

**L0117.** Close the grouped expression/declaration introduced at L113; delimiters/commas complete the same statement rather than execute a separate operation.

**L0118.** Enter the following indented branch only if you read/evaluate `provider_id`.

**L0119.** Assign to `result['provider_id']`: read/evaluate `provider_id`. Assignment stores a value/reference; it is not an equality test.

**L0120.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `context.data.setdefault('action_results', []).append(result)`.


<a id="backend-app-core-actions-githubpy"></a>
## backend/app/core/actions/github.py

Outgoing GitHub action. The supported UI/demo path is repository dispatch, which can trigger the separate YAML workflow. Stored token is ordinary config. The extra issues/comments path lacks an issue number and is not a complete verified comment-creation feature.

Source fingerprint: `ef64f6545f9bd3aa9b23bddac0ff5208952565a6ebebebcf70f6f172cf770572`. Physical lines: 45.

### Numbered source

```python
0001 | from collections.abc import Mapping
0002 | 
0003 | import httpx
0004 | 
0005 | from app.config import settings
0006 | from app.core.actions.base import Action
0007 | from app.core.event import ExecutionContext
0008 | 
0009 | 
0010 | class GitHubAction(Action):
0011 |     def __init__(self, config: Mapping[str, object]) -> None:
0012 |         token = config.get("token")
0013 |         repository = config.get("repository")
0014 |         endpoint = config.get("endpoint", "dispatches")
0015 |         if not isinstance(token, str) or not token:
0016 |             raise ValueError("GitHub action requires a token")
0017 |         if not isinstance(repository, str) or repository.count("/") != 1:
0018 |             raise ValueError("GitHub action repository must be owner/name")
0019 |         if endpoint not in {"dispatches", "issues/comments"}:
0020 |             raise ValueError("Unsupported GitHub endpoint")
0021 |         self.token = token
0022 |         self.repository = repository
0023 |         self.endpoint = endpoint
0024 |         self.event_type = str(config.get("event_type", "flowforge"))
0025 |         self.body = config.get("body", {})
0026 | 
0027 |     def execute(self, context: ExecutionContext) -> None:
0028 |         if self.endpoint == "dispatches":
0029 |             url = f"https://api.github.com/repos/{self.repository}/dispatches"
0030 |             payload = {"event_type": self.event_type, "client_payload": self.body}
0031 |         else:
0032 |             url = f"https://api.github.com/repos/{self.repository}/issues/comments"
0033 |             payload = self.body
0034 |         headers = {
0035 |             "Accept": "application/vnd.github+json",
0036 |             "Authorization": f"Bearer {self.token}",
0037 |             "X-GitHub-Api-Version": "2022-11-28",
0038 |         }
0039 |         with httpx.Client(timeout=settings.http_action_timeout_seconds) as client:
0040 |             response = client.post(url, headers=headers, json=payload)
0041 |         if response.is_error:
0042 |             raise RuntimeError(f"GitHub action returned status {response.status_code}")
0043 |         context.data.setdefault("action_results", []).append(
0044 |             {"type": "github", "status_code": response.status_code}
0045 |         )
```

### Every-line explanation

**L0001.** Import Mapping from `collections.abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import module(s) `httpx`. Top-level module code runs on first import.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import Action from `app.core.actions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Define class `GitHubAction` inheriting `Action`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0011.** Define function/method `__init__(self, config: Mapping[str, object])` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0012.** Assign to `token`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('token')`. Assignment stores a value/reference; it is not an equality test.

**L0013.** Assign to `repository`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('repository')`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Assign to `endpoint`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('endpoint', 'dispatches')`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(token, str) or not token`; later terms run only when needed.

**L0016.** Raise construct an invalid value/configuration exception: `ValueError('GitHub action requires a token')`. Normal execution at this point stops.

**L0017.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(repository, str) or repository.count('/') != 1`; later terms run only when needed.

**L0018.** Raise construct an invalid value/configuration exception: `ValueError('GitHub action repository must be owner/name')`. Normal execution at this point stops.

**L0019.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `endpoint not in {'dispatches', 'issues/comments'}`; this produces the branch/assertion's truth value.

**L0020.** Raise construct an invalid value/configuration exception: `ValueError('Unsupported GitHub endpoint')`. Normal execution at this point stops.

**L0021.** Assign to `self.token`: read/evaluate `token`. Assignment stores a value/reference; it is not an equality test.

**L0022.** Assign to `self.repository`: read/evaluate `repository`. Assignment stores a value/reference; it is not an equality test.

**L0023.** Assign to `self.endpoint`: read/evaluate `endpoint`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Assign to `self.event_type`: convert a value to its string representation: `str(config.get('event_type', 'flowforge'))`. Assignment stores a value/reference; it is not an equality test.

**L0025.** Assign to `self.body`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('body', {})`. Assignment stores a value/reference; it is not an equality test.

**L0026.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0027.** Define function/method `execute(self, context: ExecutionContext)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0028.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `self.endpoint == 'dispatches'`; this produces the branch/assertion's truth value.

**L0029.** Assign to `url`: construct an f-string, interpolating expressions at runtime: `f'https://api.github.com/repos/{self.repository}/dispatches'`. Assignment stores a value/reference; it is not an equality test.

**L0030.** Assign to `payload`: construct a dictionary mapping the displayed keys to values: `{'event_type': self.event_type, 'client_payload': self.body}`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Alternative branch when the preceding if condition is false, or the try completed without its expected exception (inspect the enclosing block).

**L0032.** Assign to `url`: construct an f-string, interpolating expressions at runtime: `f'https://api.github.com/repos/{self.repository}/issues/comments'`. Assignment stores a value/reference; it is not an equality test.

**L0033.** Assign to `payload`: read attribute `body` from `self`. Assignment stores a value/reference; it is not an equality test.

**L0034.** Assign to `headers`: construct a dictionary mapping the displayed keys to values: `{'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}`. Assignment stores a value/reference; it is not an equality test.

**L0035.** Continue the statement starting at L34 with `"Accept": "application/vnd.github+json"`. Assign to `headers`: construct a dictionary mapping the displayed keys to values: `{'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}`. Assignment stores a value/reference; it is not an equality test.

**L0036.** Continue the statement starting at L34 with `"Authorization": f"Bearer {self.token}"`. Assign to `headers`: construct a dictionary mapping the displayed keys to values: `{'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}`. Assignment stores a value/reference; it is not an equality test.

**L0037.** Continue the statement starting at L34 with `"X-GitHub-Api-Version": "2022-11-28"`. Assign to `headers`: construct a dictionary mapping the displayed keys to values: `{'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {self.token}', 'X-GitHub-Api-Version': '2022-11-28'}`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Close the grouped expression/declaration introduced at L34; delimiters/commas complete the same statement rather than execute a separate operation.

**L0039.** Enter context manager(s): create a synchronous HTTP client whose context manager closes resources: `httpx.Client(timeout=settings.http_action_timeout_seconds)` bound as `client`. Exit cleanup also runs when the body raises.

**L0040.** Assign to `response`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post(url, headers=headers, json=payload)`. Assignment stores a value/reference; it is not an equality test.

**L0041.** Enter the following indented branch only if you read attribute `is_error` from `response`.

**L0042.** Raise construct an execution/integration failure exception: `RuntimeError(f'GitHub action returned status {response.status_code}')`. Normal execution at this point stops.

**L0043.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `context.data.setdefault('action_results', []).append({'type': 'github', 'status_code': response.status_code})`.

**L0044.** Continue the statement starting at L43 with `{"type": "github", "status_code": response.status_code}`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `context.data.setdefault('action_results', []).append({'type': 'github', 'status_code': response.status_code})`.

**L0045.** Close the grouped expression/declaration introduced at L43; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-core-actions-httppy"></a>
## backend/app/core/actions/http.py

Generic synchronous outbound JSON request. Public URL checks and disabled redirect following mitigate SSRF. Validation DNS is not pinned to connection DNS. Bounded immediate retries do not provide idempotency; no response-size cap or overall workflow deadline exists.

Source fingerprint: `19246f44c44524a34b39e206e37160eb20b84da9999c7b026714d594a861c547`. Physical lines: 66.

### Numbered source

```python
0001 | import ipaddress
0002 | import socket
0003 | from collections.abc import Mapping
0004 | from urllib.parse import urlparse
0005 | 
0006 | import httpx
0007 | 
0008 | from app.config import settings
0009 | from app.core.actions.base import Action
0010 | from app.core.event import ExecutionContext
0011 | 
0012 | 
0013 | def validate_public_url(url: str) -> str:
0014 |     parsed = urlparse(url)
0015 |     if parsed.scheme not in {"http", "https"} or not parsed.hostname:
0016 |         raise ValueError("URL must use http or https")
0017 |     try:
0018 |         addresses = socket.getaddrinfo(parsed.hostname, parsed.port or 443, type=socket.SOCK_STREAM)
0019 |     except socket.gaierror as exc:
0020 |         raise ValueError("URL hostname could not be resolved") from exc
0021 |     for address in addresses:
0022 |         ip = ipaddress.ip_address(address[4][0])
0023 |         if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_unspecified:
0024 |             raise ValueError("URL must not target a private or local address")
0025 |     return url
0026 | 
0027 | 
0028 | class HttpAction(Action):
0029 |     def __init__(self, config: Mapping[str, object]) -> None:
0030 |         url = config.get("url")
0031 |         if not isinstance(url, str):
0032 |             raise ValueError("HTTP action requires a URL")
0033 |         self.url = validate_public_url(url)
0034 |         self.method = str(config.get("method", "POST")).upper()
0035 |         if self.method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
0036 |             raise ValueError("Unsupported HTTP method")
0037 |         self.headers = {
0038 |             str(key): str(value)
0039 |             for key, value in (config.get("headers", {}) or {}).items()
0040 |             if isinstance(key, str)
0041 |         }
0042 |         payload = config.get("body", {})
0043 |         self.body = payload if isinstance(payload, (dict, list, str, int, float, bool)) else {}
0044 | 
0045 |     def execute(self, context: ExecutionContext) -> None:
0046 |         request = httpx.Request(self.method, self.url, headers=self.headers, json=self.body)
0047 |         if len(request.content) > settings.http_action_max_payload_bytes:
0048 |             raise ValueError("HTTP action payload is too large")
0049 |         response = None
0050 |         for attempt in range(settings.http_action_max_retries + 1):
0051 |             try:
0052 |                 with httpx.Client(timeout=settings.http_action_timeout_seconds, follow_redirects=False) as client:
0053 |                     response = client.send(request)
0054 |             except httpx.TransportError:
0055 |                 if attempt == settings.http_action_max_retries:
0056 |                     raise RuntimeError("HTTP action network request failed") from None
0057 |                 continue
0058 |             if response.status_code < 500 or attempt == settings.http_action_max_retries:
0059 |                 break
0060 |         if response is None:
0061 |             raise RuntimeError("HTTP action did not receive a response")
0062 |         if response.is_error:
0063 |             raise RuntimeError(f"HTTP action returned status {response.status_code}")
0064 |         context.data.setdefault("action_results", []).append(
0065 |             {"type": "http", "status_code": response.status_code}
0066 |         )
```

### Every-line explanation

**L0001.** Import module(s) `ipaddress`. Top-level module code runs on first import.

**L0002.** Import module(s) `socket`. Top-level module code runs on first import.

**L0003.** Import Mapping from `collections.abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import urlparse from `urllib.parse`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Import module(s) `httpx`. Top-level module code runs on first import.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Import Action from `app.core.actions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Define function/method `validate_public_url(url: str)` with intended return type `str`. 

**L0014.** Assign to `parsed`: parse the URL into components such as scheme, hostname, and port: `urlparse(url)`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `parsed.scheme not in {'http', 'https'} or not parsed.hostname`; later terms run only when needed.

**L0016.** Raise construct an invalid value/configuration exception: `ValueError('URL must use http or https')`. Normal execution at this point stops.

**L0017.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0018.** Resolve hostname to socket addresses before request construction. Default resolver port is 443 even for HTTP; the eventual client still uses URL semantics.

**L0019.** Catch `socket.gaierror` as `exc`; execute this error branch instead of continuing the failed statement.

**L0020.** Raise construct an invalid value/configuration exception: `ValueError('URL hostname could not be resolved')`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0021.** Iterate over `addresses`, binding each item/pair to `address`. The indented body runs once per item unless it returns/raises/breaks.

**L0022.** Tuple index 4 is sockaddr; its first item is the resolved IP string. Convert it to an ipaddress object for classification.

**L0023.** Reject these nonpublic/local classifications for every returned address. This is not connection-address pinning or a complete egress policy.

**L0024.** Raise construct an invalid value/configuration exception: `ValueError('URL must not target a private or local address')`. Normal execution at this point stops.

**L0025.** Return from this function: read/evaluate `url`.

**L0026.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0027.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0028.** Define class `HttpAction` inheriting `Action`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0029.** Define function/method `__init__(self, config: Mapping[str, object])` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0030.** Assign to `url`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('url')`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Enter the following indented branch only if you negate the truth value of `isinstance(url, str)`.

**L0032.** Raise construct an invalid value/configuration exception: `ValueError('HTTP action requires a URL')`. Normal execution at this point stops.

**L0033.** Assign to `self.url`: call `validate_public_url` with the displayed positional/named arguments: `validate_public_url(url)`. Assignment stores a value/reference; it is not an equality test.

**L0034.** Assign to `self.method`: normalize a string to uppercase: `str(config.get('method', 'POST')).upper()`. Assignment stores a value/reference; it is not an equality test.

**L0035.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `self.method not in {'GET', 'POST', 'PUT', 'PATCH', 'DELETE'}`; this produces the branch/assertion's truth value.

**L0036.** Raise construct an invalid value/configuration exception: `ValueError('Unsupported HTTP method')`. Normal execution at this point stops.

**L0037.** Assign to `self.headers`: read/evaluate `{str(key): str(value) for key, value in (config.get('headers', {}) or {}).items() if isinstance(key, str)}`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Continue the statement starting at L37 with `str(key): str(value)`. Assign to `self.headers`: read/evaluate `{str(key): str(value) for key, value in (config.get('headers', {}) or {}).items() if isinstance(key, str)}`. Assignment stores a value/reference; it is not an equality test.

**L0039.** Read header pairs from configured mapping-like data. A nonmapping truthy value can raise before a safe ValueError is produced.

**L0040.** Continue the statement starting at L37 with `if isinstance(key, str)`. Assign to `self.headers`: read/evaluate `{str(key): str(value) for key, value in (config.get('headers', {}) or {}).items() if isinstance(key, str)}`. Assignment stores a value/reference; it is not an equality test.

**L0041.** Close the grouped expression/declaration introduced at L37; delimiters/commas complete the same statement rather than execute a separate operation.

**L0042.** Assign to `payload`: read a mapping key with a default (or call this object's get method as identified by the receiver): `config.get('body', {})`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Keep selected JSON-compatible body types; None and unsupported values become an empty object.

**L0044.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0045.** Define function/method `execute(self, context: ExecutionContext)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0046.** Pre-serialize an outbound JSON request so its actual encoded request content can be sized.

**L0047.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `len(request.content) > settings.http_action_max_payload_bytes`; this produces the branch/assertion's truth value.

**L0048.** Raise construct an invalid value/configuration exception: `ValueError('HTTP action payload is too large')`. Normal execution at this point stops.

**L0049.** Assign to `response`: use literal value `None` (NoneType). Assignment stores a value/reference; it is not an equality test.

**L0050.** Attempt up to max_retries + 1 times, counting the initial attempt separately from retries.

**L0051.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0052.** Create/close a synchronous client for each attempt and prohibit following redirects. Timeout is not one overall workflow deadline.

**L0053.** Assign to `response`: send the prepared HTTPX request using this client: `client.send(request)`. Assignment stores a value/reference; it is not an equality test.

**L0054.** Catch `httpx.TransportError`; execute this error branch instead of continuing the failed statement.

**L0055.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `attempt == settings.http_action_max_retries`; this produces the branch/assertion's truth value.

**L0056.** Raise construct an execution/integration failure exception: `RuntimeError('HTTP action network request failed')`; `from` controls exception cause/chaining: `None`. Normal execution at this point stops.

**L0057.** Skip the rest of this loop iteration and move to the next item/attempt.

**L0058.** Stop for every status below 500 (including 429 and redirects) or at the final allowed attempt.

**L0059.** Leave the nearest loop immediately; execution continues after the loop.

**L0060.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response is None`; this produces the branch/assertion's truth value.

**L0061.** Raise construct an execution/integration failure exception: `RuntimeError('HTTP action did not receive a response')`. Normal execution at this point stops.

**L0062.** Reject HTTPX client/server error responses. A 3xx is not is_error, so it can currently count as success despite redirects being unfollowed.

**L0063.** Raise construct an execution/integration failure exception: `RuntimeError(f'HTTP action returned status {response.status_code}')`. Normal execution at this point stops.

**L0064.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `context.data.setdefault('action_results', []).append({'type': 'http', 'status_code': response.status_code})`.

**L0065.** Continue the statement starting at L64 with `{"type": "http", "status_code": response.status_code}`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `context.data.setdefault('action_results', []).append({'type': 'http', 'status_code': response.status_code})`.

**L0066.** Close the grouped expression/declaration introduced at L64; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-core-actions-nooppy"></a>
## backend/app/core/actions/noop.py

Deterministic side-effect recorder used for demonstration/tests. calls belongs to this runtime instance and is not a persistent execution history table.

Source fingerprint: `528f55bff93e7f2406ec47c368ff0cf06e7be255565f731b15aa0f49824a8f62`. Physical lines: 12.

### Numbered source

```python
0001 | from app.core.actions.base import Action
0002 | from app.core.event import ExecutionContext
0003 | 
0004 | 
0005 | class NoOpAction(Action):
0006 |     """Records that execute() ran. No network and no secrets."""
0007 | 
0008 |     def __init__(self) -> None:
0009 |         self.calls: list[ExecutionContext] = []
0010 | 
0011 |     def execute(self, context: ExecutionContext) -> None:
0012 |         self.calls.append(context)
```

### Every-line explanation

**L0001.** Import Action from `app.core.actions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Define class `NoOpAction` inheriting `Action`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0006.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Define function/method `__init__(self)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0009.** Declare `self.calls` with intended type `list[ExecutionContext]` and initialize it: construct a list containing the displayed values: `[]`.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Define function/method `execute(self, context: ExecutionContext)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0012.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `self.calls.append(context)`.


<a id="backend-app-core-conditions-initpy"></a>
## backend/app/core/conditions/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `090b5bd67272d74cd29313518765a379e40cc5b8d3d5b38881c59f251789bc2b`. Physical lines: 20.

### Numbered source

```python
0001 | from app.core.conditions.base import Condition
0002 | from app.core.conditions.composite import AndCondition, OrCondition
0003 | from app.core.conditions.comparison import (
0004 |     ContainsCondition,
0005 |     GreaterThanCondition,
0006 |     LessThanCondition,
0007 |     NotEqualsCondition,
0008 | )
0009 | from app.core.conditions.equals import EqualsCondition
0010 | 
0011 | __all__ = [
0012 |     "AndCondition",
0013 |     "Condition",
0014 |     "ContainsCondition",
0015 |     "EqualsCondition",
0016 |     "GreaterThanCondition",
0017 |     "LessThanCondition",
0018 |     "NotEqualsCondition",
0019 |     "OrCondition",
0020 | ]
```

### Every-line explanation

**L0001.** Import Condition from `app.core.conditions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import AndCondition, OrCondition from `app.core.conditions.composite`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import ContainsCondition, GreaterThanCondition, LessThanCondition, NotEqualsCondition from `app.core.conditions.comparison`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Continue the parenthesized import from `app.core.conditions.comparison` with name(s) `ContainsCondition`.

**L0005.** Continue the parenthesized import from `app.core.conditions.comparison` with name(s) `GreaterThanCondition`.

**L0006.** Continue the parenthesized import from `app.core.conditions.comparison` with name(s) `LessThanCondition`.

**L0007.** Continue the parenthesized import from `app.core.conditions.comparison` with name(s) `NotEqualsCondition`.

**L0008.** Close the grouped expression/declaration introduced at L3; delimiters/commas complete the same statement rather than execute a separate operation.

**L0009.** Import EqualsCondition from `app.core.conditions.equals`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0012.** Continue the statement starting at L11 with `"AndCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0013.** Continue the statement starting at L11 with `"Condition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Continue the statement starting at L11 with `"ContainsCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Continue the statement starting at L11 with `"EqualsCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0016.** Continue the statement starting at L11 with `"GreaterThanCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0017.** Continue the statement starting at L11 with `"LessThanCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Continue the statement starting at L11 with `"NotEqualsCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Continue the statement starting at L11 with `"OrCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['AndCondition', 'Condition', 'ContainsCondition', 'EqualsCondition', 'GreaterThanCondition', 'LessThanCondition', 'NotEqualsCondition', 'OrCondition']`. Assignment stores a value/reference; it is not an equality test.

**L0020.** Close the grouped expression/declaration introduced at L11; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-core-conditions-basepy"></a>
## backend/app/core/conditions/base.py

Condition's abstract boolean contract. A concrete leaf or group can be used anywhere a Condition is expected.

Source fingerprint: `1e222cee22e721b85f8f957b784a199ea9ca43fa43c163e787f826de475b108c`. Physical lines: 9.

### Numbered source

```python
0001 | from abc import ABC, abstractmethod
0002 | 
0003 | from app.core.event import ExecutionContext
0004 | 
0005 | 
0006 | class Condition(ABC):
0007 |     @abstractmethod
0008 |     def evaluate(self, context: ExecutionContext) -> bool:
0009 |         """Return True when the workflow should continue."""
```

### Every-line explanation

**L0001.** Import ABC, abstractmethod from `abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `Condition` inheriting `ABC`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Mark the next method as required by the ABC mechanism before a subclass can normally be instantiated.

**L0008.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0009.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.


<a id="backend-app-core-conditions-comparisonpy"></a>
## backend/app/core/conditions/comparison.py

Inequality, ordering, and membership leaves. Ordering/membership TypeErrors become False. A missing field can still pass NotEquals. Contains checks dictionary keys, list elements, or string substrings depending on the candidate type.

Source fingerprint: `8ae9d3cc29876f40f545dba61cf479c09941a3075f69208aad9f7cf08b1f6d1a`. Physical lines: 50.

### Numbered source

```python
0001 | from typing import Any
0002 | 
0003 | from app.core.conditions.base import Condition
0004 | from app.core.event import ExecutionContext
0005 | 
0006 | 
0007 | class NotEqualsCondition(Condition):
0008 |     def __init__(self, field: str, value: Any) -> None:
0009 |         self.field = field
0010 |         self.value = value
0011 | 
0012 |     def evaluate(self, context: ExecutionContext) -> bool:
0013 |         return context.lookup(self.field) != self.value
0014 | 
0015 | 
0016 | class GreaterThanCondition(Condition):
0017 |     def __init__(self, field: str, value: Any) -> None:
0018 |         self.field = field
0019 |         self.value = value
0020 | 
0021 |     def evaluate(self, context: ExecutionContext) -> bool:
0022 |         try:
0023 |             return context.lookup(self.field) > self.value
0024 |         except TypeError:
0025 |             return False
0026 | 
0027 | 
0028 | class LessThanCondition(Condition):
0029 |     def __init__(self, field: str, value: Any) -> None:
0030 |         self.field = field
0031 |         self.value = value
0032 | 
0033 |     def evaluate(self, context: ExecutionContext) -> bool:
0034 |         try:
0035 |             return context.lookup(self.field) < self.value
0036 |         except TypeError:
0037 |             return False
0038 | 
0039 | 
0040 | class ContainsCondition(Condition):
0041 |     def __init__(self, field: str, value: Any) -> None:
0042 |         self.field = field
0043 |         self.value = value
0044 | 
0045 |     def evaluate(self, context: ExecutionContext) -> bool:
0046 |         candidate = context.lookup(self.field)
0047 |         try:
0048 |             return self.value in candidate
0049 |         except TypeError:
0050 |             return False
```

### Every-line explanation

**L0001.** Import Any from `typing`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import Condition from `app.core.conditions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Define class `NotEqualsCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0008.** Define function/method `__init__(self, field: str, value: Any)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0009.** Assign to `self.field`: read/evaluate `field`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Assign to `self.value`: read/evaluate `value`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0013.** Return from this function: evaluate the comparison/membership/identity test `context.lookup(self.field) != self.value`; this produces the branch/assertion's truth value.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Define class `GreaterThanCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0017.** Define function/method `__init__(self, field: str, value: Any)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0018.** Assign to `self.field`: read/evaluate `field`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Assign to `self.value`: read/evaluate `value`. Assignment stores a value/reference; it is not an equality test.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0022.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0023.** Return from this function: evaluate the comparison/membership/identity test `context.lookup(self.field) > self.value`; this produces the branch/assertion's truth value.

**L0024.** Catch `TypeError`; execute this error branch instead of continuing the failed statement.

**L0025.** Return from this function: use literal value `False` (bool).

**L0026.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0027.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0028.** Define class `LessThanCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0029.** Define function/method `__init__(self, field: str, value: Any)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0030.** Assign to `self.field`: read/evaluate `field`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Assign to `self.value`: read/evaluate `value`. Assignment stores a value/reference; it is not an equality test.

**L0032.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0033.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0034.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0035.** Return from this function: evaluate the comparison/membership/identity test `context.lookup(self.field) < self.value`; this produces the branch/assertion's truth value.

**L0036.** Catch `TypeError`; execute this error branch instead of continuing the failed statement.

**L0037.** Return from this function: use literal value `False` (bool).

**L0038.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0039.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0040.** Define class `ContainsCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0041.** Define function/method `__init__(self, field: str, value: Any)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0042.** Assign to `self.field`: read/evaluate `field`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Assign to `self.value`: read/evaluate `value`. Assignment stores a value/reference; it is not an equality test.

**L0044.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0045.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0046.** Assign to `candidate`: call `context.lookup` with the displayed positional/named arguments: `context.lookup(self.field)`. Assignment stores a value/reference; it is not an equality test.

**L0047.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0048.** Return from this function: evaluate the comparison/membership/identity test `self.value in candidate`; this produces the branch/assertion's truth value.

**L0049.** Catch `TypeError`; execute this error branch instead of continuing the failed statement.

**L0050.** Return from this function: use literal value `False` (bool).


<a id="backend-app-core-conditions-compositepy"></a>
## backend/app/core/conditions/composite.py

Composite pattern. Child iterables are materialized as lists. all/any short-circuit and permit nested groups. Empty AND is True; empty OR is False.

Source fingerprint: `b0d096f41911e3a9e24333ad17f6cb0dc464f32a5048a3191ae89463fe43a469`. Physical lines: 20.

### Numbered source

```python
0001 | from collections.abc import Iterable
0002 | 
0003 | from app.core.conditions.base import Condition
0004 | from app.core.event import ExecutionContext
0005 | 
0006 | 
0007 | class AndCondition(Condition):
0008 |     def __init__(self, conditions: Iterable[Condition]) -> None:
0009 |         self.conditions = list(conditions)
0010 | 
0011 |     def evaluate(self, context: ExecutionContext) -> bool:
0012 |         return all(condition.evaluate(context) for condition in self.conditions)
0013 | 
0014 | 
0015 | class OrCondition(Condition):
0016 |     def __init__(self, conditions: Iterable[Condition]) -> None:
0017 |         self.conditions = list(conditions)
0018 | 
0019 |     def evaluate(self, context: ExecutionContext) -> bool:
0020 |         return any(condition.evaluate(context) for condition in self.conditions)
```

### Every-line explanation

**L0001.** Import Iterable from `collections.abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import Condition from `app.core.conditions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Define class `AndCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0008.** Define function/method `__init__(self, conditions: Iterable[Condition])` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0009.** Assign to `self.conditions`: materialize an iterable into a list: `list(conditions)`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0012.** Return from this function: short-circuit False at the first false child; empty input yields True: `all((condition.evaluate(context) for condition in self.conditions))`.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Define class `OrCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0016.** Define function/method `__init__(self, conditions: Iterable[Condition])` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0017.** Assign to `self.conditions`: materialize an iterable into a list: `list(conditions)`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0019.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0020.** Return from this function: short-circuit True at the first true child; empty input yields False: `any((condition.evaluate(context) for condition in self.conditions))`.


<a id="backend-app-core-conditions-equalspy"></a>
## backend/app/core/conditions/equals.py

Equality leaf over a top-level context lookup. Missing fields become None; Python's equality semantics apply without universal strict type normalization.

Source fingerprint: `be3e58e412e8c91c833abd8cf87bce9a1d35960f29a6d8a5a11d87a07436fa35`. Physical lines: 11.

### Numbered source

```python
0001 | from app.core.conditions.base import Condition
0002 | from app.core.event import ExecutionContext
0003 | 
0004 | 
0005 | class EqualsCondition(Condition):
0006 |     def __init__(self, field: str, value: object) -> None:
0007 |         self.field = field
0008 |         self.value = value
0009 | 
0010 |     def evaluate(self, context: ExecutionContext) -> bool:
0011 |         return context.lookup(self.field) == self.value
```

### Every-line explanation

**L0001.** Import Condition from `app.core.conditions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Define class `EqualsCondition` inheriting `Condition`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0006.** Define function/method `__init__(self, field: str, value: object)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0007.** Assign to `self.field`: read/evaluate `field`. Assignment stores a value/reference; it is not an equality test.

**L0008.** Assign to `self.value`: read/evaluate `value`. Assignment stores a value/reference; it is not an equality test.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Define function/method `evaluate(self, context: ExecutionContext)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0011.** Return from this function: evaluate the comparison/membership/identity test `context.lookup(self.field) == self.value`; this produces the branch/assertion's truth value.


<a id="backend-app-core-enginepy"></a>
## backend/app/core/engine.py

The framework/ORM-independent execution algorithm. Trigger/condition gating happens before the action try block. Actions run in order and stop on first exception. Exception strings are preserved, not universally redacted. Empty action lists succeed with zero count.

Source fingerprint: `80885c3f3b71fe8c4fe4a3db9481e00d3c0a2491f8804a5c6b25a75d88b70969`. Physical lines: 41.

### Numbered source

```python
0001 | from dataclasses import dataclass
0002 | from enum import StrEnum
0003 | 
0004 | from app.core.event import Event, ExecutionContext
0005 | from app.core.workflow import Workflow
0006 | 
0007 | 
0008 | class ExecutionStatus(StrEnum):
0009 |     SUCCESS = "SUCCESS"
0010 |     FAILED = "FAILED"
0011 |     SKIPPED = "SKIPPED"
0012 | 
0013 | 
0014 | @dataclass(frozen=True)
0015 | class EngineResult:
0016 |     status: ExecutionStatus
0017 |     action_count: int = 0
0018 |     error: str | None = None
0019 | 
0020 | 
0021 | class WorkflowEngine:
0022 |     def execute(self, workflow: Workflow, event: Event, user_id: str | None = None) -> EngineResult:
0023 |         if not workflow.trigger.should_execute(event):
0024 |             return EngineResult(status=ExecutionStatus.SKIPPED, error="Trigger did not match")
0025 | 
0026 |         context = ExecutionContext(event=event, user_id=user_id)
0027 |         if workflow.condition is not None and not workflow.condition.evaluate(context):
0028 |             return EngineResult(status=ExecutionStatus.SKIPPED, error="Conditions did not match")
0029 | 
0030 |         executed = 0
0031 |         try:
0032 |             for action in workflow.actions:
0033 |                 action.execute(context)
0034 |                 executed += 1
0035 |         except Exception as exc:
0036 |             return EngineResult(
0037 |                 status=ExecutionStatus.FAILED,
0038 |                 action_count=executed,
0039 |                 error=str(exc) or "Action execution failed",
0040 |             )
0041 |         return EngineResult(status=ExecutionStatus.SUCCESS, action_count=executed)
```

### Every-line explanation

**L0001.** Import dataclass from `dataclasses`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import StrEnum from `enum`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import Event, ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import Workflow from `app.core.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Create a string-valued enum so statuses have symbolic identity and serializable string values (Python 3.11+ StrEnum).

**L0009.** Assign to `SUCCESS`: use literal value `'SUCCESS'` (str). Assignment stores a value/reference; it is not an equality test.

**L0010.** Assign to `FAILED`: use literal value `'FAILED'` (str). Assignment stores a value/reference; it is not an equality test.

**L0011.** Assign to `SKIPPED`: use literal value `'SKIPPED'` (str). Assignment stores a value/reference; it is not an equality test.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Generate a result data object whose fields cannot normally be reassigned after construction; this is shallow immutability.

**L0015.** Define class `EngineResult`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0016.** Declare `status` with intended type `ExecutionStatus`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0017.** Default completed-action count to zero; skipped runs need not specify it.

**L0018.** Declare `error` with intended type `str | None` and initialize it: use literal value `None` (NoneType).

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Define class `WorkflowEngine`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0022.** Public engine operation receives runtime composition, normalized event, and optional owner; no database session enters this method.

**L0023.** Call the concrete Trigger polymorphically and negate its boolean result; if it does not match, enter the early-return branch.

**L0024.** End execution immediately as SKIPPED with the trigger reason; no context/actions are created/run yet.

**L0025.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0026.** Construct a fresh per-run context, carrying event and owner identity for user-specific actions such as Gmail.

**L0027.** Short-circuit the None check before calling evaluate. A false concrete condition enters the skip branch.

**L0028.** End as SKIPPED with a condition reason; action_count retains its default zero.

**L0029.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0030.** Initialize the number of actions that have returned normally.

**L0031.** Begin exception handling for the action loop only; trigger/condition failures above are outside this block.

**L0032.** Visit each runtime Action in the stored/configured order.

**L0033.** Dynamic dispatch calls this concrete action's execute with the shared execution context; the engine has no provider-type branch.

**L0034.** Increase the count only after execute returns; the failing action itself is not counted as completed.

**L0035.** Catch an Exception from action iteration/execution; later actions stop. BaseException subclasses such as KeyboardInterrupt are not covered.

**L0036.** Return from this function: construct the engine's final status/count/error data object: `EngineResult(status=ExecutionStatus.FAILED, action_count=executed, error=str(exc) or 'Action execution failed')`.

**L0037.** Mark attempted action execution as FAILED, distinguishing it from rule-based SKIPPED.

**L0038.** Preserve the number of previously completed actions; no external side effects are rolled back.

**L0039.** Preserve the exception's string or fall back if empty. This relies on safe action errors, not automatic redaction.

**L0040.** Close the grouped expression/declaration introduced at L36; delimiters/commas complete the same statement rather than execute a separate operation.

**L0041.** If all actions return, finish SUCCESS with their count; an empty list yields SUCCESS with zero.


<a id="backend-app-core-eventpy"></a>
## backend/app/core/event.py

Dataclasses normalize an event envelope and hold per-run context. Each instance receives fresh dicts. lookup is top-level only, prioritizes context.data, and does not traverse dotted paths. Event.source and payload['source'] are distinct.

Source fingerprint: `a6f02274b218828b0f2b28089d74dc787b6823505ed4e39ff0a445f4123f2caa`. Physical lines: 25.

### Numbered source

```python
0001 | from dataclasses import dataclass, field
0002 | from datetime import datetime, timezone
0003 | from typing import Any
0004 | 
0005 | 
0006 | @dataclass
0007 | class Event:
0008 |     """Normalized inbound event. The engine should never parse vendor JSON directly."""
0009 | 
0010 |     type: str
0011 |     source: str
0012 |     payload: dict[str, Any] = field(default_factory=dict)
0013 |     timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
0014 | 
0015 | 
0016 | @dataclass
0017 | class ExecutionContext:
0018 |     event: Event
0019 |     user_id: str | None = None
0020 |     data: dict[str, Any] = field(default_factory=dict)
0021 | 
0022 |     def lookup(self, field_name: str) -> Any:
0023 |         if field_name in self.data:
0024 |             return self.data[field_name]
0025 |         return self.event.payload.get(field_name)
```

### Every-line explanation

**L0001.** Import dataclass, field from `dataclasses`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import datetime, timezone from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import Any from `typing`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Generate dataclass initialization/representation/equality from annotated fields.

**L0007.** Define class `Event`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0008.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Declare `type` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0011.** Declare `source` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0012.** Create a fresh payload dictionary per Event via default_factory; Any permits varied JSON-like input without strict field typing.

**L0013.** Use a deferred lambda to capture a new timezone-aware UTC timestamp at each Event construction.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Generate dataclass initialization/representation/equality from annotated fields.

**L0017.** Define class `ExecutionContext`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0018.** Declare `event` with intended type `Event`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0019.** Store the owning user ID when supplied, enabling per-user integration lookup; None supports pure core/local tests.

**L0020.** Create fresh mutable data for each execution context; actions can append selected results here.

**L0021.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0022.** Define function/method `lookup(self, field_name: str)` with intended return type `Any`.  `self` is supplied by an ordinary bound method call.

**L0023.** Test key presence in context data rather than truthiness of its value, so even a stored None/False overrides payload.

**L0024.** Return the exact context-data value when the key exists.

**L0025.** Otherwise perform a top-level payload get, returning None if absent; dots are literal characters here.


<a id="backend-app-core-factoriespy"></a>
## backend/app/core/factories.py

Simple static factories turn recognized type/config data into Python objects. Composite condition construction recurses. Branches belong here rather than in the engine. This is not arbitrary class loading or eval.

Source fingerprint: `57c91148d0c124c2b23e44099eb0f4ff33a39bd1e133917a468ff838dc7c94aa`. Physical lines: 81.

### Numbered source

```python
0001 | from collections.abc import Mapping
0002 | from typing import Any
0003 | 
0004 | from app.core.actions import Action, EmailAction, GitHubAction, HttpAction, NoOpAction
0005 | from app.core.conditions import (
0006 |     AndCondition,
0007 |     Condition,
0008 |     ContainsCondition,
0009 |     EqualsCondition,
0010 |     GreaterThanCondition,
0011 |     LessThanCondition,
0012 |     NotEqualsCondition,
0013 |     OrCondition,
0014 | )
0015 | from app.core.triggers import ManualTrigger, ScheduledTrigger, Trigger, WebhookTrigger
0016 | 
0017 | 
0018 | def _required(config: Mapping[str, Any], key: str) -> Any:
0019 |     if key not in config:
0020 |         raise ValueError(f"Missing required configuration: {key}")
0021 |     return config[key]
0022 | 
0023 | 
0024 | class TriggerFactory:
0025 |     @staticmethod
0026 |     def create(trigger_type: str, config: Mapping[str, Any] | None = None) -> Trigger:
0027 |         values = config or {}
0028 |         if trigger_type == "manual":
0029 |             return ManualTrigger()
0030 |         if trigger_type == "webhook":
0031 |             return WebhookTrigger(source=values.get("source"))
0032 |         if trigger_type == "scheduled":
0033 |             return ScheduledTrigger()
0034 |         raise ValueError(f"Unsupported trigger type: {trigger_type}")
0035 | 
0036 | 
0037 | class ConditionFactory:
0038 |     @staticmethod
0039 |     def create(condition_type: str, config: Mapping[str, Any] | None = None) -> Condition:
0040 |         values = config or {}
0041 |         if condition_type in {"and", "or"}:
0042 |             children = values.get("conditions")
0043 |             if not isinstance(children, list):
0044 |                 raise ValueError("Composite conditions require a conditions list")
0045 |             hydrated = [
0046 |                 ConditionFactory.create(child["type"], child.get("config", {}))
0047 |                 for child in children
0048 |             ]
0049 |             return AndCondition(hydrated) if condition_type == "and" else OrCondition(hydrated)
0050 | 
0051 |         field = _required(values, "field")
0052 |         value = _required(values, "value")
0053 |         condition_types = {
0054 |             "equals": EqualsCondition,
0055 |             "not_equals": NotEqualsCondition,
0056 |             "greater_than": GreaterThanCondition,
0057 |             "less_than": LessThanCondition,
0058 |             "contains": ContainsCondition,
0059 |         }
0060 |         condition_class = condition_types.get(condition_type)
0061 |         if condition_class is None:
0062 |             raise ValueError(f"Unsupported condition type: {condition_type}")
0063 |         return condition_class(field=field, value=value)
0064 | 
0065 | 
0066 | class ActionFactory:
0067 |     @staticmethod
0068 |     def create(
0069 |         action_type: str,
0070 |         config: Mapping[str, Any] | None = None,
0071 |         gmail_service: Any = None,
0072 |     ) -> Action:
0073 |         if action_type == "noop":
0074 |             return NoOpAction()
0075 |         if action_type == "http":
0076 |             return HttpAction(config or {})
0077 |         if action_type == "github":
0078 |             return GitHubAction(config or {})
0079 |         if action_type == "email":
0080 |             return EmailAction(config or {}, gmail_service=gmail_service)
0081 |         raise ValueError(f"Unsupported action type: {action_type}")
```

### Every-line explanation

**L0001.** Import Mapping from `collections.abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Any from `typing`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import Action, EmailAction, GitHubAction, HttpAction, NoOpAction from `app.core.actions`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import AndCondition, Condition, ContainsCondition, EqualsCondition, GreaterThanCondition, LessThanCondition, NotEqualsCondition, OrCondition from `app.core.conditions`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Continue the parenthesized import from `app.core.conditions` with name(s) `AndCondition`.

**L0007.** Continue the parenthesized import from `app.core.conditions` with name(s) `Condition`.

**L0008.** Continue the parenthesized import from `app.core.conditions` with name(s) `ContainsCondition`.

**L0009.** Continue the parenthesized import from `app.core.conditions` with name(s) `EqualsCondition`.

**L0010.** Continue the parenthesized import from `app.core.conditions` with name(s) `GreaterThanCondition`.

**L0011.** Continue the parenthesized import from `app.core.conditions` with name(s) `LessThanCondition`.

**L0012.** Continue the parenthesized import from `app.core.conditions` with name(s) `NotEqualsCondition`.

**L0013.** Continue the parenthesized import from `app.core.conditions` with name(s) `OrCondition`.

**L0014.** Close the grouped expression/declaration introduced at L5; delimiters/commas complete the same statement rather than execute a separate operation.

**L0015.** Import ManualTrigger, ScheduledTrigger, Trigger, WebhookTrigger from `app.core.triggers`. Imported names become available in this module; aliases distinguish roles where used.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0018.** Define function/method `_required(config: Mapping[str, Any], key: str)` with intended return type `Any`. 

**L0019.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `key not in config`; this produces the branch/assertion's truth value.

**L0020.** Raise construct an invalid value/configuration exception: `ValueError(f'Missing required configuration: {key}')`. Normal execution at this point stops.

**L0021.** Return from this function: look up/index `config` using `key`; missing keys/out-of-range indices can raise.

**L0022.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0023.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0024.** Define class `TriggerFactory`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0025.** Decorate the following factory/helper so it does not receive an implicit self instance argument.

**L0026.** Define function/method `create(trigger_type: str, config: Mapping[str, Any] | None=None)` with intended return type `Trigger`. 

**L0027.** Assign to `values`: evaluate the short-circuit boolean expression `config or {}`; later terms run only when needed. Assignment stores a value/reference; it is not an equality test.

**L0028.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `trigger_type == 'manual'`; this produces the branch/assertion's truth value.

**L0029.** Return from this function: call `ManualTrigger` with the displayed positional/named arguments: `ManualTrigger()`.

**L0030.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `trigger_type == 'webhook'`; this produces the branch/assertion's truth value.

**L0031.** Return from this function: call `WebhookTrigger` with the displayed positional/named arguments: `WebhookTrigger(source=values.get('source'))`.

**L0032.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `trigger_type == 'scheduled'`; this produces the branch/assertion's truth value.

**L0033.** Return from this function: call `ScheduledTrigger` with the displayed positional/named arguments: `ScheduledTrigger()`.

**L0034.** Raise construct an invalid value/configuration exception: `ValueError(f'Unsupported trigger type: {trigger_type}')`. Normal execution at this point stops.

**L0035.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0036.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0037.** Define class `ConditionFactory`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0038.** Decorate the following factory/helper so it does not receive an implicit self instance argument.

**L0039.** Define function/method `create(condition_type: str, config: Mapping[str, Any] | None=None)` with intended return type `Condition`. 

**L0040.** Assign to `values`: evaluate the short-circuit boolean expression `config or {}`; later terms run only when needed. Assignment stores a value/reference; it is not an equality test.

**L0041.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `condition_type in {'and', 'or'}`; this produces the branch/assertion's truth value.

**L0042.** Assign to `children`: read a mapping key with a default (or call this object's get method as identified by the receiver): `values.get('conditions')`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Enter the following indented branch only if you negate the truth value of `isinstance(children, list)`.

**L0044.** Raise construct an invalid value/configuration exception: `ValueError('Composite conditions require a conditions list')`. Normal execution at this point stops.

**L0045.** Assign to `hydrated`: construct a new list by applying the displayed expression for each item in the comprehension: `[ConditionFactory.create(child['type'], child.get('config', {})) for child in children]`. Assignment stores a value/reference; it is not an equality test.

**L0046.** Continue the statement starting at L45 with `ConditionFactory.create(child["type"], child.get("config", {}))`. Assign to `hydrated`: construct a new list by applying the displayed expression for each item in the comprehension: `[ConditionFactory.create(child['type'], child.get('config', {})) for child in children]`. Assignment stores a value/reference; it is not an equality test.

**L0047.** Continue the statement starting at L45 with `for child in children`. Assign to `hydrated`: construct a new list by applying the displayed expression for each item in the comprehension: `[ConditionFactory.create(child['type'], child.get('config', {})) for child in children]`. Assignment stores a value/reference; it is not an equality test.

**L0048.** Close the grouped expression/declaration introduced at L45; delimiters/commas complete the same statement rather than execute a separate operation.

**L0049.** Return from this function: choose `AndCondition(hydrated)` when `condition_type == 'and'` is true, otherwise `OrCondition(hydrated)`.

**L0050.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0051.** Assign to `field`: call `_required` with the displayed positional/named arguments: `_required(values, 'field')`. Assignment stores a value/reference; it is not an equality test.

**L0052.** Assign to `value`: call `_required` with the displayed positional/named arguments: `_required(values, 'value')`. Assignment stores a value/reference; it is not an equality test.

**L0053.** Assign to `condition_types`: construct a dictionary mapping the displayed keys to values: `{'equals': EqualsCondition, 'not_equals': NotEqualsCondition, 'greater_than': GreaterThanCondition, 'less_than': LessThanCondition, 'contains': ContainsCondition}`. Assignment stores a value/reference; it is not an equality test.

**L0054.** Continue the statement starting at L53 with `"equals": EqualsCondition`. Assign to `condition_types`: construct a dictionary mapping the displayed keys to values: `{'equals': EqualsCondition, 'not_equals': NotEqualsCondition, 'greater_than': GreaterThanCondition, 'less_than': LessThanCondition, 'contains': ContainsCondition}`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Continue the statement starting at L53 with `"not_equals": NotEqualsCondition`. Assign to `condition_types`: construct a dictionary mapping the displayed keys to values: `{'equals': EqualsCondition, 'not_equals': NotEqualsCondition, 'greater_than': GreaterThanCondition, 'less_than': LessThanCondition, 'contains': ContainsCondition}`. Assignment stores a value/reference; it is not an equality test.

**L0056.** Continue the statement starting at L53 with `"greater_than": GreaterThanCondition`. Assign to `condition_types`: construct a dictionary mapping the displayed keys to values: `{'equals': EqualsCondition, 'not_equals': NotEqualsCondition, 'greater_than': GreaterThanCondition, 'less_than': LessThanCondition, 'contains': ContainsCondition}`. Assignment stores a value/reference; it is not an equality test.

**L0057.** Continue the statement starting at L53 with `"less_than": LessThanCondition`. Assign to `condition_types`: construct a dictionary mapping the displayed keys to values: `{'equals': EqualsCondition, 'not_equals': NotEqualsCondition, 'greater_than': GreaterThanCondition, 'less_than': LessThanCondition, 'contains': ContainsCondition}`. Assignment stores a value/reference; it is not an equality test.

**L0058.** Continue the statement starting at L53 with `"contains": ContainsCondition`. Assign to `condition_types`: construct a dictionary mapping the displayed keys to values: `{'equals': EqualsCondition, 'not_equals': NotEqualsCondition, 'greater_than': GreaterThanCondition, 'less_than': LessThanCondition, 'contains': ContainsCondition}`. Assignment stores a value/reference; it is not an equality test.

**L0059.** Close the grouped expression/declaration introduced at L53; delimiters/commas complete the same statement rather than execute a separate operation.

**L0060.** Assign to `condition_class`: read a mapping key with a default (or call this object's get method as identified by the receiver): `condition_types.get(condition_type)`. Assignment stores a value/reference; it is not an equality test.

**L0061.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `condition_class is None`; this produces the branch/assertion's truth value.

**L0062.** Raise construct an invalid value/configuration exception: `ValueError(f'Unsupported condition type: {condition_type}')`. Normal execution at this point stops.

**L0063.** Return from this function: call `condition_class` with the displayed positional/named arguments: `condition_class(field=field, value=value)`.

**L0064.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0065.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0066.** Define class `ActionFactory`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0067.** Decorate the following factory/helper so it does not receive an implicit self instance argument.

**L0068.** Define function/method `create(action_type: str, config: Mapping[str, Any] | None=None, gmail_service: Any=None)` with intended return type `Action`. 

**L0069.** Continue the function signature: `action_type: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0070.** Continue the function signature: `config: Mapping[str, Any] | None = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0071.** Continue the function signature: `gmail_service: Any = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0072.** Continue the function signature: `) -> Action:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0073.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `action_type == 'noop'`; this produces the branch/assertion's truth value.

**L0074.** Return from this function: call `NoOpAction` with the displayed positional/named arguments: `NoOpAction()`.

**L0075.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `action_type == 'http'`; this produces the branch/assertion's truth value.

**L0076.** Return from this function: call `HttpAction` with the displayed positional/named arguments: `HttpAction(config or {})`.

**L0077.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `action_type == 'github'`; this produces the branch/assertion's truth value.

**L0078.** Return from this function: call `GitHubAction` with the displayed positional/named arguments: `GitHubAction(config or {})`.

**L0079.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `action_type == 'email'`; this produces the branch/assertion's truth value.

**L0080.** Return from this function: call `EmailAction` with the displayed positional/named arguments: `EmailAction(config or {}, gmail_service=gmail_service)`.

**L0081.** Raise construct an invalid value/configuration exception: `ValueError(f'Unsupported action type: {action_type}')`. Normal execution at this point stops.


<a id="backend-app-core-triggers-initpy"></a>
## backend/app/core/triggers/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `b1c976deeef3434742f884e43706ade9e1ca97842f6f0523ed58ec6b61e391e2`. Physical lines: 6.

### Numbered source

```python
0001 | from app.core.triggers.base import Trigger
0002 | from app.core.triggers.manual import ManualTrigger
0003 | from app.core.triggers.scheduled import ScheduledTrigger
0004 | from app.core.triggers.webhook import WebhookTrigger
0005 | 
0006 | __all__ = ["ManualTrigger", "ScheduledTrigger", "Trigger", "WebhookTrigger"]
```

### Every-line explanation

**L0001.** Import Trigger from `app.core.triggers.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import ManualTrigger from `app.core.triggers.manual`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import ScheduledTrigger from `app.core.triggers.scheduled`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import WebhookTrigger from `app.core.triggers.webhook`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Assign to `__all__`: construct a list containing the displayed values: `['ManualTrigger', 'ScheduledTrigger', 'Trigger', 'WebhookTrigger']`. Assignment stores a value/reference; it is not an equality test.


<a id="backend-app-core-triggers-basepy"></a>
## backend/app/core/triggers/base.py

Trigger's abstract boolean contract. It checks an already delivered normalized event; a trigger class is not itself a network receiver or timer.

Source fingerprint: `1b7c332454492956c68fcacefe064d9c37ccde5bb9657760d7924260ca5dad20`. Physical lines: 9.

### Numbered source

```python
0001 | from abc import ABC, abstractmethod
0002 | 
0003 | from app.core.event import Event
0004 | 
0005 | 
0006 | class Trigger(ABC):
0007 |     @abstractmethod
0008 |     def should_execute(self, event: Event) -> bool:
0009 |         """Return True when this workflow should start for the given event."""
```

### Every-line explanation

**L0001.** Import ABC, abstractmethod from `abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import Event from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `Trigger` inheriting `ABC`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Mark the next method as required by the ABC mechanism before a subclass can normally be instantiated.

**L0008.** Define function/method `should_execute(self, event: Event)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0009.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.


<a id="backend-app-core-triggers-manualpy"></a>
## backend/app/core/triggers/manual.py

Manual matches type manual OR source manual. This is intentionally broader than matching only the type. It does not inspect payload.source.

Source fingerprint: `5d911343a72fd92020220654d16da4d25f1789574f96b56fc81c4dfb8cd96b2f`. Physical lines: 9.

### Numbered source

```python
0001 | from app.core.event import Event
0002 | from app.core.triggers.base import Trigger
0003 | 
0004 | 
0005 | class ManualTrigger(Trigger):
0006 |     """Matches operator-initiated or test events. No external webhook required."""
0007 | 
0008 |     def should_execute(self, event: Event) -> bool:
0009 |         return event.type == "manual" or event.source == "manual"
```

### Every-line explanation

**L0001.** Import Event from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Trigger from `app.core.triggers.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Define class `ManualTrigger` inheriting `Trigger`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0006.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Define function/method `should_execute(self, event: Event)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0009.** Return from this function: evaluate the short-circuit boolean expression `event.type == 'manual' or event.source == 'manual'`; later terms run only when needed.


<a id="backend-app-core-triggers-scheduledpy"></a>
## backend/app/core/triggers/scheduled.py

Only an event-type predicate. There is no timer, cron scheduling, job persistence, or automatic event generation in this file or the running application.

Source fingerprint: `32b5f6782d7e330000d036235d05fb8ead98148d37742d9ab043ecc73b31282a`. Physical lines: 7.

### Numbered source

```python
0001 | from app.core.event import Event
0002 | from app.core.triggers.base import Trigger
0003 | 
0004 | 
0005 | class ScheduledTrigger(Trigger):
0006 |     def should_execute(self, event: Event) -> bool:
0007 |         return event.type == "scheduled"
```

### Every-line explanation

**L0001.** Import Event from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Trigger from `app.core.triggers.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Define class `ScheduledTrigger` inheriting `Trigger`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0006.** Define function/method `should_execute(self, event: Event)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0007.** Return from this function: evaluate the comparison/membership/identity test `event.type == 'scheduled'`; this produces the branch/assertion's truth value.


<a id="backend-app-core-triggers-webhookpy"></a>
## backend/app/core/triggers/webhook.py

Webhook requires normalized type webhook and optionally restricts the source. None means no source restriction in the core object.

Source fingerprint: `494869a9da3201093fee3765a638b0b080cfeb20dc90a28aaa322395823b523d`. Physical lines: 12.

### Numbered source

```python
0001 | from app.core.event import Event
0002 | from app.core.triggers.base import Trigger
0003 | 
0004 | 
0005 | class WebhookTrigger(Trigger):
0006 |     def __init__(self, source: str | None = None) -> None:
0007 |         self.source = source
0008 | 
0009 |     def should_execute(self, event: Event) -> bool:
0010 |         if event.type != "webhook":
0011 |             return False
0012 |         return self.source is None or event.source == self.source
```

### Every-line explanation

**L0001.** Import Event from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Trigger from `app.core.triggers.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Define class `WebhookTrigger` inheriting `Trigger`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0006.** Define function/method `__init__(self, source: str | None=None)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0007.** Assign to `self.source`: read/evaluate `source`. Assignment stores a value/reference; it is not an equality test.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Define function/method `should_execute(self, event: Event)` with intended return type `bool`.  `self` is supplied by an ordinary bound method call.

**L0010.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `event.type != 'webhook'`; this produces the branch/assertion's truth value.

**L0011.** Return from this function: use literal value `False` (bool).

**L0012.** Return from this function: evaluate the short-circuit boolean expression `self.source is None or event.source == self.source`; later terms run only when needed.


<a id="backend-app-core-workflowpy"></a>
## backend/app/core/workflow.py

Runtime object composition: name, Trigger, optional Condition, ordered Actions. It is not an ORM row and does not itself execute. Ordinary Python references are stored without runtime type enforcement.

Source fingerprint: `f0b4d88955bc3e76f174f6fd8eafdb06fb4270d35042c7ed23e4725ef8247731`. Physical lines: 19.

### Numbered source

```python
0001 | from app.core.actions.base import Action
0002 | from app.core.conditions.base import Condition
0003 | from app.core.triggers.base import Trigger
0004 | 
0005 | 
0006 | class Workflow:
0007 |     """Composable workflow configuration object. Not the execution engine."""
0008 | 
0009 |     def __init__(
0010 |         self,
0011 |         name: str,
0012 |         trigger: Trigger,
0013 |         condition: Condition | None,
0014 |         actions: list[Action],
0015 |     ) -> None:
0016 |         self.name = name
0017 |         self.trigger = trigger
0018 |         self.condition = condition
0019 |         self.actions = actions
```

### Every-line explanation

**L0001.** Import Action from `app.core.actions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Condition from `app.core.conditions.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import Trigger from `app.core.triggers.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `Workflow`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Define function/method `__init__(self, name: str, trigger: Trigger, condition: Condition | None, actions: list[Action])` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0010.** Continue the function signature: `self,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0011.** Continue the function signature: `name: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0012.** Continue the function signature: `trigger: Trigger,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0013.** Continue the function signature: `condition: Condition | None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0014.** Continue the function signature: `actions: list[Action],`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0015.** Close the grouped expression/declaration introduced at L9; delimiters/commas complete the same statement rather than execute a separate operation.

**L0016.** Assign to `self.name`: read/evaluate `name`. Assignment stores a value/reference; it is not an equality test.

**L0017.** Assign to `self.trigger`: read/evaluate `trigger`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Assign to `self.condition`: read/evaluate `condition`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Assign to `self.actions`: read/evaluate `actions`. Assignment stores a value/reference; it is not an equality test.


<a id="backend-app-dbpy"></a>
## backend/app/db.py

Database engine and transaction-scoped dependency. SQLAlchemy engine is unrelated to WorkflowEngine. flush sends SQL in a transaction; get_session commits/rolls back/closes. create_all is initial table creation, not versioned migration management.

Source fingerprint: `66444d3ff5181ffae3d68eca0a19df357afde58326eb20589656173f499c054c`. Physical lines: 31.

### Numbered source

```python
0001 | from collections.abc import Generator
0002 | 
0003 | from sqlalchemy import create_engine
0004 | from sqlalchemy.orm import Session, sessionmaker
0005 | 
0006 | from app.config import settings
0007 | from app.models import Base  # noqa: F401 — register all mapped tables
0008 | 
0009 | connect_args = {}
0010 | if settings.database_url.startswith("sqlite"):
0011 |     connect_args = {"check_same_thread": False}
0012 | 
0013 | engine = create_engine(settings.database_url, connect_args=connect_args)
0014 | SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
0015 | 
0016 | 
0017 | def init_db() -> None:
0018 |     """Create tables for this greenfield SQLite slice. Replace with Alembic later."""
0019 |     Base.metadata.create_all(bind=engine)
0020 | 
0021 | 
0022 | def get_session() -> Generator[Session, None, None]:
0023 |     session = SessionLocal()
0024 |     try:
0025 |         yield session
0026 |         session.commit()
0027 |     except Exception:
0028 |         session.rollback()
0029 |         raise
0030 |     finally:
0031 |         session.close()
```

### Every-line explanation

**L0001.** Import Generator from `collections.abc`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import create_engine from `sqlalchemy`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import Session, sessionmaker from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import Base from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Assign to `connect_args`: construct a dictionary mapping the displayed keys to values: `{}`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Enter the following indented branch only if you call `settings.database_url.startswith` with the displayed positional/named arguments: `settings.database_url.startswith('sqlite')`.

**L0011.** Assign to `connect_args`: construct a dictionary mapping the displayed keys to values: `{'check_same_thread': False}`. Assignment stores a value/reference; it is not an equality test.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Assign to `engine`: create SQLAlchemy's database engine/connection manager: `create_engine(settings.database_url, connect_args=connect_args)`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Assign to `SessionLocal`: build a factory for database Session objects: `sessionmaker(bind=engine, autocommit=False, autoflush=False)`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Define function/method `init_db()` with intended return type `None`. 

**L0018.** Docstring text documents this module/class/function; it does not execute a workflow or validate the described promise by itself.

**L0019.** Perform the expression for its effect: create currently missing mapped database tables (not migrate existing schemas): `Base.metadata.create_all(bind=engine)`.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0022.** Define function/method `get_session()` with intended return type `Generator[Session, None, None]`. 

**L0023.** Assign to `session`: allocate a database unit-of-work session: `SessionLocal()`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0025.** Yield `session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0026.** Perform the expression for its effect: commit the current database transaction: `session.commit()`.

**L0027.** Catch `Exception`; execute this error branch instead of continuing the failed statement.

**L0028.** Perform the expression for its effect: undo the current database transaction on a propagated exception: `session.rollback()`.

**L0029.** Raise the currently handled exception again. Normal execution at this point stops.

**L0030.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0031.** Perform the expression for its effect: release the Session's resources: `session.close()`.


<a id="backend-app-mainpy"></a>
## backend/app/main.py

Application composition root. Startup creates tables, CORS permits configured/local origins, and the API router mounts routes. The async lifespan contains synchronous initialization and yields control to the application's running phase.

Source fingerprint: `de0acfea470dc96dd003e6737a19e9b4560ea34f289178c4813fdd2b827f15cc`. Physical lines: 27.

### Numbered source

```python
0001 | from contextlib import asynccontextmanager
0002 | 
0003 | from fastapi import FastAPI
0004 | from fastapi.middleware.cors import CORSMiddleware
0005 | 
0006 | from app.api.routes import api_router
0007 | from app.config import settings
0008 | from app.db import init_db
0009 | 
0010 | 
0011 | @asynccontextmanager
0012 | async def lifespan(_app: FastAPI):
0013 |     init_db()
0014 |     yield
0015 | 
0016 | 
0017 | app = FastAPI(title="FlowForge", lifespan=lifespan)
0018 | app.add_middleware(
0019 |     CORSMiddleware,
0020 |     allow_origins=sorted(
0021 |         {settings.frontend_origin, "http://localhost:5173", "http://127.0.0.1:5173"}
0022 |     ),
0023 |     allow_credentials=True,
0024 |     allow_methods=["*"],
0025 |     allow_headers=["*"],
0026 | )
0027 | app.include_router(api_router)
```

### Every-line explanation

**L0001.** Import asynccontextmanager from `contextlib`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import FastAPI from `fastapi`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import CORSMiddleware from `fastapi.middleware.cors`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Import api_router from `app.api.routes`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Import init_db from `app.db`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Transform the following async generator into a lifespan context manager with setup before yield and cleanup afterward.

**L0012.** Define async function/method `lifespan(_app: FastAPI)`. 

**L0013.** Perform the expression for its effect: call `init_db` with the displayed positional/named arguments: `init_db()`.

**L0014.** Yield control to the running application; code after yield is resumed during normal lifecycle/cleanup.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Assign to `app`: call `FastAPI` with the displayed positional/named arguments: `FastAPI(title='FlowForge', lifespan=lifespan)`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0019.** Continue the statement starting at L18 with `CORSMiddleware`. Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0020.** Continue the statement starting at L18 with `allow_origins=sorted(`. Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0021.** Continue the statement starting at L18 with `{settings.frontend_origin, "http://localhost:5173", "http://127.0.0.1:5173"}`. Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0022.** Close the grouped expression/declaration introduced at L18; delimiters/commas complete the same statement rather than execute a separate operation.

**L0023.** Continue the statement starting at L18 with `allow_credentials=True`. Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0024.** Continue the statement starting at L18 with `allow_methods=["*"]`. Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0025.** Continue the statement starting at L18 with `allow_headers=["*"]`. Perform the expression for its effect: call `app.add_middleware` with the displayed positional/named arguments: `app.add_middleware(CORSMiddleware, allow_origins=sorted({settings.frontend_origin, 'http://localhost:5173', 'http://127.0.0.1:5173'}), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])`.

**L0026.** Close the grouped expression/declaration introduced at L18; delimiters/commas complete the same statement rather than execute a separate operation.

**L0027.** Perform the expression for its effect: call `app.include_router` with the displayed positional/named arguments: `app.include_router(api_router)`.


<a id="backend-app-models-initpy"></a>
## backend/app/models/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `6d67557c0250c8668c3cc78a0539e5da4104ee29c4e8b204b578303642a0208e`. Physical lines: 25.

### Numbered source

```python
0001 | from app.models.base import Base
0002 | from app.models.entities import (
0003 |     Execution,
0004 |     GmailConnection,
0005 |     GmailOAuthState,
0006 |     Integration,
0007 |     User,
0008 |     Workflow,
0009 |     WorkflowAction,
0010 |     WorkflowCondition,
0011 |     WorkflowTrigger,
0012 | )
0013 | 
0014 | __all__ = [
0015 |     "Base",
0016 |     "Execution",
0017 |     "GmailConnection",
0018 |     "GmailOAuthState",
0019 |     "Integration",
0020 |     "User",
0021 |     "Workflow",
0022 |     "WorkflowAction",
0023 |     "WorkflowCondition",
0024 |     "WorkflowTrigger",
0025 | ]
```

### Every-line explanation

**L0001.** Import Base from `app.models.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import Execution, GmailConnection, GmailOAuthState, Integration, User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger from `app.models.entities`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Continue the parenthesized import from `app.models.entities` with name(s) `Execution`.

**L0004.** Continue the parenthesized import from `app.models.entities` with name(s) `GmailConnection`.

**L0005.** Continue the parenthesized import from `app.models.entities` with name(s) `GmailOAuthState`.

**L0006.** Continue the parenthesized import from `app.models.entities` with name(s) `Integration`.

**L0007.** Continue the parenthesized import from `app.models.entities` with name(s) `User`.

**L0008.** Continue the parenthesized import from `app.models.entities` with name(s) `Workflow`.

**L0009.** Continue the parenthesized import from `app.models.entities` with name(s) `WorkflowAction`.

**L0010.** Continue the parenthesized import from `app.models.entities` with name(s) `WorkflowCondition`.

**L0011.** Continue the parenthesized import from `app.models.entities` with name(s) `WorkflowTrigger`.

**L0012.** Close the grouped expression/declaration introduced at L2; delimiters/commas complete the same statement rather than execute a separate operation.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Continue the statement starting at L14 with `"Base"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0016.** Continue the statement starting at L14 with `"Execution"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0017.** Continue the statement starting at L14 with `"GmailConnection"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Continue the statement starting at L14 with `"GmailOAuthState"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Continue the statement starting at L14 with `"Integration"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0020.** Continue the statement starting at L14 with `"User"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0021.** Continue the statement starting at L14 with `"Workflow"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0022.** Continue the statement starting at L14 with `"WorkflowAction"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0023.** Continue the statement starting at L14 with `"WorkflowCondition"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Continue the statement starting at L14 with `"WorkflowTrigger"`. Assign to `__all__`: construct a list containing the displayed values: `['Base', 'Execution', 'GmailConnection', 'GmailOAuthState', 'Integration', 'User', 'Workflow', 'WorkflowAction', 'WorkflowCondition', 'WorkflowTrigger']`. Assignment stores a value/reference; it is not an equality test.

**L0025.** Close the grouped expression/declaration introduced at L14; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-models-basepy"></a>
## backend/app/models/base.py

SQLAlchemy declarative Base, per-row UUID-string generator, and created_at mixin. server_default executes in the database; callable default=new_id is distinct from prematurely calling new_id().

Source fingerprint: `70a95ee5620acad6b8b79a09553d388c5ccbcec46121d50ccb23138521c2e236`. Physical lines: 19.

### Numbered source

```python
0001 | from datetime import datetime
0002 | from uuid import uuid4
0003 | 
0004 | from sqlalchemy import DateTime, func
0005 | from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
0006 | 
0007 | 
0008 | def new_id() -> str:
0009 |     return str(uuid4())
0010 | 
0011 | 
0012 | class Base(DeclarativeBase):
0013 |     pass
0014 | 
0015 | 
0016 | class TimestampMixin:
0017 |     created_at: Mapped[datetime] = mapped_column(
0018 |         DateTime(timezone=True), server_default=func.now(), nullable=False
0019 |     )
```

### Every-line explanation

**L0001.** Import datetime from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import uuid4 from `uuid`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import DateTime, func from `sqlalchemy`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import DeclarativeBase, Mapped, mapped_column from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Define function/method `new_id()` with intended return type `str`. 

**L0009.** Return from this function: convert a value to its string representation: `str(uuid4())`.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Define class `Base` inheriting `DeclarativeBase`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0013.** Empty placeholder body required by Python syntax; SQLAlchemy's base class supplies inherited behavior here.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Define class `TimestampMixin`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0017.** Declare `created_at` with intended type `Mapped[datetime]` and map it to persistence: timestamp column requesting timezone support; `server_default=func.now()` supplies a database-side insert default; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0018.** Continue the statement starting at L17 with `DateTime(timezone=True), server_default=func.now(), nullable=False`. Declare `created_at` with intended type `Mapped[datetime]` and map it to persistence: timestamp column requesting timezone support; `server_default=func.now()` supplies a database-side insert default; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0019.** Close the grouped expression/declaration introduced at L17; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-models-entitiespy"></a>
## backend/app/models/entities.py

Nine persisted entities, distinct from runtime/Pydantic objects. Relationships express navigation and ORM cascades; foreign keys/uniqueness express constraints. Gmail token columns hold ciphertext created by the service, while generic JSON config is not automatically encrypted.

Source fingerprint: `2606acf557c019ca1ba057bf26056b83bce457e1703f6f97ad7520a9aa8727f3`. Physical lines: 130.

### Numbered source

```python
0001 | from datetime import datetime
0002 | 
0003 | from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
0004 | from sqlalchemy.orm import Mapped, mapped_column, relationship
0005 | from sqlalchemy.types import JSON
0006 | 
0007 | from app.models.base import Base, TimestampMixin, new_id
0008 | 
0009 | 
0010 | class User(TimestampMixin, Base):
0011 |     __tablename__ = "users"
0012 | 
0013 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0014 |     email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
0015 | 
0016 |     workflows: Mapped[list["Workflow"]] = relationship(back_populates="user")
0017 |     integrations: Mapped[list["Integration"]] = relationship(back_populates="user")
0018 | 
0019 | 
0020 | class Workflow(TimestampMixin, Base):
0021 |     __tablename__ = "workflows"
0022 | 
0023 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0024 |     user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
0025 |     name: Mapped[str] = mapped_column(String(200), nullable=False)
0026 |     enabled: Mapped[bool] = mapped_column(default=False, nullable=False)
0027 |     updated_at: Mapped[datetime] = mapped_column(
0028 |         DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
0029 |     )
0030 | 
0031 |     user: Mapped[User] = relationship(back_populates="workflows")
0032 |     trigger: Mapped["WorkflowTrigger | None"] = relationship(
0033 |         back_populates="workflow", uselist=False, cascade="all, delete-orphan"
0034 |     )
0035 |     conditions: Mapped[list["WorkflowCondition"]] = relationship(
0036 |         back_populates="workflow", cascade="all, delete-orphan"
0037 |     )
0038 |     actions: Mapped[list["WorkflowAction"]] = relationship(
0039 |         back_populates="workflow", cascade="all, delete-orphan", order_by="WorkflowAction.position"
0040 |     )
0041 |     executions: Mapped[list["Execution"]] = relationship(
0042 |         back_populates="workflow", cascade="all, delete-orphan"
0043 |     )
0044 | 
0045 | 
0046 | class WorkflowTrigger(Base):
0047 |     __tablename__ = "workflow_triggers"
0048 | 
0049 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0050 |     workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), unique=True, nullable=False)
0051 |     trigger_type: Mapped[str] = mapped_column(String(64), nullable=False)
0052 |     config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
0053 | 
0054 |     workflow: Mapped[Workflow] = relationship(back_populates="trigger")
0055 | 
0056 | 
0057 | class WorkflowCondition(Base):
0058 |     __tablename__ = "workflow_conditions"
0059 | 
0060 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0061 |     workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), nullable=False)
0062 |     parent_id: Mapped[str | None] = mapped_column(ForeignKey("workflow_conditions.id"), nullable=True)
0063 |     condition_type: Mapped[str] = mapped_column(String(64), nullable=False)
0064 |     config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
0065 | 
0066 |     workflow: Mapped[Workflow] = relationship(back_populates="conditions")
0067 | 
0068 | 
0069 | class Integration(TimestampMixin, Base):
0070 |     __tablename__ = "integrations"
0071 | 
0072 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0073 |     user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
0074 |     provider: Mapped[str] = mapped_column(String(64), nullable=False)
0075 |     config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
0076 | 
0077 |     user: Mapped[User] = relationship(back_populates="integrations")
0078 |     actions: Mapped[list["WorkflowAction"]] = relationship(back_populates="integration")
0079 | 
0080 | 
0081 | class GmailConnection(TimestampMixin, Base):
0082 |     __tablename__ = "gmail_connections"
0083 | 
0084 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0085 |     user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
0086 |     email: Mapped[str] = mapped_column(String(320), nullable=False)
0087 |     access_token: Mapped[str] = mapped_column(Text, nullable=False)
0088 |     refresh_token: Mapped[str] = mapped_column(Text, nullable=False)
0089 |     token_expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
0090 | 
0091 |     user: Mapped[User] = relationship()
0092 | 
0093 | 
0094 | class GmailOAuthState(Base):
0095 |     __tablename__ = "gmail_oauth_states"
0096 | 
0097 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0098 |     state_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
0099 |     user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
0100 |     expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
0101 |     used_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
0102 | 
0103 | 
0104 | class WorkflowAction(Base):
0105 |     __tablename__ = "workflow_actions"
0106 | 
0107 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0108 |     workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), nullable=False)
0109 |     integration_id: Mapped[str | None] = mapped_column(ForeignKey("integrations.id"), nullable=True)
0110 |     position: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
0111 |     action_type: Mapped[str] = mapped_column(String(64), nullable=False)
0112 |     config: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
0113 | 
0114 |     workflow: Mapped[Workflow] = relationship(back_populates="actions")
0115 |     integration: Mapped[Integration | None] = relationship(back_populates="actions")
0116 | 
0117 | 
0118 | class Execution(Base):
0119 |     __tablename__ = "executions"
0120 | 
0121 |     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_id)
0122 |     workflow_id: Mapped[str] = mapped_column(ForeignKey("workflows.id"), nullable=False)
0123 |     status: Mapped[str] = mapped_column(String(32), nullable=False, default="PENDING")
0124 |     started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
0125 |     completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
0126 |     trigger_data: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
0127 |     result: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
0128 |     error: Mapped[str | None] = mapped_column(Text, nullable=True)
0129 | 
0130 |     workflow: Mapped[Workflow] = relationship(back_populates="executions")
```

### Every-line explanation

**L0001.** Import datetime from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import DateTime, ForeignKey, Integer, String, Text, func from `sqlalchemy`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import Mapped, mapped_column, relationship from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import JSON from `sqlalchemy.types`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Import Base, TimestampMixin, new_id from `app.models.base`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Define class `User` inheriting `TimestampMixin, Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0011.** Assign to `__tablename__`: use literal value `'users'` (str). Assignment stores a value/reference; it is not an equality test.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0014.** Declare `email` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 320 (exact enforcement depends on the database); `unique=True` disallows duplicate non-null values; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Declare `workflows` with intended type `Mapped[list['Workflow']]` as ORM object navigation, not another physical column. `back_populates='user'` names the reverse ORM relationship.

**L0017.** Declare `integrations` with intended type `Mapped[list['Integration']]` as ORM object navigation, not another physical column. `back_populates='user'` names the reverse ORM relationship.

**L0018.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Define class `Workflow` inheriting `TimestampMixin, Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0021.** Assign to `__tablename__`: use literal value `'workflows'` (str). Assignment stores a value/reference; it is not an equality test.

**L0022.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0023.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0024.** Declare `user_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `users.id`; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0025.** Declare `name` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 200 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0026.** Declare `enabled` with intended type `Mapped[bool]` and map it to persistence: `default=False` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0027.** Declare `updated_at` with intended type `Mapped[datetime]` and map it to persistence: timestamp column requesting timezone support; `server_default=func.now()` supplies a database-side insert default; `onupdate=func.now()` supplies a value when this row is updated; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0028.** Continue the statement starting at L27 with `DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False`. Declare `updated_at` with intended type `Mapped[datetime]` and map it to persistence: timestamp column requesting timezone support; `server_default=func.now()` supplies a database-side insert default; `onupdate=func.now()` supplies a value when this row is updated; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0029.** Close the grouped expression/declaration introduced at L27; delimiters/commas complete the same statement rather than execute a separate operation.

**L0030.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0031.** Declare `user` with intended type `Mapped[User]` as ORM object navigation, not another physical column. `back_populates='workflows'` names the reverse ORM relationship.

**L0032.** Declare `trigger` with intended type `Mapped['WorkflowTrigger | None']` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `uselist=False` False requests one related object rather than a collection; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent.

**L0033.** Continue the statement starting at L32 with `back_populates="workflow", uselist=False, cascade="all, delete-orphan"`. Declare `trigger` with intended type `Mapped['WorkflowTrigger | None']` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `uselist=False` False requests one related object rather than a collection; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent.

**L0034.** Close the grouped expression/declaration introduced at L32; delimiters/commas complete the same statement rather than execute a separate operation.

**L0035.** Declare `conditions` with intended type `Mapped[list['WorkflowCondition']]` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent.

**L0036.** Continue the statement starting at L35 with `back_populates="workflow", cascade="all, delete-orphan"`. Declare `conditions` with intended type `Mapped[list['WorkflowCondition']]` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent.

**L0037.** Close the grouped expression/declaration introduced at L35; delimiters/commas complete the same statement rather than execute a separate operation.

**L0038.** Declare `actions` with intended type `Mapped[list['WorkflowAction']]` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent; `order_by='WorkflowAction.position'` orders loaded related actions by their persisted position.

**L0039.** Continue the statement starting at L38 with `back_populates="workflow", cascade="all, delete-orphan", order_by="WorkflowAction.position"`. Declare `actions` with intended type `Mapped[list['WorkflowAction']]` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent; `order_by='WorkflowAction.position'` orders loaded related actions by their persisted position.

**L0040.** Close the grouped expression/declaration introduced at L38; delimiters/commas complete the same statement rather than execute a separate operation.

**L0041.** Declare `executions` with intended type `Mapped[list['Execution']]` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent.

**L0042.** Continue the statement starting at L41 with `back_populates="workflow", cascade="all, delete-orphan"`. Declare `executions` with intended type `Mapped[list['Execution']]` as ORM object navigation, not another physical column. `back_populates='workflow'` names the reverse ORM relationship; `cascade='all, delete-orphan'` all/delete-orphan propagates ORM operations and removes owned children disconnected from the parent.

**L0043.** Close the grouped expression/declaration introduced at L41; delimiters/commas complete the same statement rather than execute a separate operation.

**L0044.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0045.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0046.** Define class `WorkflowTrigger` inheriting `Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0047.** Assign to `__tablename__`: use literal value `'workflow_triggers'` (str). Assignment stores a value/reference; it is not an equality test.

**L0048.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0049.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0050.** Declare `workflow_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `workflows.id`; `unique=True` disallows duplicate non-null values; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0051.** Declare `trigger_type` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 64 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0052.** Declare `config` with intended type `Mapped[dict]` and map it to persistence: JSON configuration/data column; JSON storage does not automatically encrypt its values; `default=dict` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0053.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0054.** Declare `workflow` with intended type `Mapped[Workflow]` as ORM object navigation, not another physical column. `back_populates='trigger'` names the reverse ORM relationship.

**L0055.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0056.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0057.** Define class `WorkflowCondition` inheriting `Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0058.** Assign to `__tablename__`: use literal value `'workflow_conditions'` (str). Assignment stores a value/reference; it is not an equality test.

**L0059.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0060.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0061.** Declare `workflow_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `workflows.id`; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0062.** Declare `parent_id` with intended type `Mapped[str | None]` and map it to persistence: foreign-key reference to `workflow_conditions.id`; `nullable=True` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0063.** Declare `condition_type` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 64 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0064.** Declare `config` with intended type `Mapped[dict]` and map it to persistence: JSON configuration/data column; JSON storage does not automatically encrypt its values; `default=dict` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0065.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0066.** Declare `workflow` with intended type `Mapped[Workflow]` as ORM object navigation, not another physical column. `back_populates='conditions'` names the reverse ORM relationship.

**L0067.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0068.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0069.** Define class `Integration` inheriting `TimestampMixin, Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0070.** Assign to `__tablename__`: use literal value `'integrations'` (str). Assignment stores a value/reference; it is not an equality test.

**L0071.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0072.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0073.** Declare `user_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `users.id`; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0074.** Declare `provider` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 64 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0075.** Declare `config` with intended type `Mapped[dict]` and map it to persistence: JSON configuration/data column; JSON storage does not automatically encrypt its values; `default=dict` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0076.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0077.** Declare `user` with intended type `Mapped[User]` as ORM object navigation, not another physical column. `back_populates='integrations'` names the reverse ORM relationship.

**L0078.** Declare `actions` with intended type `Mapped[list['WorkflowAction']]` as ORM object navigation, not another physical column. `back_populates='integration'` names the reverse ORM relationship.

**L0079.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0080.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0081.** Define class `GmailConnection` inheriting `TimestampMixin, Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0082.** Assign to `__tablename__`: use literal value `'gmail_connections'` (str). Assignment stores a value/reference; it is not an equality test.

**L0083.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0084.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0085.** Declare `user_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `users.id`; `unique=True` disallows duplicate non-null values; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0086.** Declare `email` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 320 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0087.** Declare `access_token` with intended type `Mapped[str]` and map it to persistence: text column suitable for longer values/ciphertext; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0088.** Declare `refresh_token` with intended type `Mapped[str]` and map it to persistence: text column suitable for longer values/ciphertext; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0089.** Declare `token_expires_at` with intended type `Mapped[datetime]` and map it to persistence: timestamp column requesting timezone support; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0090.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0091.** Declare `user` with intended type `Mapped[User]` as ORM object navigation, not another physical column. SQLAlchemy infers the relationship from mapped types/foreign keys.

**L0092.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0093.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0094.** Define class `GmailOAuthState` inheriting `Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0095.** Assign to `__tablename__`: use literal value `'gmail_oauth_states'` (str). Assignment stores a value/reference; it is not an equality test.

**L0096.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0097.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0098.** Declare `state_hash` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 64 (exact enforcement depends on the database); `unique=True` disallows duplicate non-null values; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0099.** Declare `user_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `users.id`; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0100.** Declare `expires_at` with intended type `Mapped[datetime]` and map it to persistence: timestamp column requesting timezone support; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0101.** Declare `used_at` with intended type `Mapped[datetime | None]` and map it to persistence: timestamp column requesting timezone support; `nullable=True` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0102.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0103.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0104.** Define class `WorkflowAction` inheriting `Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0105.** Assign to `__tablename__`: use literal value `'workflow_actions'` (str). Assignment stores a value/reference; it is not an equality test.

**L0106.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0107.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0108.** Declare `workflow_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `workflows.id`; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0109.** Declare `integration_id` with intended type `Mapped[str | None]` and map it to persistence: foreign-key reference to `integrations.id`; `nullable=True` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0110.** Declare `position` with intended type `Mapped[int]` and map it to persistence: integer column; `nullable=False` controls whether SQL NULL is permitted; `default=0` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0111.** Declare `action_type` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 64 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0112.** Declare `config` with intended type `Mapped[dict]` and map it to persistence: JSON configuration/data column; JSON storage does not automatically encrypt its values; `default=dict` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0113.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0114.** Declare `workflow` with intended type `Mapped[Workflow]` as ORM object navigation, not another physical column. `back_populates='actions'` names the reverse ORM relationship.

**L0115.** Declare `integration` with intended type `Mapped[Integration | None]` as ORM object navigation, not another physical column. `back_populates='actions'` names the reverse ORM relationship.

**L0116.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0117.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0118.** Define class `Execution` inheriting `Base`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0119.** Assign to `__tablename__`: use literal value `'executions'` (str). Assignment stores a value/reference; it is not an equality test.

**L0120.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0121.** Declare `id` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 36 (exact enforcement depends on the database); `primary_key=True` identifies a row uniquely; `default=new_id` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0122.** Declare `workflow_id` with intended type `Mapped[str]` and map it to persistence: foreign-key reference to `workflows.id`; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0123.** Declare `status` with intended type `Mapped[str]` and map it to persistence: string column with declared maximum length 32 (exact enforcement depends on the database); `nullable=False` controls whether SQL NULL is permitted; `default='PENDING'` supplies an application-side insert default; a callable is invoked when needed. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0124.** Declare `started_at` with intended type `Mapped[datetime | None]` and map it to persistence: timestamp column requesting timezone support; `nullable=True` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0125.** Declare `completed_at` with intended type `Mapped[datetime | None]` and map it to persistence: timestamp column requesting timezone support; `nullable=True` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0126.** Declare `trigger_data` with intended type `Mapped[dict]` and map it to persistence: JSON configuration/data column; JSON storage does not automatically encrypt its values; `default=dict` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0127.** Declare `result` with intended type `Mapped[dict]` and map it to persistence: JSON configuration/data column; JSON storage does not automatically encrypt its values; `default=dict` supplies an application-side insert default; a callable is invoked when needed; `nullable=False` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0128.** Declare `error` with intended type `Mapped[str | None]` and map it to persistence: text column suitable for longer values/ciphertext; `nullable=True` controls whether SQL NULL is permitted. SQLAlchemy interprets this declaration; a plain annotation alone would not create a table column.

**L0129.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0130.** Declare `workflow` with intended type `Mapped[Workflow]` as ORM object navigation, not another physical column. `back_populates='executions'` names the reverse ORM relationship.


<a id="backend-app-repositories-initpy"></a>
## backend/app/repositories/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `a71da2e39fddb35bf65ab8763a0413750bb908898814dc3f371945c550df4d49`. Physical lines: 4.

### Numbered source

```python
0001 | 
0002 | from app.repositories.workflow import WorkflowRepository
0003 | 
0004 | __all__ = ["WorkflowRepository"]
```

### Every-line explanation

**L0001.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0002.** Import WorkflowRepository from `app.repositories.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Assign to `__all__`: construct a list containing the displayed values: `['WorkflowRepository']`. Assignment stores a value/reference; it is not an equality test.


<a id="backend-app-repositories-workflowpy"></a>
## backend/app/repositories/workflow.py

Focused SQLAlchemy lookups, additions, and owner/history listing. list methods are filtered and sorted but not paginated. Ownership authorization is checked by routes, not automatically by this class.

Source fingerprint: `e16306246d62625839fae05c27b377f774bb2c3463cb5db999f9c0486bbacb5e`. Physical lines: 32.

### Numbered source

```python
0001 | from sqlalchemy.orm import Session
0002 | 
0003 | from app.models import Execution, Workflow
0004 | 
0005 | 
0006 | class WorkflowRepository:
0007 |     def __init__(self, session: Session) -> None:
0008 |         self.session = session
0009 | 
0010 |     def get(self, workflow_id: str) -> Workflow | None:
0011 |         return self.session.get(Workflow, workflow_id)
0012 | 
0013 |     def add(self, workflow: Workflow) -> Workflow:
0014 |         self.session.add(workflow)
0015 |         self.session.flush()
0016 |         return workflow
0017 | 
0018 |     def list_for_user(self, user_id: str) -> list[Workflow]:
0019 |         return list(
0020 |             self.session.query(Workflow)
0021 |             .filter(Workflow.user_id == user_id)
0022 |             .order_by(Workflow.updated_at.desc())
0023 |             .all()
0024 |         )
0025 | 
0026 |     def executions(self, workflow_id: str) -> list[Execution]:
0027 |         return list(
0028 |             self.session.query(Execution)
0029 |             .filter(Execution.workflow_id == workflow_id)
0030 |             .order_by(Execution.started_at.desc())
0031 |             .all()
0032 |         )
```

### Every-line explanation

**L0001.** Import Session from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import Execution, Workflow from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `WorkflowRepository`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Define function/method `__init__(self, session: Session)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0008.** Assign to `self.session`: read/evaluate `session`. Assignment stores a value/reference; it is not an equality test.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Define function/method `get(self, workflow_id: str)` with intended return type `Workflow | None`.  `self` is supplied by an ordinary bound method call.

**L0011.** Return from this function: look up a mapped row by primary key in this session: `self.session.get(Workflow, workflow_id)`.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Define function/method `add(self, workflow: Workflow)` with intended return type `Workflow`.  `self` is supplied by an ordinary bound method call.

**L0014.** Perform the expression for its effect: stage an ORM object for persistence in this service's session: `self.session.add(workflow)`.

**L0015.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0016.** Return from this function: read/evaluate `workflow`.

**L0017.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0018.** Define function/method `list_for_user(self, user_id: str)` with intended return type `list[Workflow]`.  `self` is supplied by an ordinary bound method call.

**L0019.** Return from this function: materialize an iterable into a list: `list(self.session.query(Workflow).filter(Workflow.user_id == user_id).order_by(Workflow.updated_at.desc()).all())`.

**L0020.** Continue the statement starting at L19 with `self.session.query(Workflow)`. Return from this function: materialize an iterable into a list: `list(self.session.query(Workflow).filter(Workflow.user_id == user_id).order_by(Workflow.updated_at.desc()).all())`.

**L0021.** Continue the statement starting at L19 with `.filter(Workflow.user_id == user_id)`. Return from this function: materialize an iterable into a list: `list(self.session.query(Workflow).filter(Workflow.user_id == user_id).order_by(Workflow.updated_at.desc()).all())`.

**L0022.** Continue the statement starting at L19 with `.order_by(Workflow.updated_at.desc())`. Return from this function: materialize an iterable into a list: `list(self.session.query(Workflow).filter(Workflow.user_id == user_id).order_by(Workflow.updated_at.desc()).all())`.

**L0023.** Continue the statement starting at L19 with `.all()`. Return from this function: materialize an iterable into a list: `list(self.session.query(Workflow).filter(Workflow.user_id == user_id).order_by(Workflow.updated_at.desc()).all())`.

**L0024.** Close the grouped expression/declaration introduced at L19; delimiters/commas complete the same statement rather than execute a separate operation.

**L0025.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0026.** Define function/method `executions(self, workflow_id: str)` with intended return type `list[Execution]`.  `self` is supplied by an ordinary bound method call.

**L0027.** Return from this function: materialize an iterable into a list: `list(self.session.query(Execution).filter(Execution.workflow_id == workflow_id).order_by(Execution.started_at.desc()).all())`.

**L0028.** Continue the statement starting at L27 with `self.session.query(Execution)`. Return from this function: materialize an iterable into a list: `list(self.session.query(Execution).filter(Execution.workflow_id == workflow_id).order_by(Execution.started_at.desc()).all())`.

**L0029.** Continue the statement starting at L27 with `.filter(Execution.workflow_id == workflow_id)`. Return from this function: materialize an iterable into a list: `list(self.session.query(Execution).filter(Execution.workflow_id == workflow_id).order_by(Execution.started_at.desc()).all())`.

**L0030.** Continue the statement starting at L27 with `.order_by(Execution.started_at.desc())`. Return from this function: materialize an iterable into a list: `list(self.session.query(Execution).filter(Execution.workflow_id == workflow_id).order_by(Execution.started_at.desc()).all())`.

**L0031.** Continue the statement starting at L27 with `.all()`. Return from this function: materialize an iterable into a list: `list(self.session.query(Execution).filter(Execution.workflow_id == workflow_id).order_by(Execution.started_at.desc()).all())`.

**L0032.** Close the grouped expression/declaration introduced at L27; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-app-schemas-initpy"></a>
## backend/app/schemas/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6`. Physical lines: 1.

### Numbered source

```python
0001 | 
```

### Every-line explanation

**L0001.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.


<a id="backend-app-schemas-healthpy"></a>
## backend/app/schemas/health.py

Pydantic response shape for the liveness endpoint: two strings, status and service.

Source fingerprint: `ade553292e72fb40a633069592db9f4d9b640a1949bf0c787203c462edbc2719`. Physical lines: 6.

### Numbered source

```python
0001 | from pydantic import BaseModel
0002 | 
0003 | 
0004 | class HealthResponse(BaseModel):
0005 |     status: str
0006 |     service: str
```

### Every-line explanation

**L0001.** Import BaseModel from `pydantic`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Define class `HealthResponse` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0005.** Declare `status` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0006.** Declare `service` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.


<a id="backend-app-schemas-workflowspy"></a>
## backend/app/schemas/workflows.py

Pydantic API shapes. Names have length bounds; component config remains broad. Empty action lists are allowed. WorkflowUpdate replaces config rather than implementing partial PATCH. Response models distinguish summaries from full editable details.

Source fingerprint: `6de5496e0f1e5c7e3dae80ab2aedf356316a556529eac7a6ede418b9b740ee02`. Physical lines: 51.

### Numbered source

```python
0001 | from typing import Any
0002 | 
0003 | from pydantic import BaseModel, Field
0004 | 
0005 | 
0006 | class ComponentConfig(BaseModel):
0007 |     type: str
0008 |     config: dict[str, Any] = Field(default_factory=dict)
0009 | 
0010 | 
0011 | class WorkflowCreate(BaseModel):
0012 |     user_id: str
0013 |     name: str = Field(min_length=1, max_length=200)
0014 |     enabled: bool = False
0015 |     trigger: ComponentConfig
0016 |     conditions: list[ComponentConfig] = Field(default_factory=list)
0017 |     actions: list[ComponentConfig] = Field(default_factory=list)
0018 | 
0019 | 
0020 | class WorkflowUpdate(BaseModel):
0021 |     name: str = Field(min_length=1, max_length=200)
0022 |     enabled: bool
0023 |     trigger: ComponentConfig
0024 |     conditions: list[ComponentConfig] = Field(default_factory=list)
0025 |     actions: list[ComponentConfig] = Field(default_factory=list)
0026 | 
0027 | 
0028 | class WorkflowResponse(BaseModel):
0029 |     id: str
0030 |     user_id: str
0031 |     name: str
0032 |     enabled: bool
0033 | 
0034 | 
0035 | class WorkflowDetailResponse(WorkflowResponse):
0036 |     trigger: ComponentConfig
0037 |     conditions: list[ComponentConfig]
0038 |     actions: list[ComponentConfig]
0039 | 
0040 | 
0041 | class ManualRunRequest(BaseModel):
0042 |     payload: dict[str, Any] = Field(default_factory=dict)
0043 | 
0044 | 
0045 | class ExecutionResponse(BaseModel):
0046 |     id: str
0047 |     workflow_id: str
0048 |     status: str
0049 |     trigger_data: dict[str, Any]
0050 |     result: dict[str, Any]
0051 |     error: str | None
```

### Every-line explanation

**L0001.** Import Any from `typing`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import BaseModel, Field from `pydantic`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define class `ComponentConfig` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0007.** Declare `type` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0008.** Declare `config` with intended type `dict[str, Any]` and initialize it: declare Pydantic field defaults/validation metadata: `Field(default_factory=dict)`.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Define class `WorkflowCreate` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0012.** Declare `user_id` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0013.** Declare `name` with intended type `str` and initialize it: declare Pydantic field defaults/validation metadata: `Field(min_length=1, max_length=200)`.

**L0014.** Declare `enabled` with intended type `bool` and initialize it: use literal value `False` (bool).

**L0015.** Declare `trigger` with intended type `ComponentConfig`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0016.** Declare `conditions` with intended type `list[ComponentConfig]` and initialize it: declare Pydantic field defaults/validation metadata: `Field(default_factory=list)`.

**L0017.** Declare `actions` with intended type `list[ComponentConfig]` and initialize it: declare Pydantic field defaults/validation metadata: `Field(default_factory=list)`.

**L0018.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Define class `WorkflowUpdate` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0021.** Declare `name` with intended type `str` and initialize it: declare Pydantic field defaults/validation metadata: `Field(min_length=1, max_length=200)`.

**L0022.** Declare `enabled` with intended type `bool`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0023.** Declare `trigger` with intended type `ComponentConfig`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0024.** Declare `conditions` with intended type `list[ComponentConfig]` and initialize it: declare Pydantic field defaults/validation metadata: `Field(default_factory=list)`.

**L0025.** Declare `actions` with intended type `list[ComponentConfig]` and initialize it: declare Pydantic field defaults/validation metadata: `Field(default_factory=list)`.

**L0026.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0027.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0028.** Define class `WorkflowResponse` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0029.** Declare `id` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0030.** Declare `user_id` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0031.** Declare `name` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0032.** Declare `enabled` with intended type `bool`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0033.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0034.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0035.** Define class `WorkflowDetailResponse` inheriting `WorkflowResponse`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0036.** Declare `trigger` with intended type `ComponentConfig`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0037.** Declare `conditions` with intended type `list[ComponentConfig]`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0038.** Declare `actions` with intended type `list[ComponentConfig]`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0039.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0040.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0041.** Define class `ManualRunRequest` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0042.** Declare `payload` with intended type `dict[str, Any]` and initialize it: declare Pydantic field defaults/validation metadata: `Field(default_factory=dict)`.

**L0043.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0044.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0045.** Define class `ExecutionResponse` inheriting `BaseModel`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0046.** Declare `id` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0047.** Declare `workflow_id` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0048.** Declare `status` with intended type `str`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0049.** Declare `trigger_data` with intended type `dict[str, Any]`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0050.** Declare `result` with intended type `dict[str, Any]`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.

**L0051.** Declare `error` with intended type `str | None`; dataclass/Pydantic/ORM machinery interprets this declaration according to its containing class.


<a id="backend-app-services-initpy"></a>
## backend/app/services/__init__.py

Package initializer. Imports/re-exports organize the public module surface and may register mapped classes. Empty/blank initializers provide package structure without runtime workflow behavior. __all__ is an export convention, not security.

Source fingerprint: `7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6`. Physical lines: 1.

### Numbered source

```python
0001 | 
```

### Every-line explanation

**L0001.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.


<a id="backend-app-services-gmailpy"></a>
## backend/app/services/gmail.py

Google OAuth token exchange/profile, per-user encrypted connection storage, refresh, and MIME send. Hashing state, encrypting recoverable tokens, and base64url message encoding solve three different problems. Local disconnect does not revoke Google consent.

Source fingerprint: `a03aae65a108e7c5fec8d2806baa986979eb4009c7b491439cdc38611fcbfd1f`. Physical lines: 192.

### Numbered source

```python
0001 | import base64
0002 | import hashlib
0003 | import secrets
0004 | from datetime import datetime, timedelta, timezone
0005 | from email.message import EmailMessage
0006 | from email.utils import formataddr
0007 | from urllib.parse import urlencode
0008 | 
0009 | import httpx
0010 | from cryptography.fernet import Fernet, InvalidToken
0011 | from sqlalchemy.orm import Session
0012 | 
0013 | from app.config import settings
0014 | from app.models import GmailConnection
0015 | 
0016 | 
0017 | class GmailService:
0018 |     def __init__(self, session: Session) -> None:
0019 |         self.session = session
0020 | 
0021 |     @staticmethod
0022 |     def _cipher() -> Fernet:
0023 |         if not settings.token_encryption_key:
0024 |             raise RuntimeError("Gmail token encryption is not configured")
0025 |         try:
0026 |             return Fernet(settings.token_encryption_key.encode())
0027 |         except (ValueError, TypeError) as exc:
0028 |             raise RuntimeError("Gmail token encryption key is invalid") from exc
0029 | 
0030 |     @staticmethod
0031 |     def hash_state(state: str) -> str:
0032 |         return hashlib.sha256(state.encode()).hexdigest()
0033 | 
0034 |     def oauth_url(self, state: str) -> str:
0035 |         if not settings.google_client_id or not settings.google_client_secret:
0036 |             raise RuntimeError("Google OAuth is not configured")
0037 |         query = urlencode(
0038 |             {
0039 |                 "client_id": settings.google_client_id,
0040 |                 "redirect_uri": settings.google_redirect_uri,
0041 |                 "response_type": "code",
0042 |                 "scope": "openid email https://www.googleapis.com/auth/gmail.send",
0043 |                 "access_type": "offline",
0044 |                 "prompt": "consent",
0045 |                 "state": state,
0046 |             }
0047 |         )
0048 |         return f"https://accounts.google.com/o/oauth2/v2/auth?{query}"
0049 | 
0050 |     def exchange_code(self, code: str) -> tuple[str, str, datetime]:
0051 |         response = httpx.post(
0052 |             "https://oauth2.googleapis.com/token",
0053 |             data={
0054 |                 "client_id": settings.google_client_id,
0055 |                 "client_secret": settings.google_client_secret,
0056 |                 "code": code,
0057 |                 "grant_type": "authorization_code",
0058 |                 "redirect_uri": settings.google_redirect_uri,
0059 |             },
0060 |             timeout=10.0,
0061 |         )
0062 |         if response.status_code != 200:
0063 |             try:
0064 |                 error = response.json().get("error")
0065 |                 description = response.json().get("error_description")
0066 |             except ValueError:
0067 |                 error = None
0068 |                 description = None
0069 |             detail = error if isinstance(error, str) else "unknown_error"
0070 |             if isinstance(description, str) and description:
0071 |                 detail = f"{detail}: {description}"
0072 |             raise RuntimeError(f"Google OAuth token exchange failed ({detail})")
0073 |         data = response.json()
0074 |         access_token = data.get("access_token")
0075 |         refresh_token = data.get("refresh_token")
0076 |         expires_in = data.get("expires_in")
0077 |         if not all(isinstance(item, str) for item in (access_token, refresh_token)) or not isinstance(
0078 |             expires_in, int
0079 |         ):
0080 |             raise RuntimeError("Google OAuth response was invalid")
0081 |         return access_token, refresh_token, datetime.now(timezone.utc) + timedelta(seconds=expires_in)
0082 | 
0083 |     def profile(self, access_token: str) -> str:
0084 |         response = httpx.get(
0085 |             "https://openidconnect.googleapis.com/v1/userinfo",
0086 |             headers={"Authorization": f"Bearer {access_token}"},
0087 |             timeout=10.0,
0088 |         )
0089 |         if response.status_code != 200:
0090 |             raise RuntimeError(f"Could not read the Gmail profile (status {response.status_code})")
0091 |         email = response.json().get("email")
0092 |         if not isinstance(email, str) or "@" not in email:
0093 |             raise RuntimeError("Google did not return a valid Gmail address")
0094 |         return email
0095 | 
0096 |     def save_connection(
0097 |         self, user_id: str, email: str, access_token: str, refresh_token: str, expires_at: datetime
0098 |     ) -> GmailConnection:
0099 |         connection = self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()
0100 |         if connection is None:
0101 |             connection = GmailConnection(user_id=user_id, email=email, access_token="", refresh_token="")
0102 |             self.session.add(connection)
0103 |         cipher = self._cipher()
0104 |         connection.email = email
0105 |         connection.access_token = cipher.encrypt(access_token.encode()).decode()
0106 |         connection.refresh_token = cipher.encrypt(refresh_token.encode()).decode()
0107 |         connection.token_expires_at = expires_at
0108 |         self.session.flush()
0109 |         return connection
0110 | 
0111 |     def disconnect(self, user_id: str) -> None:
0112 |         connection = self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()
0113 |         if connection is not None:
0114 |             self.session.delete(connection)
0115 |             self.session.flush()
0116 | 
0117 |     def connection(self, user_id: str) -> GmailConnection | None:
0118 |         return self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()
0119 | 
0120 |     def _decrypt(self, value: str) -> str:
0121 |         try:
0122 |             return self._cipher().decrypt(value.encode()).decode()
0123 |         except (InvalidToken, UnicodeDecodeError) as exc:
0124 |             raise RuntimeError("Stored Gmail credentials are invalid") from exc
0125 | 
0126 |     def _refresh(self, connection: GmailConnection, refresh_token: str) -> str:
0127 |         response = httpx.post(
0128 |             "https://oauth2.googleapis.com/token",
0129 |             data={
0130 |                 "client_id": settings.google_client_id,
0131 |                 "client_secret": settings.google_client_secret,
0132 |                 "refresh_token": refresh_token,
0133 |                 "grant_type": "refresh_token",
0134 |             },
0135 |             timeout=10.0,
0136 |         )
0137 |         if response.status_code != 200:
0138 |             raise RuntimeError("Gmail authorization expired; reconnect Gmail")
0139 |         access_token = response.json().get("access_token")
0140 |         expires_in = response.json().get("expires_in", 3600)
0141 |         if not isinstance(access_token, str) or not isinstance(expires_in, int):
0142 |             raise RuntimeError("Gmail token refresh response was invalid")
0143 |         connection.access_token = self._cipher().encrypt(access_token.encode()).decode()
0144 |         connection.token_expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
0145 |         self.session.flush()
0146 |         return access_token
0147 | 
0148 |     def send(
0149 |         self,
0150 |         user_id: str,
0151 |         recipients: list[str],
0152 |         subject: str,
0153 |         text: str,
0154 |         html: str | None,
0155 |         sender: str | None = None,
0156 |     ) -> dict[str, object]:
0157 |         connection = self.connection(user_id)
0158 |         if connection is None:
0159 |             raise RuntimeError("Connect Gmail before using the email action")
0160 |         access_token = self._decrypt(connection.access_token)
0161 |         refresh_token = self._decrypt(connection.refresh_token)
0162 |         expires_at = connection.token_expires_at
0163 |         if expires_at.tzinfo is None:
0164 |             expires_at = expires_at.replace(tzinfo=timezone.utc)
0165 |         if expires_at <= datetime.now(timezone.utc) + timedelta(minutes=1):
0166 |             access_token = self._refresh(connection, refresh_token)
0167 | 
0168 |         message = EmailMessage()
0169 |         message["From"] = formataddr(("FlowForge", connection.email))
0170 |         message["To"] = ", ".join(recipients)
0171 |         message["Subject"] = subject
0172 |         message.set_content(text)
0173 |         if html:
0174 |             message.add_alternative(html, subtype="html")
0175 |         encoded = base64.urlsafe_b64encode(message.as_bytes()).decode()
0176 |         response = httpx.post(
0177 |             "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
0178 |             headers={"Authorization": f"Bearer {access_token}"},
0179 |             json={"raw": encoded},
0180 |             timeout=settings.http_action_timeout_seconds,
0181 |         )
0182 |         if response.status_code >= 400:
0183 |             raise RuntimeError(f"Gmail API returned status {response.status_code}")
0184 |         provider_id = response.json().get("id")
0185 |         result: dict[str, object] = {"type": "email", "provider": "gmail", "status": "sent"}
0186 |         if isinstance(provider_id, str):
0187 |             result["provider_id"] = provider_id
0188 |         return result
0189 | 
0190 | 
0191 | def new_oauth_state() -> str:
0192 |     return secrets.token_urlsafe(32)
```

### Every-line explanation

**L0001.** Import module(s) `base64`. Top-level module code runs on first import.

**L0002.** Import module(s) `hashlib`. Top-level module code runs on first import.

**L0003.** Import module(s) `secrets`. Top-level module code runs on first import.

**L0004.** Import datetime, timedelta, timezone from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import EmailMessage from `email.message`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import formataddr from `email.utils`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import urlencode from `urllib.parse`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Import module(s) `httpx`. Top-level module code runs on first import.

**L0010.** Import Fernet, InvalidToken from `cryptography.fernet`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Import Session from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0014.** Import GmailConnection from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Define class `GmailService`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0018.** Define function/method `__init__(self, session: Session)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0019.** Assign to `self.session`: read/evaluate `session`. Assignment stores a value/reference; it is not an equality test.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Decorate the following factory/helper so it does not receive an implicit self instance argument.

**L0022.** Define function/method `_cipher()` with intended return type `Fernet`. 

**L0023.** Enter the following indented branch only if you negate the truth value of `settings.token_encryption_key`.

**L0024.** Raise construct an execution/integration failure exception: `RuntimeError('Gmail token encryption is not configured')`. Normal execution at this point stops.

**L0025.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0026.** Return from this function: construct authenticated symmetric encryption with the configured key: `Fernet(settings.token_encryption_key.encode())`.

**L0027.** Catch `(ValueError, TypeError)` as `exc`; execute this error branch instead of continuing the failed statement.

**L0028.** Raise construct an execution/integration failure exception: `RuntimeError('Gmail token encryption key is invalid')`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0029.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0030.** Decorate the following factory/helper so it does not receive an implicit self instance argument.

**L0031.** Define function/method `hash_state(state: str)` with intended return type `str`. 

**L0032.** Return from this function: format the digest as hexadecimal text: `hashlib.sha256(state.encode()).hexdigest()`.

**L0033.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0034.** Define function/method `oauth_url(self, state: str)` with intended return type `str`.  `self` is supplied by an ordinary bound method call.

**L0035.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not settings.google_client_id or not settings.google_client_secret`; later terms run only when needed.

**L0036.** Raise construct an execution/integration failure exception: `RuntimeError('Google OAuth is not configured')`. Normal execution at this point stops.

**L0037.** Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Continue the statement starting at L37 with `{`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0039.** Continue the statement starting at L37 with `"client_id": settings.google_client_id`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0040.** Continue the statement starting at L37 with `"redirect_uri": settings.google_redirect_uri`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0041.** Continue the statement starting at L37 with `"response_type": "code"`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0042.** Continue the statement starting at L37 with `"scope": "openid email https://www.googleapis.com/auth/gmail.send"`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Continue the statement starting at L37 with `"access_type": "offline"`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0044.** Continue the statement starting at L37 with `"prompt": "consent"`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0045.** Continue the statement starting at L37 with `"state": state`. Assign to `query`: encode a dictionary into URL query parameters: `urlencode({'client_id': settings.google_client_id, 'redirect_uri': settings.google_redirect_uri, 'response_type': 'code', 'scope': 'openid email https://www.googleapis.com/auth/gmail.send', 'access_type': 'offline', 'prompt': 'consent', 'state': state})`. Assignment stores a value/reference; it is not an equality test.

**L0046.** Close the grouped expression/declaration introduced at L37; delimiters/commas complete the same statement rather than execute a separate operation.

**L0047.** Close the grouped expression/declaration introduced at L37; delimiters/commas complete the same statement rather than execute a separate operation.

**L0048.** Return from this function: construct an f-string, interpolating expressions at runtime: `f'https://accounts.google.com/o/oauth2/v2/auth?{query}'`.

**L0049.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0050.** Define function/method `exchange_code(self, code: str)` with intended return type `tuple[str, str, datetime]`.  `self` is supplied by an ordinary bound method call.

**L0051.** Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0052.** Continue the statement starting at L51 with `"https://oauth2.googleapis.com/token"`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0053.** Continue the statement starting at L51 with `data={`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0054.** Continue the statement starting at L51 with `"client_id": settings.google_client_id`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Continue the statement starting at L51 with `"client_secret": settings.google_client_secret`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0056.** Continue the statement starting at L51 with `"code": code`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0057.** Continue the statement starting at L51 with `"grant_type": "authorization_code"`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0058.** Continue the statement starting at L51 with `"redirect_uri": settings.google_redirect_uri`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0059.** Close the grouped expression/declaration introduced at L51; delimiters/commas complete the same statement rather than execute a separate operation.

**L0060.** Continue the statement starting at L51 with `timeout=10.0`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'code': code, 'grant_type': 'authorization_code', 'redirect_uri': settings.google_redirect_uri}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0061.** Close the grouped expression/declaration introduced at L51; delimiters/commas complete the same statement rather than execute a separate operation.

**L0062.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response.status_code != 200`; this produces the branch/assertion's truth value.

**L0063.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0064.** Assign to `error`: read a mapping key with a default (or call this object's get method as identified by the receiver): `response.json().get('error')`. Assignment stores a value/reference; it is not an equality test.

**L0065.** Assign to `description`: read a mapping key with a default (or call this object's get method as identified by the receiver): `response.json().get('error_description')`. Assignment stores a value/reference; it is not an equality test.

**L0066.** Catch `ValueError`; execute this error branch instead of continuing the failed statement.

**L0067.** Assign to `error`: use literal value `None` (NoneType). Assignment stores a value/reference; it is not an equality test.

**L0068.** Assign to `description`: use literal value `None` (NoneType). Assignment stores a value/reference; it is not an equality test.

**L0069.** Assign to `detail`: choose `error` when `isinstance(error, str)` is true, otherwise `'unknown_error'`. Assignment stores a value/reference; it is not an equality test.

**L0070.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `isinstance(description, str) and description`; later terms run only when needed.

**L0071.** Assign to `detail`: construct an f-string, interpolating expressions at runtime: `f'{detail}: {description}'`. Assignment stores a value/reference; it is not an equality test.

**L0072.** Raise construct an execution/integration failure exception: `RuntimeError(f'Google OAuth token exchange failed ({detail})')`. Normal execution at this point stops.

**L0073.** Assign to `data`: decode this response's JSON body, potentially raising on invalid data: `response.json()`. Assignment stores a value/reference; it is not an equality test.

**L0074.** Assign to `access_token`: read a mapping key with a default (or call this object's get method as identified by the receiver): `data.get('access_token')`. Assignment stores a value/reference; it is not an equality test.

**L0075.** Assign to `refresh_token`: read a mapping key with a default (or call this object's get method as identified by the receiver): `data.get('refresh_token')`. Assignment stores a value/reference; it is not an equality test.

**L0076.** Assign to `expires_in`: read a mapping key with a default (or call this object's get method as identified by the receiver): `data.get('expires_in')`. Assignment stores a value/reference; it is not an equality test.

**L0077.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not all((isinstance(item, str) for item in (access_token, refresh_token))) or not isinstance(expires_in, int)`; later terms run only when needed.

**L0078.** Continue the statement starting at L77 with `expires_in, int`. Enter the following indented branch only if you evaluate the short-circuit boolean expression `not all((isinstance(item, str) for item in (access_token, refresh_token))) or not isinstance(expires_in, int)`; later terms run only when needed.

**L0079.** Continue the statement starting at L77 with `):`. Enter the following indented branch only if you evaluate the short-circuit boolean expression `not all((isinstance(item, str) for item in (access_token, refresh_token))) or not isinstance(expires_in, int)`; later terms run only when needed.

**L0080.** Raise construct an execution/integration failure exception: `RuntimeError('Google OAuth response was invalid')`. Normal execution at this point stops.

**L0081.** Return from this function: construct a tuple containing the displayed values: `(access_token, refresh_token, datetime.now(timezone.utc) + timedelta(seconds=expires_in))`.

**L0082.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0083.** Define function/method `profile(self, access_token: str)` with intended return type `str`.  `self` is supplied by an ordinary bound method call.

**L0084.** Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get('https://openidconnect.googleapis.com/v1/userinfo', headers={'Authorization': f'Bearer {access_token}'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0085.** Continue the statement starting at L84 with `"https://openidconnect.googleapis.com/v1/userinfo"`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get('https://openidconnect.googleapis.com/v1/userinfo', headers={'Authorization': f'Bearer {access_token}'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0086.** Continue the statement starting at L84 with `headers={"Authorization": f"Bearer {access_token}"}`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get('https://openidconnect.googleapis.com/v1/userinfo', headers={'Authorization': f'Bearer {access_token}'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0087.** Continue the statement starting at L84 with `timeout=10.0`. Assign to `response`: make a synchronous outbound HTTP GET (mocked where the test replaces it): `httpx.get('https://openidconnect.googleapis.com/v1/userinfo', headers={'Authorization': f'Bearer {access_token}'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0088.** Close the grouped expression/declaration introduced at L84; delimiters/commas complete the same statement rather than execute a separate operation.

**L0089.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response.status_code != 200`; this produces the branch/assertion's truth value.

**L0090.** Raise construct an execution/integration failure exception: `RuntimeError(f'Could not read the Gmail profile (status {response.status_code})')`. Normal execution at this point stops.

**L0091.** Assign to `email`: read a mapping key with a default (or call this object's get method as identified by the receiver): `response.json().get('email')`. Assignment stores a value/reference; it is not an equality test.

**L0092.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(email, str) or '@' not in email`; later terms run only when needed.

**L0093.** Raise construct an execution/integration failure exception: `RuntimeError('Google did not return a valid Gmail address')`. Normal execution at this point stops.

**L0094.** Return from this function: read/evaluate `email`.

**L0095.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0096.** Define function/method `save_connection(self, user_id: str, email: str, access_token: str, refresh_token: str, expires_at: datetime)` with intended return type `GmailConnection`.  `self` is supplied by an ordinary bound method call.

**L0097.** Continue the function signature: `self, user_id: str, email: str, access_token: str, refresh_token: str, expires_at: datetime`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0098.** Continue the function signature: `) -> GmailConnection:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0099.** Assign to `connection`: require zero or one matching row and reject duplicates: `self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()`. Assignment stores a value/reference; it is not an equality test.

**L0100.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `connection is None`; this produces the branch/assertion's truth value.

**L0101.** Assign to `connection`: call `GmailConnection` with the displayed positional/named arguments: `GmailConnection(user_id=user_id, email=email, access_token='', refresh_token='')`. Assignment stores a value/reference; it is not an equality test.

**L0102.** Perform the expression for its effect: stage an ORM object for persistence in this service's session: `self.session.add(connection)`.

**L0103.** Assign to `cipher`: call `self._cipher` with the displayed positional/named arguments: `self._cipher()`. Assignment stores a value/reference; it is not an equality test.

**L0104.** Assign to `connection.email`: read/evaluate `email`. Assignment stores a value/reference; it is not an equality test.

**L0105.** Assign to `connection.access_token`: convert bytes into text using the default UTF-8 encoding: `cipher.encrypt(access_token.encode()).decode()`. Assignment stores a value/reference; it is not an equality test.

**L0106.** Assign to `connection.refresh_token`: convert bytes into text using the default UTF-8 encoding: `cipher.encrypt(refresh_token.encode()).decode()`. Assignment stores a value/reference; it is not an equality test.

**L0107.** Assign to `connection.token_expires_at`: read/evaluate `expires_at`. Assignment stores a value/reference; it is not an equality test.

**L0108.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0109.** Return from this function: read/evaluate `connection`.

**L0110.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0111.** Define function/method `disconnect(self, user_id: str)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0112.** Assign to `connection`: require zero or one matching row and reject duplicates: `self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()`. Assignment stores a value/reference; it is not an equality test.

**L0113.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `connection is not None`; this produces the branch/assertion's truth value.

**L0114.** Perform the expression for its effect: mark an ORM object for deletion; configured cascades may delete dependents: `self.session.delete(connection)`.

**L0115.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0116.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0117.** Define function/method `connection(self, user_id: str)` with intended return type `GmailConnection | None`.  `self` is supplied by an ordinary bound method call.

**L0118.** Return from this function: require zero or one matching row and reject duplicates: `self.session.query(GmailConnection).filter_by(user_id=user_id).one_or_none()`.

**L0119.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0120.** Define function/method `_decrypt(self, value: str)` with intended return type `str`.  `self` is supplied by an ordinary bound method call.

**L0121.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0122.** Return from this function: convert bytes into text using the default UTF-8 encoding: `self._cipher().decrypt(value.encode()).decode()`.

**L0123.** Catch `(InvalidToken, UnicodeDecodeError)` as `exc`; execute this error branch instead of continuing the failed statement.

**L0124.** Raise construct an execution/integration failure exception: `RuntimeError('Stored Gmail credentials are invalid')`; `from` controls exception cause/chaining: `exc`. Normal execution at this point stops.

**L0125.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0126.** Define function/method `_refresh(self, connection: GmailConnection, refresh_token: str)` with intended return type `str`.  `self` is supplied by an ordinary bound method call.

**L0127.** Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0128.** Continue the statement starting at L127 with `"https://oauth2.googleapis.com/token"`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0129.** Continue the statement starting at L127 with `data={`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0130.** Continue the statement starting at L127 with `"client_id": settings.google_client_id`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0131.** Continue the statement starting at L127 with `"client_secret": settings.google_client_secret`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0132.** Continue the statement starting at L127 with `"refresh_token": refresh_token`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0133.** Continue the statement starting at L127 with `"grant_type": "refresh_token"`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0134.** Close the grouped expression/declaration introduced at L127; delimiters/commas complete the same statement rather than execute a separate operation.

**L0135.** Continue the statement starting at L127 with `timeout=10.0`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://oauth2.googleapis.com/token', data={'client_id': settings.google_client_id, 'client_secret': settings.google_client_secret, 'refresh_token': refresh_token, 'grant_type': 'refresh_token'}, timeout=10.0)`. Assignment stores a value/reference; it is not an equality test.

**L0136.** Close the grouped expression/declaration introduced at L127; delimiters/commas complete the same statement rather than execute a separate operation.

**L0137.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response.status_code != 200`; this produces the branch/assertion's truth value.

**L0138.** Raise construct an execution/integration failure exception: `RuntimeError('Gmail authorization expired; reconnect Gmail')`. Normal execution at this point stops.

**L0139.** Assign to `access_token`: read a mapping key with a default (or call this object's get method as identified by the receiver): `response.json().get('access_token')`. Assignment stores a value/reference; it is not an equality test.

**L0140.** Assign to `expires_in`: read a mapping key with a default (or call this object's get method as identified by the receiver): `response.json().get('expires_in', 3600)`. Assignment stores a value/reference; it is not an equality test.

**L0141.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `not isinstance(access_token, str) or not isinstance(expires_in, int)`; later terms run only when needed.

**L0142.** Raise construct an execution/integration failure exception: `RuntimeError('Gmail token refresh response was invalid')`. Normal execution at this point stops.

**L0143.** Assign to `connection.access_token`: convert bytes into text using the default UTF-8 encoding: `self._cipher().encrypt(access_token.encode()).decode()`. Assignment stores a value/reference; it is not an equality test.

**L0144.** Assign to `connection.token_expires_at`: compute `datetime.now(timezone.utc) + timedelta(seconds=expires_in)` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0145.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0146.** Return from this function: read/evaluate `access_token`.

**L0147.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0148.** Define function/method `send(self, user_id: str, recipients: list[str], subject: str, text: str, html: str | None, sender: str | None=None)` with intended return type `dict[str, object]`.  `self` is supplied by an ordinary bound method call.

**L0149.** Continue the function signature: `self,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0150.** Continue the function signature: `user_id: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0151.** Continue the function signature: `recipients: list[str],`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0152.** Continue the function signature: `subject: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0153.** Continue the function signature: `text: str,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0154.** Continue the function signature: `html: str | None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0155.** Continue the function signature: `sender: str | None = None,`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0156.** Continue the function signature: `) -> dict[str, object]:`. Annotations document types, defaults provide omitted arguments, commas separate parameters, and the colon starts the indented body.

**L0157.** Assign to `connection`: look up the user's stored Gmail connection without returning token values to the frontend: `self.connection(user_id)`. Assignment stores a value/reference; it is not an equality test.

**L0158.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `connection is None`; this produces the branch/assertion's truth value.

**L0159.** Raise construct an execution/integration failure exception: `RuntimeError('Connect Gmail before using the email action')`. Normal execution at this point stops.

**L0160.** Assign to `access_token`: call `self._decrypt` with the displayed positional/named arguments: `self._decrypt(connection.access_token)`. Assignment stores a value/reference; it is not an equality test.

**L0161.** Assign to `refresh_token`: call `self._decrypt` with the displayed positional/named arguments: `self._decrypt(connection.refresh_token)`. Assignment stores a value/reference; it is not an equality test.

**L0162.** Assign to `expires_at`: read attribute `token_expires_at` from `connection`. Assignment stores a value/reference; it is not an equality test.

**L0163.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `expires_at.tzinfo is None`; this produces the branch/assertion's truth value.

**L0164.** Assign to `expires_at`: replace the specified datetime field/timezone or string segment, according to receiver: `expires_at.replace(tzinfo=timezone.utc)`. Assignment stores a value/reference; it is not an equality test.

**L0165.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `expires_at <= datetime.now(timezone.utc) + timedelta(minutes=1)`; this produces the branch/assertion's truth value.

**L0166.** Assign to `access_token`: call `self._refresh` with the displayed positional/named arguments: `self._refresh(connection, refresh_token)`. Assignment stores a value/reference; it is not an equality test.

**L0167.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0168.** Assign to `message`: construct a MIME-aware email message object: `EmailMessage()`. Assignment stores a value/reference; it is not an equality test.

**L0169.** Assign to `message['From']`: format the display-name/address header safely using the email library: `formataddr(('FlowForge', connection.email))`. Assignment stores a value/reference; it is not an equality test.

**L0170.** Assign to `message['To']`: call `', '.join` with the displayed positional/named arguments: `', '.join(recipients)`. Assignment stores a value/reference; it is not an equality test.

**L0171.** Assign to `message['Subject']`: read/evaluate `subject`. Assignment stores a value/reference; it is not an equality test.

**L0172.** Perform the expression for its effect: add a plain text MIME body to the email message: `message.set_content(text)`.

**L0173.** Enter the following indented branch only if you read/evaluate `html`.

**L0174.** Perform the expression for its effect: add the optional HTML MIME alternative: `message.add_alternative(html, subtype='html')`.

**L0175.** Assign to `encoded`: convert bytes into text using the default UTF-8 encoding: `base64.urlsafe_b64encode(message.as_bytes()).decode()`. Assignment stores a value/reference; it is not an equality test.

**L0176.** Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', headers={'Authorization': f'Bearer {access_token}'}, json={'raw': encoded}, timeout=settings.http_action_timeout_seconds)`. Assignment stores a value/reference; it is not an equality test.

**L0177.** Continue the statement starting at L176 with `"https://gmail.googleapis.com/gmail/v1/users/me/messages/send"`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', headers={'Authorization': f'Bearer {access_token}'}, json={'raw': encoded}, timeout=settings.http_action_timeout_seconds)`. Assignment stores a value/reference; it is not an equality test.

**L0178.** Continue the statement starting at L176 with `headers={"Authorization": f"Bearer {access_token}"}`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', headers={'Authorization': f'Bearer {access_token}'}, json={'raw': encoded}, timeout=settings.http_action_timeout_seconds)`. Assignment stores a value/reference; it is not an equality test.

**L0179.** Continue the statement starting at L176 with `json={"raw": encoded}`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', headers={'Authorization': f'Bearer {access_token}'}, json={'raw': encoded}, timeout=settings.http_action_timeout_seconds)`. Assignment stores a value/reference; it is not an equality test.

**L0180.** Continue the statement starting at L176 with `timeout=settings.http_action_timeout_seconds`. Assign to `response`: make a synchronous outbound HTTP POST (mocked where the test replaces it): `httpx.post('https://gmail.googleapis.com/gmail/v1/users/me/messages/send', headers={'Authorization': f'Bearer {access_token}'}, json={'raw': encoded}, timeout=settings.http_action_timeout_seconds)`. Assignment stores a value/reference; it is not an equality test.

**L0181.** Close the grouped expression/declaration introduced at L176; delimiters/commas complete the same statement rather than execute a separate operation.

**L0182.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `response.status_code >= 400`; this produces the branch/assertion's truth value.

**L0183.** Raise construct an execution/integration failure exception: `RuntimeError(f'Gmail API returned status {response.status_code}')`. Normal execution at this point stops.

**L0184.** Assign to `provider_id`: read a mapping key with a default (or call this object's get method as identified by the receiver): `response.json().get('id')`. Assignment stores a value/reference; it is not an equality test.

**L0185.** Declare `result` with intended type `dict[str, object]` and initialize it: construct a dictionary mapping the displayed keys to values: `{'type': 'email', 'provider': 'gmail', 'status': 'sent'}`.

**L0186.** Enter the following indented branch only if you perform an actual runtime type check: `isinstance(provider_id, str)`.

**L0187.** Assign to `result['provider_id']`: read/evaluate `provider_id`. Assignment stores a value/reference; it is not an equality test.

**L0188.** Return from this function: read/evaluate `result`.

**L0189.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0190.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0191.** Define function/method `new_oauth_state()` with intended return type `str`. 

**L0192.** Return from this function: generate cryptographically strong random URL-safe text: `secrets.token_urlsafe(32)`.


<a id="backend-app-services-healthpy"></a>
## backend/app/services/health.py

Returns a fixed liveness response. It performs no database/provider checks.

Source fingerprint: `c179eb28fbc2857eec967f4b6eddf8ed24fa3ab17edc5f9262aa7e84353cb776`. Physical lines: 6.

### Numbered source

```python
0001 | from app.schemas.health import HealthResponse
0002 | 
0003 | 
0004 | class HealthService:
0005 |     def status(self) -> HealthResponse:
0006 |         return HealthResponse(status="ok", service="flowforge")
```

### Every-line explanation

**L0001.** Import HealthResponse from `app.schemas.health`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Define class `HealthService`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0005.** Define function/method `status(self)` with intended return type `HealthResponse`.  `self` is supplied by an ordinary bound method call.

**L0006.** Return from this function: construct/validate the health response fields: `HealthResponse(status='ok', service='flowforge')`.


<a id="backend-app-services-workflowpy"></a>
## backend/app/services/workflow.py

Use-case coordinator. Saves configuration, validates factory construction, hydrates objects, enforces enabled before run, and stores the engine result. Timestamps are currently generated after execution and only action_count is persisted from the result.

Source fingerprint: `ec3810bebd548042c627210f4a79614eadd2cb8c8469d009393ed6e03a4ea1cb`. Physical lines: 138.

### Numbered source

```python
0001 | from datetime import datetime, timezone
0002 | 
0003 | from sqlalchemy.orm import Session
0004 | 
0005 | from app.core.engine import WorkflowEngine
0006 | from app.core.event import Event
0007 | from app.core.factories import ActionFactory, ConditionFactory, TriggerFactory
0008 | from app.core.workflow import Workflow as RuntimeWorkflow
0009 | from app.models import Execution, User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger
0010 | from app.repositories.workflow import WorkflowRepository
0011 | from app.services.gmail import GmailService
0012 | from app.schemas.workflows import WorkflowCreate, WorkflowUpdate
0013 | 
0014 | 
0015 | class WorkflowService:
0016 |     def __init__(self, session: Session) -> None:
0017 |         self.session = session
0018 |         self.repository = WorkflowRepository(session)
0019 | 
0020 |     def create(self, request: WorkflowCreate) -> Workflow:
0021 |         if self.session.get(User, request.user_id) is None:
0022 |             raise ValueError("User does not exist")
0023 |         workflow = self.repository.add(
0024 |             Workflow(
0025 |                 user_id=request.user_id,
0026 |                 name=request.name,
0027 |                 enabled=request.enabled,
0028 |             )
0029 |         )
0030 |         workflow.trigger = WorkflowTrigger(
0031 |             trigger_type=request.trigger.type,
0032 |             config=request.trigger.config,
0033 |         )
0034 |         workflow.conditions = [
0035 |             WorkflowCondition(condition_type=item.type, config=item.config)
0036 |             for item in request.conditions
0037 |         ]
0038 |         workflow.actions = [
0039 |             WorkflowAction(position=index, action_type=item.type, config=item.config)
0040 |             for index, item in enumerate(request.actions)
0041 |         ]
0042 |         self.session.flush()
0043 |         self._validate_runtime(workflow)
0044 |         return workflow
0045 | 
0046 |     def update(self, workflow_id: str, request: WorkflowUpdate) -> Workflow:
0047 |         workflow = self.repository.get(workflow_id)
0048 |         if workflow is None:
0049 |             raise ValueError("Workflow not found")
0050 |         workflow.name = request.name
0051 |         workflow.enabled = request.enabled
0052 |         if workflow.trigger is None:
0053 |             workflow.trigger = WorkflowTrigger(
0054 |                 trigger_type=request.trigger.type,
0055 |                 config=request.trigger.config,
0056 |             )
0057 |         else:
0058 |             workflow.trigger.trigger_type = request.trigger.type
0059 |             workflow.trigger.config = request.trigger.config
0060 |         workflow.conditions = [
0061 |             WorkflowCondition(condition_type=item.type, config=item.config)
0062 |             for item in request.conditions
0063 |         ]
0064 |         workflow.actions = [
0065 |             WorkflowAction(position=index, action_type=item.type, config=item.config)
0066 |             for index, item in enumerate(request.actions)
0067 |         ]
0068 |         self.session.flush()
0069 |         self._validate_runtime(workflow)
0070 |         return workflow
0071 | 
0072 |     def delete(self, workflow_id: str) -> None:
0073 |         workflow = self.repository.get(workflow_id)
0074 |         if workflow is None:
0075 |             raise ValueError("Workflow not found")
0076 |         self.session.delete(workflow)
0077 |         self.session.flush()
0078 | 
0079 |     def _validate_runtime(self, workflow: Workflow) -> None:
0080 |         if workflow.trigger is None:
0081 |             raise ValueError("Workflow requires a trigger")
0082 |         TriggerFactory.create(workflow.trigger.trigger_type, workflow.trigger.config)
0083 |         for condition in workflow.conditions:
0084 |             ConditionFactory.create(condition.condition_type, condition.config)
0085 |         for action in workflow.actions:
0086 |             ActionFactory.create(action.action_type, action.config)
0087 | 
0088 |     def load_runtime(self, workflow_id: str) -> tuple[Workflow, RuntimeWorkflow]:
0089 |         stored = self.repository.get(workflow_id)
0090 |         if stored is None or stored.trigger is None:
0091 |             raise ValueError("Workflow configuration does not exist")
0092 |         trigger = TriggerFactory.create(stored.trigger.trigger_type, stored.trigger.config)
0093 |         condition = ConditionFactory.create("and", {"conditions": [
0094 |             {"type": row.condition_type, "config": row.config} for row in stored.conditions
0095 |         ]}) if len(stored.conditions) > 1 else (
0096 |             ConditionFactory.create(
0097 |                 stored.conditions[0].condition_type,
0098 |                 stored.conditions[0].config,
0099 |             ) if stored.conditions else None
0100 |         )
0101 |         actions = [
0102 |             ActionFactory.create(
0103 |                 row.action_type,
0104 |                 row.config,
0105 |                 gmail_service=GmailService(self.session),
0106 |             )
0107 |             for row in stored.actions
0108 |         ]
0109 |         return stored, RuntimeWorkflow(
0110 |             name=stored.name,
0111 |             trigger=trigger,
0112 |             condition=condition,
0113 |             actions=actions,
0114 |         )
0115 | 
0116 |     def run_manual(self, workflow_id: str, payload: dict) -> Execution:
0117 |         return self.run_event(
0118 |             workflow_id,
0119 |             Event(type="manual", source="manual", payload=payload),
0120 |         )
0121 | 
0122 |     def run_event(self, workflow_id: str, event: Event) -> Execution:
0123 |         stored, runtime = self.load_runtime(workflow_id)
0124 |         if not stored.enabled:
0125 |             raise ValueError("Workflow is disabled")
0126 |         result = WorkflowEngine().execute(runtime, event, user_id=stored.user_id)
0127 |         execution = Execution(
0128 |             workflow_id=stored.id,
0129 |             status=result.status.value,
0130 |             started_at=datetime.now(timezone.utc),
0131 |             completed_at=datetime.now(timezone.utc),
0132 |             trigger_data=event.payload,
0133 |             result={"action_count": result.action_count},
0134 |             error=result.error,
0135 |         )
0136 |         self.session.add(execution)
0137 |         self.session.flush()
0138 |         return execution
```

### Every-line explanation

**L0001.** Import datetime, timezone from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import Session from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import WorkflowEngine from `app.core.engine`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import Event from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import ActionFactory, ConditionFactory, TriggerFactory from `app.core.factories`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Alias the runtime composition class as RuntimeWorkflow to distinguish it from the ORM Workflow imported next.

**L0009.** Import Execution, User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Import WorkflowRepository from `app.repositories.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Import GmailService from `app.services.gmail`. Imported names become available in this module; aliases distinguish roles where used.

**L0012.** Import WorkflowCreate, WorkflowUpdate from `app.schemas.workflows`. Imported names become available in this module; aliases distinguish roles where used.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Define class `WorkflowService`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0016.** Define function/method `__init__(self, session: Session)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0017.** Assign to `self.session`: read/evaluate `session`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Assign to `self.repository`: construct the persistence helper using the supplied session: `WorkflowRepository(session)`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Define function/method `create(self, request: WorkflowCreate)` with intended return type `Workflow`.  `self` is supplied by an ordinary bound method call.

**L0021.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `self.session.get(User, request.user_id) is None`; this produces the branch/assertion's truth value.

**L0022.** Raise construct an invalid value/configuration exception: `ValueError('User does not exist')`. Normal execution at this point stops.

**L0023.** Assign to `workflow`: call `self.repository.add` with the displayed positional/named arguments: `self.repository.add(Workflow(user_id=request.user_id, name=request.name, enabled=request.enabled))`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Continue the statement starting at L23 with `Workflow(`. Assign to `workflow`: call `self.repository.add` with the displayed positional/named arguments: `self.repository.add(Workflow(user_id=request.user_id, name=request.name, enabled=request.enabled))`. Assignment stores a value/reference; it is not an equality test.

**L0025.** Continue the statement starting at L23 with `user_id=request.user_id`. Assign to `workflow`: call `self.repository.add` with the displayed positional/named arguments: `self.repository.add(Workflow(user_id=request.user_id, name=request.name, enabled=request.enabled))`. Assignment stores a value/reference; it is not an equality test.

**L0026.** Continue the statement starting at L23 with `name=request.name`. Assign to `workflow`: call `self.repository.add` with the displayed positional/named arguments: `self.repository.add(Workflow(user_id=request.user_id, name=request.name, enabled=request.enabled))`. Assignment stores a value/reference; it is not an equality test.

**L0027.** Continue the statement starting at L23 with `enabled=request.enabled`. Assign to `workflow`: call `self.repository.add` with the displayed positional/named arguments: `self.repository.add(Workflow(user_id=request.user_id, name=request.name, enabled=request.enabled))`. Assignment stores a value/reference; it is not an equality test.

**L0028.** Close the grouped expression/declaration introduced at L23; delimiters/commas complete the same statement rather than execute a separate operation.

**L0029.** Close the grouped expression/declaration introduced at L23; delimiters/commas complete the same statement rather than execute a separate operation.

**L0030.** Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type=request.trigger.type, config=request.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Continue the statement starting at L30 with `trigger_type=request.trigger.type`. Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type=request.trigger.type, config=request.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0032.** Continue the statement starting at L30 with `config=request.trigger.config`. Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type=request.trigger.type, config=request.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0033.** Close the grouped expression/declaration introduced at L30; delimiters/commas complete the same statement rather than execute a separate operation.

**L0034.** Assign to `workflow.conditions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowCondition(condition_type=item.type, config=item.config) for item in request.conditions]`. Assignment stores a value/reference; it is not an equality test.

**L0035.** Continue the statement starting at L34 with `WorkflowCondition(condition_type=item.type, config=item.config)`. Assign to `workflow.conditions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowCondition(condition_type=item.type, config=item.config) for item in request.conditions]`. Assignment stores a value/reference; it is not an equality test.

**L0036.** Continue the statement starting at L34 with `for item in request.conditions`. Assign to `workflow.conditions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowCondition(condition_type=item.type, config=item.config) for item in request.conditions]`. Assignment stores a value/reference; it is not an equality test.

**L0037.** Close the grouped expression/declaration introduced at L34; delimiters/commas complete the same statement rather than execute a separate operation.

**L0038.** Assign to `workflow.actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowAction(position=index, action_type=item.type, config=item.config) for index, item in enumerate(request.actions)]`. Assignment stores a value/reference; it is not an equality test.

**L0039.** Continue the statement starting at L38 with `WorkflowAction(position=index, action_type=item.type, config=item.config)`. Assign to `workflow.actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowAction(position=index, action_type=item.type, config=item.config) for index, item in enumerate(request.actions)]`. Assignment stores a value/reference; it is not an equality test.

**L0040.** Continue the statement starting at L38 with `for index, item in enumerate(request.actions)`. Assign to `workflow.actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowAction(position=index, action_type=item.type, config=item.config) for index, item in enumerate(request.actions)]`. Assignment stores a value/reference; it is not an equality test.

**L0041.** Close the grouped expression/declaration introduced at L38; delimiters/commas complete the same statement rather than execute a separate operation.

**L0042.** Flush child/parent configuration into the current transaction without committing it.

**L0043.** Build component objects to reject unsupported/bad configuration before the request can commit.

**L0044.** Return from this function: read/evaluate `workflow`.

**L0045.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0046.** Define function/method `update(self, workflow_id: str, request: WorkflowUpdate)` with intended return type `Workflow`.  `self` is supplied by an ordinary bound method call.

**L0047.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `self.repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0048.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0049.** Raise construct an invalid value/configuration exception: `ValueError('Workflow not found')`. Normal execution at this point stops.

**L0050.** Assign to `workflow.name`: read attribute `name` from `request`. Assignment stores a value/reference; it is not an equality test.

**L0051.** Assign to `workflow.enabled`: read attribute `enabled` from `request`. Assignment stores a value/reference; it is not an equality test.

**L0052.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow.trigger is None`; this produces the branch/assertion's truth value.

**L0053.** Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type=request.trigger.type, config=request.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0054.** Continue the statement starting at L53 with `trigger_type=request.trigger.type`. Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type=request.trigger.type, config=request.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Continue the statement starting at L53 with `config=request.trigger.config`. Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type=request.trigger.type, config=request.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0056.** Close the grouped expression/declaration introduced at L53; delimiters/commas complete the same statement rather than execute a separate operation.

**L0057.** Alternative branch when the preceding if condition is false, or the try completed without its expected exception (inspect the enclosing block).

**L0058.** Assign to `workflow.trigger.trigger_type`: read attribute `type` from `request.trigger`. Assignment stores a value/reference; it is not an equality test.

**L0059.** Assign to `workflow.trigger.config`: read attribute `config` from `request.trigger`. Assignment stores a value/reference; it is not an equality test.

**L0060.** Replace the stored condition collection; delete-orphan cascade removes disconnected old rows on flush.

**L0061.** Continue the statement starting at L60 with `WorkflowCondition(condition_type=item.type, config=item.config)`. Assign to `workflow.conditions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowCondition(condition_type=item.type, config=item.config) for item in request.conditions]`. Assignment stores a value/reference; it is not an equality test.

**L0062.** Continue the statement starting at L60 with `for item in request.conditions`. Assign to `workflow.conditions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowCondition(condition_type=item.type, config=item.config) for item in request.conditions]`. Assignment stores a value/reference; it is not an equality test.

**L0063.** Close the grouped expression/declaration introduced at L60; delimiters/commas complete the same statement rather than execute a separate operation.

**L0064.** Replace the action collection and rebuild position values, rather than partially merging actions.

**L0065.** Continue the statement starting at L64 with `WorkflowAction(position=index, action_type=item.type, config=item.config)`. Assign to `workflow.actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowAction(position=index, action_type=item.type, config=item.config) for index, item in enumerate(request.actions)]`. Assignment stores a value/reference; it is not an equality test.

**L0066.** Continue the statement starting at L64 with `for index, item in enumerate(request.actions)`. Assign to `workflow.actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[WorkflowAction(position=index, action_type=item.type, config=item.config) for index, item in enumerate(request.actions)]`. Assignment stores a value/reference; it is not an equality test.

**L0067.** Close the grouped expression/declaration introduced at L64; delimiters/commas complete the same statement rather than execute a separate operation.

**L0068.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0069.** Perform the expression for its effect: construct supported component objects to validate configuration: `self._validate_runtime(workflow)`.

**L0070.** Return from this function: read/evaluate `workflow`.

**L0071.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0072.** Define function/method `delete(self, workflow_id: str)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0073.** Assign to `workflow`: read a mapping key with a default (or call this object's get method as identified by the receiver): `self.repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0074.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow is None`; this produces the branch/assertion's truth value.

**L0075.** Raise construct an invalid value/configuration exception: `ValueError('Workflow not found')`. Normal execution at this point stops.

**L0076.** Perform the expression for its effect: mark an ORM object for deletion; configured cascades may delete dependents: `self.session.delete(workflow)`.

**L0077.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0078.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0079.** Define function/method `_validate_runtime(self, workflow: Workflow)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0080.** Enter the following indented branch only if you evaluate the comparison/membership/identity test `workflow.trigger is None`; this produces the branch/assertion's truth value.

**L0081.** Raise construct an invalid value/configuration exception: `ValueError('Workflow requires a trigger')`. Normal execution at this point stops.

**L0082.** Validate trigger factory construction without executing a workflow.

**L0083.** Iterate over `workflow.conditions`, binding each item/pair to `condition`. The indented body runs once per item unless it returns/raises/breaks.

**L0084.** Perform the expression for its effect: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create(condition.condition_type, condition.config)`.

**L0085.** Iterate over `workflow.actions`, binding each item/pair to `action`. The indented body runs once per item unless it returns/raises/breaks.

**L0086.** Validate an action's constructor. Gmail's service is absent here; its actual presence is checked during execution.

**L0087.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0088.** Return both the persisted row and a separate executable runtime composition.

**L0089.** Assign to `stored`: read a mapping key with a default (or call this object's get method as identified by the receiver): `self.repository.get(workflow_id)`. Assignment stores a value/reference; it is not an equality test.

**L0090.** Enter the following indented branch only if you evaluate the short-circuit boolean expression `stored is None or stored.trigger is None`; later terms run only when needed.

**L0091.** Raise construct an invalid value/configuration exception: `ValueError('Workflow configuration does not exist')`. Normal execution at this point stops.

**L0092.** Assign to `trigger`: construct a component through a factory, or call a service create use case as identified by receiver: `TriggerFactory.create(stored.trigger.trigger_type, stored.trigger.config)`. Assignment stores a value/reference; it is not an equality test.

**L0093.** For several condition rows, construct one implicit AND configuration around their type/config representations.

**L0094.** Continue the statement starting at L93 with `{"type": row.condition_type, "config": row.config} for row in stored.conditions`. Assign to `condition`: choose `ConditionFactory.create('and', {'conditions': [{'type': row.condition_type, 'config': row.config} for row in stored.conditions]})` when `len(stored.conditions) > 1` is true, otherwise `ConditionFactory.create(stored.conditions[0].condition_type, stored.conditions[0].config) if stored.conditions else None`. Assignment stores a value/reference; it is not an equality test.

**L0095.** The conditional expression selects the implicit AND path only when there is more than one top-level row.

**L0096.** Continue the statement starting at L93 with `ConditionFactory.create(`. Assign to `condition`: choose `ConditionFactory.create('and', {'conditions': [{'type': row.condition_type, 'config': row.config} for row in stored.conditions]})` when `len(stored.conditions) > 1` is true, otherwise `ConditionFactory.create(stored.conditions[0].condition_type, stored.conditions[0].config) if stored.conditions else None`. Assignment stores a value/reference; it is not an equality test.

**L0097.** Continue the statement starting at L93 with `stored.conditions[0].condition_type`. Assign to `condition`: choose `ConditionFactory.create('and', {'conditions': [{'type': row.condition_type, 'config': row.config} for row in stored.conditions]})` when `len(stored.conditions) > 1` is true, otherwise `ConditionFactory.create(stored.conditions[0].condition_type, stored.conditions[0].config) if stored.conditions else None`. Assignment stores a value/reference; it is not an equality test.

**L0098.** Continue the statement starting at L93 with `stored.conditions[0].config`. Assign to `condition`: choose `ConditionFactory.create('and', {'conditions': [{'type': row.condition_type, 'config': row.config} for row in stored.conditions]})` when `len(stored.conditions) > 1` is true, otherwise `ConditionFactory.create(stored.conditions[0].condition_type, stored.conditions[0].config) if stored.conditions else None`. Assignment stores a value/reference; it is not an equality test.

**L0099.** For one condition construct it directly; for no conditions use None so the engine has no gate.

**L0100.** Close the grouped expression/declaration introduced at L93; delimiters/commas complete the same statement rather than execute a separate operation.

**L0101.** Assign to `actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[ActionFactory.create(row.action_type, row.config, gmail_service=GmailService(self.session)) for row in stored.actions]`. Assignment stores a value/reference; it is not an equality test.

**L0102.** Continue the statement starting at L101 with `ActionFactory.create(`. Assign to `actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[ActionFactory.create(row.action_type, row.config, gmail_service=GmailService(self.session)) for row in stored.actions]`. Assignment stores a value/reference; it is not an equality test.

**L0103.** Continue the statement starting at L101 with `row.action_type`. Assign to `actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[ActionFactory.create(row.action_type, row.config, gmail_service=GmailService(self.session)) for row in stored.actions]`. Assignment stores a value/reference; it is not an equality test.

**L0104.** Continue the statement starting at L101 with `row.config`. Assign to `actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[ActionFactory.create(row.action_type, row.config, gmail_service=GmailService(self.session)) for row in stored.actions]`. Assignment stores a value/reference; it is not an equality test.

**L0105.** Inject a session-bound GmailService into hydrated actions; the factory uses it for email.

**L0106.** Close the grouped expression/declaration introduced at L101; delimiters/commas complete the same statement rather than execute a separate operation.

**L0107.** Continue the statement starting at L101 with `for row in stored.actions`. Assign to `actions`: construct a new list by applying the displayed expression for each item in the comprehension: `[ActionFactory.create(row.action_type, row.config, gmail_service=GmailService(self.session)) for row in stored.actions]`. Assignment stores a value/reference; it is not an equality test.

**L0108.** Close the grouped expression/declaration introduced at L101; delimiters/commas complete the same statement rather than execute a separate operation.

**L0109.** Return from this function: construct a tuple containing the displayed values: `(stored, RuntimeWorkflow(name=stored.name, trigger=trigger, condition=condition, actions=actions))`.

**L0110.** Continue the statement starting at L109 with `name=stored.name`. Return from this function: construct a tuple containing the displayed values: `(stored, RuntimeWorkflow(name=stored.name, trigger=trigger, condition=condition, actions=actions))`.

**L0111.** Continue the statement starting at L109 with `trigger=trigger`. Return from this function: construct a tuple containing the displayed values: `(stored, RuntimeWorkflow(name=stored.name, trigger=trigger, condition=condition, actions=actions))`.

**L0112.** Continue the statement starting at L109 with `condition=condition`. Return from this function: construct a tuple containing the displayed values: `(stored, RuntimeWorkflow(name=stored.name, trigger=trigger, condition=condition, actions=actions))`.

**L0113.** Continue the statement starting at L109 with `actions=actions`. Return from this function: construct a tuple containing the displayed values: `(stored, RuntimeWorkflow(name=stored.name, trigger=trigger, condition=condition, actions=actions))`.

**L0114.** Close the grouped expression/declaration introduced at L109; delimiters/commas complete the same statement rather than execute a separate operation.

**L0115.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0116.** Define function/method `run_manual(self, workflow_id: str, payload: dict)` with intended return type `Execution`.  `self` is supplied by an ordinary bound method call.

**L0117.** Return from this function: run a normalized event through hydration/engine/history persistence synchronously: `self.run_event(workflow_id, Event(type='manual', source='manual', payload=payload))`.

**L0118.** Continue the statement starting at L117 with `workflow_id`. Return from this function: run a normalized event through hydration/engine/history persistence synchronously: `self.run_event(workflow_id, Event(type='manual', source='manual', payload=payload))`.

**L0119.** Normalize a manual request into a manual envelope; source strings inside payload remain separate data.

**L0120.** Close the grouped expression/declaration introduced at L117; delimiters/commas complete the same statement rather than execute a separate operation.

**L0121.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0122.** Define function/method `run_event(self, workflow_id: str, event: Event)` with intended return type `Execution`.  `self` is supplied by an ordinary bound method call.

**L0123.** Hydrate before checking enabled, so invalid configuration can fail before the disabled-policy check.

**L0124.** Enter the following indented branch only if you negate the truth value of `stored.enabled`.

**L0125.** Raise for a disabled workflow rather than creating a SKIPPED execution row.

**L0126.** Invoke the engine synchronously and bind owner identity from stored data, not an untrusted run-payload owner.

**L0127.** Assign to `execution`: construct a persisted execution ORM object, not commit it yet: `Execution(workflow_id=stored.id, status=result.status.value, started_at=datetime.now(timezone.utc), completed_at=datetime.now(timezone.utc), trigger_data=event.payload, result={'action_count': result.action_count}, error=result.error)`. Assignment stores a value/reference; it is not an equality test.

**L0128.** Continue the statement starting at L127 with `workflow_id=stored.id`. Assign to `execution`: construct a persisted execution ORM object, not commit it yet: `Execution(workflow_id=stored.id, status=result.status.value, started_at=datetime.now(timezone.utc), completed_at=datetime.now(timezone.utc), trigger_data=event.payload, result={'action_count': result.action_count}, error=result.error)`. Assignment stores a value/reference; it is not an equality test.

**L0129.** Continue the statement starting at L127 with `status=result.status.value`. Assign to `execution`: construct a persisted execution ORM object, not commit it yet: `Execution(workflow_id=stored.id, status=result.status.value, started_at=datetime.now(timezone.utc), completed_at=datetime.now(timezone.utc), trigger_data=event.payload, result={'action_count': result.action_count}, error=result.error)`. Assignment stores a value/reference; it is not an equality test.

**L0130.** Assign start time after the engine already returned; currently not a true measured start timestamp.

**L0131.** Assign completion time immediately afterward; subtracting these timestamps misses action duration.

**L0132.** Persist raw event payload without a general redaction filter.

**L0133.** Persist only action_count; action_results appended by concrete actions are not included in this stored result.

**L0134.** Persist the engine error string; custom actions must avoid sensitive exceptions.

**L0135.** Close the grouped expression/declaration introduced at L127; delimiters/commas complete the same statement rather than execute a separate operation.

**L0136.** Perform the expression for its effect: stage an ORM object for persistence in this service's session: `self.session.add(execution)`.

**L0137.** Perform the expression for its effect: flush pending SQL without a final commit: `self.session.flush()`.

**L0138.** Return from this function: read/evaluate `execution`.


<a id="backend-tests-conftestpy"></a>
## backend/tests/conftest.py

Shared test fixtures use in-memory SQLite and temporarily disable configured auth/select Resend. TestClient drives the ASGI app. Dependency overrides in individual API tests supply the test database/user. Tests exercise mocked providers, not live delivery.

Source fingerprint: `9f4f4d69f8a86013f4d6b92fa9446c79ea37aa7f066e496162aebf5271d8b54c`. Physical lines: 41.

### Numbered source

```python
0001 | import os
0002 | 
0003 | os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
0004 | 
0005 | import pytest
0006 | from fastapi.testclient import TestClient
0007 | from sqlalchemy import create_engine
0008 | from sqlalchemy.orm import Session, sessionmaker
0009 | 
0010 | from app.main import app
0011 | from app.models import Base
0012 | from app.config import settings
0013 | 
0014 | 
0015 | @pytest.fixture(autouse=True)
0016 | def local_test_settings(monkeypatch):
0017 |     monkeypatch.setattr(settings, "supabase_url", "")
0018 |     monkeypatch.setattr(settings, "email_provider", "resend")
0019 | 
0020 | 
0021 | @pytest.fixture
0022 | def client() -> TestClient:
0023 |     with TestClient(app) as test_client:
0024 |         yield test_client
0025 | 
0026 | 
0027 | @pytest.fixture
0028 | def db_session() -> Session:
0029 |     engine = create_engine(
0030 |         "sqlite:///:memory:",
0031 |         connect_args={"check_same_thread": False},
0032 |     )
0033 |     Base.metadata.create_all(bind=engine)
0034 |     SessionLocal = sessionmaker(bind=engine)
0035 |     session = SessionLocal()
0036 |     try:
0037 |         yield session
0038 |         session.commit()
0039 |     finally:
0040 |         session.close()
0041 |         Base.metadata.drop_all(bind=engine)
```

### Every-line explanation

**L0001.** Import module(s) `os`. Top-level module code runs on first import.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Perform the expression for its effect: get an existing dictionary entry or insert and return its default: `os.environ.setdefault('DATABASE_URL', 'sqlite:///:memory:')`.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import module(s) `pytest`. Top-level module code runs on first import.

**L0006.** Import TestClient from `fastapi.testclient`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import create_engine from `sqlalchemy`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Import Session, sessionmaker from `sqlalchemy.orm`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Import app from `app.main`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Import Base from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0012.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Apply/register the following definition with decorator `@pytest.fixture(autouse=True)`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0016.** Define function/method `local_test_settings(monkeypatch)`. 

**L0017.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'supabase_url', '')`.

**L0018.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'email_provider', 'resend')`.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Apply/register the following definition with decorator `@pytest.fixture`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0022.** Define function/method `client()` with intended return type `TestClient`. 

**L0023.** Enter context manager(s): call `TestClient` with the displayed positional/named arguments: `TestClient(app)` bound as `test_client`. Exit cleanup also runs when the body raises.

**L0024.** Yield `test_client` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0025.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0026.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0027.** Apply/register the following definition with decorator `@pytest.fixture`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0028.** Define function/method `db_session()` with intended return type `Session`. 

**L0029.** Assign to `engine`: create SQLAlchemy's database engine/connection manager: `create_engine('sqlite:///:memory:', connect_args={'check_same_thread': False})`. Assignment stores a value/reference; it is not an equality test.

**L0030.** Continue the statement starting at L29 with `"sqlite:///:memory:"`. Assign to `engine`: create SQLAlchemy's database engine/connection manager: `create_engine('sqlite:///:memory:', connect_args={'check_same_thread': False})`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Continue the statement starting at L29 with `connect_args={"check_same_thread": False}`. Assign to `engine`: create SQLAlchemy's database engine/connection manager: `create_engine('sqlite:///:memory:', connect_args={'check_same_thread': False})`. Assignment stores a value/reference; it is not an equality test.

**L0032.** Close the grouped expression/declaration introduced at L29; delimiters/commas complete the same statement rather than execute a separate operation.

**L0033.** Perform the expression for its effect: create currently missing mapped database tables (not migrate existing schemas): `Base.metadata.create_all(bind=engine)`.

**L0034.** Assign to `SessionLocal`: build a factory for database Session objects: `sessionmaker(bind=engine)`. Assignment stores a value/reference; it is not an equality test.

**L0035.** Assign to `session`: allocate a database unit-of-work session: `SessionLocal()`. Assignment stores a value/reference; it is not an equality test.

**L0036.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0037.** Yield `session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0038.** Perform the expression for its effect: commit the current database transaction: `session.commit()`.

**L0039.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0040.** Perform the expression for its effect: release the Session's resources: `session.close()`.

**L0041.** Perform the expression for its effect: drop the fixture's isolated test tables during cleanup: `Base.metadata.drop_all(bind=engine)`.


<a id="backend-tests-testauthpy"></a>
## backend/tests/test_auth.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `e08b692cfe25160d784fc85fd5e666b832c0e7e2f6566cfe1c83cc1bb002bd9d`. Physical lines: 18.

### Numbered source

```python
0001 | from unittest.mock import Mock, patch
0002 | 
0003 | from app.api.auth import current_user
0004 | 
0005 | 
0006 | @patch("app.api.auth.httpx.get")
0007 | def test_current_user_reads_supabase_identity(mock_get: Mock, monkeypatch) -> None:
0008 |     monkeypatch.setattr("app.api.auth.settings.supabase_url", "https://project.supabase.co")
0009 |     response = Mock(status_code=200)
0010 |     response.json.return_value = {"id": "user-123", "email": "user@example.com"}
0011 |     mock_get.return_value = response
0012 | 
0013 |     user = current_user("Bearer access-token")
0014 | 
0015 |     assert user is not None
0016 |     assert user.id == "user-123"
0017 |     assert user.email == "user@example.com"
0018 |     mock_get.assert_called_once()
```

### Every-line explanation

**L0001.** Import Mock, patch from `unittest.mock`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import current_user from `app.api.auth`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Apply/register the following definition with decorator `@patch("app.api.auth.httpx.get")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0007.** Define function/method `test_current_user_reads_supabase_identity(mock_get: Mock, monkeypatch)` with intended return type `None`. Mock the remote user endpoint and verify identity mapping; this does not test all missing/invalid token paths.

**L0008.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr('app.api.auth.settings.supabase_url', 'https://project.supabase.co')`.

**L0009.** Assign to `response`: create a programmable test double rather than a real provider response: `Mock(status_code=200)`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Assign to `response.json.return_value`: construct a dictionary mapping the displayed keys to values: `{'id': 'user-123', 'email': 'user@example.com'}`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Assign to `mock_get.return_value`: read/evaluate `response`. Assignment stores a value/reference; it is not an equality test.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Assign to `user`: call `current_user` with the displayed positional/named arguments: `current_user('Bearer access-token')`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Test assertion: evaluate the comparison/membership/identity test `user is not None`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0016.** Test assertion: evaluate the comparison/membership/identity test `user.id == 'user-123'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0017.** Test assertion: evaluate the comparison/membership/identity test `user.email == 'user@example.com'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0018.** Perform the expression for its effect: assert this test mock was called once: `mock_get.assert_called_once()`.


<a id="backend-tests-testconfigpy"></a>
## backend/tests/test_config.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `543c1f7fa3995eeb3ce83434372773806ec8a4cbe9db98c7687652f3e6474d75`. Physical lines: 8.

### Numbered source

```python
0001 | from pathlib import Path
0002 | 
0003 | from app.config import Settings
0004 | 
0005 | 
0006 | def test_settings_load_backend_env_file_independent_of_working_directory() -> None:
0007 |     env_file = Path(__file__).resolve().parents[1] / ".env"
0008 |     assert Settings.model_config["env_file"] == env_file
```

### Every-line explanation

**L0001.** Import Path from `pathlib`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import Settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0006.** Define function/method `test_settings_load_backend_env_file_independent_of_working_directory()` with intended return type `None`. Verify that the declared dotenv path is computed from the backend location; no dotenv contents are printed.

**L0007.** Assign to `env_file`: compute `Path(__file__).resolve().parents[1] / '.env'` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0008.** Test assertion: evaluate the comparison/membership/identity test `Settings.model_config['env_file'] == env_file`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.


<a id="backend-tests-testenginepy"></a>
## backend/tests/test_engine.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `48014a9da77d6b356ef7357de73f415f8935214864d8f7ba2dbcfd385a3b3134`. Physical lines: 85.

### Numbered source

```python
0001 | from app.core.conditions import AndCondition, ContainsCondition, EqualsCondition, OrCondition
0002 | from app.core.engine import ExecutionStatus, WorkflowEngine
0003 | from app.core.event import Event, ExecutionContext
0004 | from app.core.factories import ActionFactory, ConditionFactory, TriggerFactory
0005 | from app.core.workflow import Workflow
0006 | 
0007 | 
0008 | def test_factories_hydrate_nested_conditions_and_triggers() -> None:
0009 |     condition = ConditionFactory.create(
0010 |         "and",
0011 |         {
0012 |             "conditions": [
0013 |                 {"type": "equals", "config": {"field": "repo", "value": "FlowForge"}},
0014 |                 {"type": "contains", "config": {"field": "labels", "value": "bug"}},
0015 |             ]
0016 |         },
0017 |     )
0018 |     assert isinstance(condition, AndCondition)
0019 |     assert condition.evaluate(
0020 |         ExecutionContext(
0021 |             event=Event(type="manual", source="manual"),
0022 |             data={"repo": "FlowForge", "labels": ["bug"]},
0023 |         )
0024 |     )
0025 |     assert isinstance(TriggerFactory.create("webhook", {"source": "github"}), object)
0026 |     assert isinstance(ActionFactory.create("noop"), object)
0027 | 
0028 | 
0029 | def test_comparison_and_or_conditions() -> None:
0030 |     context = ExecutionContext(
0031 |         event=Event(type="manual", source="manual"),
0032 |         data={"count": 3, "status": "open"},
0033 |     )
0034 |     assert ConditionFactory.create("greater_than", {"field": "count", "value": 2}).evaluate(context)
0035 |     assert ConditionFactory.create("less_than", {"field": "count", "value": 4}).evaluate(context)
0036 |     assert ConditionFactory.create("not_equals", {"field": "status", "value": "closed"}).evaluate(context)
0037 |     assert OrCondition([EqualsCondition("status", "closed"), EqualsCondition("count", 3)]).evaluate(context)
0038 | 
0039 | 
0040 | def test_engine_skips_before_actions_when_trigger_or_condition_fails() -> None:
0041 |     action = ActionFactory.create("noop")
0042 |     workflow = Workflow(
0043 |         name="manual",
0044 |         trigger=TriggerFactory.create("manual"),
0045 |         condition=ConditionFactory.create("equals", {"field": "repo", "value": "FlowForge"}),
0046 |         actions=[action],
0047 |     )
0048 | 
0049 |     trigger_result = WorkflowEngine().execute(
0050 |         workflow,
0051 |         Event(type="webhook", source="github", payload={"repo": "FlowForge"}),
0052 |     )
0053 |     condition_result = WorkflowEngine().execute(
0054 |         workflow,
0055 |         Event(type="manual", source="manual", payload={"repo": "other"}),
0056 |     )
0057 | 
0058 |     assert trigger_result.status is ExecutionStatus.SKIPPED
0059 |     assert condition_result.status is ExecutionStatus.SKIPPED
0060 |     assert action.calls == []
0061 | 
0062 | 
0063 | def test_engine_executes_actions_in_order() -> None:
0064 |     first = ActionFactory.create("noop")
0065 |     second = ActionFactory.create("noop")
0066 |     workflow = Workflow("manual", TriggerFactory.create("manual"), None, [first, second])
0067 | 
0068 |     result = WorkflowEngine().execute(workflow, Event(type="manual", source="manual"))
0069 | 
0070 |     assert result.status is ExecutionStatus.SUCCESS
0071 |     assert result.action_count == 2
0072 |     assert len(first.calls) == 1
0073 |     assert len(second.calls) == 1
0074 | 
0075 | 
0076 | def test_engine_preserves_safe_action_error() -> None:
0077 |     class FailingAction:
0078 |         def execute(self, _context: ExecutionContext) -> None:
0079 |             raise RuntimeError("GitHub action returned status 403")
0080 | 
0081 |     workflow = Workflow("manual", TriggerFactory.create("manual"), None, [FailingAction()])
0082 |     result = WorkflowEngine().execute(workflow, Event(type="manual", source="manual"))
0083 | 
0084 |     assert result.status is ExecutionStatus.FAILED
0085 |     assert result.error == "GitHub action returned status 403"
```

### Every-line explanation

**L0001.** Import AndCondition, ContainsCondition, EqualsCondition, OrCondition from `app.core.conditions`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import ExecutionStatus, WorkflowEngine from `app.core.engine`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import Event, ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import ActionFactory, ConditionFactory, TriggerFactory from `app.core.factories`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import Workflow from `app.core.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Define function/method `test_factories_hydrate_nested_conditions_and_triggers()` with intended return type `None`. Verify nested condition factory/evaluation. The object-type checks for trigger/action are weak because almost everything is an object.

**L0009.** Assign to `condition`: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create('and', {'conditions': [{'type': 'equals', 'config': {'field': 'repo', 'value': 'FlowForge'}}, {'type': 'contains', 'config': {'field': 'labels', 'value': 'bug'}}]})`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Continue the statement starting at L9 with `"and"`. Assign to `condition`: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create('and', {'conditions': [{'type': 'equals', 'config': {'field': 'repo', 'value': 'FlowForge'}}, {'type': 'contains', 'config': {'field': 'labels', 'value': 'bug'}}]})`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Continue the statement starting at L9 with `{`. Assign to `condition`: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create('and', {'conditions': [{'type': 'equals', 'config': {'field': 'repo', 'value': 'FlowForge'}}, {'type': 'contains', 'config': {'field': 'labels', 'value': 'bug'}}]})`. Assignment stores a value/reference; it is not an equality test.

**L0012.** Continue the statement starting at L9 with `"conditions": [`. Assign to `condition`: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create('and', {'conditions': [{'type': 'equals', 'config': {'field': 'repo', 'value': 'FlowForge'}}, {'type': 'contains', 'config': {'field': 'labels', 'value': 'bug'}}]})`. Assignment stores a value/reference; it is not an equality test.

**L0013.** Continue the statement starting at L9 with `{"type": "equals", "config": {"field": "repo", "value": "FlowForge"}}`. Assign to `condition`: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create('and', {'conditions': [{'type': 'equals', 'config': {'field': 'repo', 'value': 'FlowForge'}}, {'type': 'contains', 'config': {'field': 'labels', 'value': 'bug'}}]})`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Continue the statement starting at L9 with `{"type": "contains", "config": {"field": "labels", "value": "bug"}}`. Assign to `condition`: construct a component through a factory, or call a service create use case as identified by receiver: `ConditionFactory.create('and', {'conditions': [{'type': 'equals', 'config': {'field': 'repo', 'value': 'FlowForge'}}, {'type': 'contains', 'config': {'field': 'labels', 'value': 'bug'}}]})`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Close the grouped expression/declaration introduced at L9; delimiters/commas complete the same statement rather than execute a separate operation.

**L0016.** Close the grouped expression/declaration introduced at L9; delimiters/commas complete the same statement rather than execute a separate operation.

**L0017.** Close the grouped expression/declaration introduced at L9; delimiters/commas complete the same statement rather than execute a separate operation.

**L0018.** Test assertion: perform an actual runtime type check: `isinstance(condition, AndCondition)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0019.** Test assertion: invoke the selected Condition's boolean behavior polymorphically: `condition.evaluate(ExecutionContext(event=Event(type='manual', source='manual'), data={'repo': 'FlowForge', 'labels': ['bug']}))`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0020.** Continue the statement starting at L19 with `ExecutionContext(`. Test assertion: invoke the selected Condition's boolean behavior polymorphically: `condition.evaluate(ExecutionContext(event=Event(type='manual', source='manual'), data={'repo': 'FlowForge', 'labels': ['bug']}))`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0021.** Continue the statement starting at L19 with `event=Event(type="manual", source="manual")`. Test assertion: invoke the selected Condition's boolean behavior polymorphically: `condition.evaluate(ExecutionContext(event=Event(type='manual', source='manual'), data={'repo': 'FlowForge', 'labels': ['bug']}))`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0022.** Continue the statement starting at L19 with `data={"repo": "FlowForge", "labels": ["bug"]}`. Test assertion: invoke the selected Condition's boolean behavior polymorphically: `condition.evaluate(ExecutionContext(event=Event(type='manual', source='manual'), data={'repo': 'FlowForge', 'labels': ['bug']}))`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0023.** Close the grouped expression/declaration introduced at L19; delimiters/commas complete the same statement rather than execute a separate operation.

**L0024.** Close the grouped expression/declaration introduced at L19; delimiters/commas complete the same statement rather than execute a separate operation.

**L0025.** Test assertion: perform an actual runtime type check: `isinstance(TriggerFactory.create('webhook', {'source': 'github'}), object)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0026.** Test assertion: perform an actual runtime type check: `isinstance(ActionFactory.create('noop'), object)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0027.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0028.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0029.** Define function/method `test_comparison_and_or_conditions()` with intended return type `None`. Verify greater/less/not-equal and an OR result using deterministic context data.

**L0030.** Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'count': 3, 'status': 'open'})`. Assignment stores a value/reference; it is not an equality test.

**L0031.** Continue the statement starting at L30 with `event=Event(type="manual", source="manual")`. Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'count': 3, 'status': 'open'})`. Assignment stores a value/reference; it is not an equality test.

**L0032.** Continue the statement starting at L30 with `data={"count": 3, "status": "open"}`. Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'count': 3, 'status': 'open'})`. Assignment stores a value/reference; it is not an equality test.

**L0033.** Close the grouped expression/declaration introduced at L30; delimiters/commas complete the same statement rather than execute a separate operation.

**L0034.** Test assertion: invoke the selected Condition's boolean behavior polymorphically: `ConditionFactory.create('greater_than', {'field': 'count', 'value': 2}).evaluate(context)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0035.** Test assertion: invoke the selected Condition's boolean behavior polymorphically: `ConditionFactory.create('less_than', {'field': 'count', 'value': 4}).evaluate(context)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0036.** Test assertion: invoke the selected Condition's boolean behavior polymorphically: `ConditionFactory.create('not_equals', {'field': 'status', 'value': 'closed'}).evaluate(context)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0037.** Test assertion: invoke the selected Condition's boolean behavior polymorphically: `OrCondition([EqualsCondition('status', 'closed'), EqualsCondition('count', 3)]).evaluate(context)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0038.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0039.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0040.** Define function/method `test_engine_skips_before_actions_when_trigger_or_condition_fails()` with intended return type `None`. Verify both gating failures produce SKIPPED and never call the action.

**L0041.** Assign to `action`: construct a component through a factory, or call a service create use case as identified by receiver: `ActionFactory.create('noop')`. Assignment stores a value/reference; it is not an equality test.

**L0042.** Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='manual', trigger=TriggerFactory.create('manual'), condition=ConditionFactory.create('equals', {'field': 'repo', 'value': 'FlowForge'}), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Continue the statement starting at L42 with `name="manual"`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='manual', trigger=TriggerFactory.create('manual'), condition=ConditionFactory.create('equals', {'field': 'repo', 'value': 'FlowForge'}), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0044.** Continue the statement starting at L42 with `trigger=TriggerFactory.create("manual")`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='manual', trigger=TriggerFactory.create('manual'), condition=ConditionFactory.create('equals', {'field': 'repo', 'value': 'FlowForge'}), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0045.** Continue the statement starting at L42 with `condition=ConditionFactory.create("equals", {"field": "repo", "value": "FlowForge"})`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='manual', trigger=TriggerFactory.create('manual'), condition=ConditionFactory.create('equals', {'field': 'repo', 'value': 'FlowForge'}), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0046.** Continue the statement starting at L42 with `actions=[action]`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='manual', trigger=TriggerFactory.create('manual'), condition=ConditionFactory.create('equals', {'field': 'repo', 'value': 'FlowForge'}), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0047.** Close the grouped expression/declaration introduced at L42; delimiters/commas complete the same statement rather than execute a separate operation.

**L0048.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0049.** Assign to `trigger_result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='webhook', source='github', payload={'repo': 'FlowForge'}))`. Assignment stores a value/reference; it is not an equality test.

**L0050.** Continue the statement starting at L49 with `workflow`. Assign to `trigger_result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='webhook', source='github', payload={'repo': 'FlowForge'}))`. Assignment stores a value/reference; it is not an equality test.

**L0051.** Continue the statement starting at L49 with `Event(type="webhook", source="github", payload={"repo": "FlowForge"})`. Assign to `trigger_result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='webhook', source='github', payload={'repo': 'FlowForge'}))`. Assignment stores a value/reference; it is not an equality test.

**L0052.** Close the grouped expression/declaration introduced at L49; delimiters/commas complete the same statement rather than execute a separate operation.

**L0053.** Assign to `condition_result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='manual', source='manual', payload={'repo': 'other'}))`. Assignment stores a value/reference; it is not an equality test.

**L0054.** Continue the statement starting at L53 with `workflow`. Assign to `condition_result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='manual', source='manual', payload={'repo': 'other'}))`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Continue the statement starting at L53 with `Event(type="manual", source="manual", payload={"repo": "other"})`. Assign to `condition_result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='manual', source='manual', payload={'repo': 'other'}))`. Assignment stores a value/reference; it is not an equality test.

**L0056.** Close the grouped expression/declaration introduced at L53; delimiters/commas complete the same statement rather than execute a separate operation.

**L0057.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0058.** Test assertion: evaluate the comparison/membership/identity test `trigger_result.status is ExecutionStatus.SKIPPED`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0059.** Test assertion: evaluate the comparison/membership/identity test `condition_result.status is ExecutionStatus.SKIPPED`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0060.** Test assertion: evaluate the comparison/membership/identity test `action.calls == []`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0061.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0062.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0063.** Define function/method `test_engine_executes_actions_in_order()` with intended return type `None`. Check two actions ran once and count is two. The assertions do not independently record exact interleaving order.

**L0064.** Assign to `first`: construct a component through a factory, or call a service create use case as identified by receiver: `ActionFactory.create('noop')`. Assignment stores a value/reference; it is not an equality test.

**L0065.** Assign to `second`: construct a component through a factory, or call a service create use case as identified by receiver: `ActionFactory.create('noop')`. Assignment stores a value/reference; it is not an equality test.

**L0066.** Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow('manual', TriggerFactory.create('manual'), None, [first, second])`. Assignment stores a value/reference; it is not an equality test.

**L0067.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0068.** Assign to `result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='manual', source='manual'))`. Assignment stores a value/reference; it is not an equality test.

**L0069.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0070.** Test assertion: evaluate the comparison/membership/identity test `result.status is ExecutionStatus.SUCCESS`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0071.** Test assertion: evaluate the comparison/membership/identity test `result.action_count == 2`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0072.** Test assertion: evaluate the comparison/membership/identity test `len(first.calls) == 1`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0073.** Test assertion: evaluate the comparison/membership/identity test `len(second.calls) == 1`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0074.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0075.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0076.** Define function/method `test_engine_preserves_safe_action_error()` with intended return type `None`. Supply a failing duck-typed action and verify FAILED preserves the deliberately safe example error.

**L0077.** Define class `FailingAction`. The indented suite defines its attributes/methods; defining a class does not instantiate it.

**L0078.** Define function/method `execute(self, _context: ExecutionContext)` with intended return type `None`.  `self` is supplied by an ordinary bound method call.

**L0079.** Raise construct an execution/integration failure exception: `RuntimeError('GitHub action returned status 403')`. Normal execution at this point stops.

**L0080.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0081.** Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow('manual', TriggerFactory.create('manual'), None, [FailingAction()])`. Assignment stores a value/reference; it is not an equality test.

**L0082.** Assign to `result`: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `WorkflowEngine().execute(workflow, Event(type='manual', source='manual'))`. Assignment stores a value/reference; it is not an equality test.

**L0083.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0084.** Test assertion: evaluate the comparison/membership/identity test `result.status is ExecutionStatus.FAILED`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0085.** Test assertion: evaluate the comparison/membership/identity test `result.error == 'GitHub action returned status 403'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.


<a id="backend-tests-testgmailpy"></a>
## backend/tests/test_gmail.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `7b5e6feda0989fe597285bb8392f9e7cd05e1279131aca4f4369e31913f2bb93`. Physical lines: 102.

### Numbered source

```python
0001 | from datetime import datetime, timedelta, timezone
0002 | from urllib.parse import parse_qs, urlparse
0003 | from unittest.mock import Mock, patch
0004 | 
0005 | from cryptography.fernet import Fernet
0006 | 
0007 | from app.config import settings
0008 | from app.api.auth import AuthenticatedUser, current_user
0009 | from app.core.event import Event, ExecutionContext
0010 | from app.core.actions.email import EmailAction
0011 | from app.db import get_session
0012 | from app.main import app
0013 | from app.models import GmailConnection, User
0014 | from app.services.gmail import GmailService
0015 | 
0016 | 
0017 | def test_gmail_action_sends_message_without_exposing_token(db_session, monkeypatch) -> None:
0018 |     key = Fernet.generate_key().decode()
0019 |     monkeypatch.setattr(settings, "token_encryption_key", key)
0020 |     monkeypatch.setattr(settings, "email_provider", "gmail")
0021 |     user = User(email="gmail@example.com")
0022 |     db_session.add(user)
0023 |     db_session.flush()
0024 |     GmailService(db_session).save_connection(
0025 |         user.id,
0026 |         "sender@gmail.com",
0027 |         "access-token",
0028 |         "refresh-token",
0029 |         datetime.now(timezone.utc) + timedelta(hours=1),
0030 |     )
0031 |     response = Mock(status_code=200)
0032 |     response.json.return_value = {"id": "gmail-message-1"}
0033 | 
0034 |     with patch("app.services.gmail.httpx.post", return_value=response) as request:
0035 |         context = ExecutionContext(Event(type="manual", source="test"), user_id=user.id)
0036 |         EmailAction(
0037 |             {"to": ["recipient@example.com"], "subject": "Test", "text": "Body"},
0038 |             gmail_service=GmailService(db_session),
0039 |         ).execute(context)
0040 | 
0041 |     assert context.data["action_results"] == [
0042 |         {"type": "email", "provider": "gmail", "status": "sent", "provider_id": "gmail-message-1"}
0043 |     ]
0044 |     assert request.call_args.kwargs["headers"]["Authorization"] == "Bearer access-token"
0045 |     assert "refresh-token" not in str(context.data)
0046 |     assert "access-token" not in str(context.data)
0047 | 
0048 | 
0049 | def test_gmail_service_rejects_missing_connection(db_session, monkeypatch) -> None:
0050 |     monkeypatch.setattr(settings, "token_encryption_key", Fernet.generate_key().decode())
0051 |     service = GmailService(db_session)
0052 | 
0053 |     try:
0054 |         service.send("missing-user", ["recipient@example.com"], "Test", "Body", None)
0055 |     except RuntimeError as exc:
0056 |         assert str(exc) == "Connect Gmail before using the email action"
0057 |     else:
0058 |         raise AssertionError("Expected missing Gmail connection to fail")
0059 | 
0060 | 
0061 | def test_gmail_connect_and_callback_store_user_connection(client, db_session, monkeypatch) -> None:
0062 |     user = User(id="supabase-user", email="user@example.com")
0063 |     db_session.add(user)
0064 |     db_session.commit()
0065 |     authenticated = AuthenticatedUser(id=user.id, email=user.email)
0066 |     def override_session():
0067 |         yield db_session
0068 | 
0069 |     app.dependency_overrides[get_session] = override_session
0070 |     app.dependency_overrides[current_user] = lambda: authenticated
0071 |     monkeypatch.setattr(settings, "google_client_id", "client-id")
0072 |     monkeypatch.setattr(settings, "google_client_secret", "client-secret")
0073 |     monkeypatch.setattr(settings, "token_encryption_key", Fernet.generate_key().decode())
0074 |     try:
0075 |         connect = client.get("/api/integrations/gmail/connect")
0076 |         assert connect.status_code == 200
0077 |         authorization_url = connect.json()["authorization_url"]
0078 |         assert "state=" in authorization_url
0079 |         query = parse_qs(urlparse(authorization_url).query)
0080 |         assert query["scope"][0] == "openid email https://www.googleapis.com/auth/gmail.send"
0081 |         state = query["state"][0]
0082 | 
0083 |         monkeypatch.setattr(
0084 |             GmailService,
0085 |             "exchange_code",
0086 |             lambda _service, _code: (
0087 |                 "access-token",
0088 |                 "refresh-token",
0089 |                 datetime.now(timezone.utc) + timedelta(hours=1),
0090 |             ),
0091 |         )
0092 |         monkeypatch.setattr(GmailService, "profile", lambda _service, _token: "user@gmail.com")
0093 |         callback = client.get(
0094 |             f"/api/integrations/gmail/callback?code=oauth-code&state={state}",
0095 |             follow_redirects=False,
0096 |         )
0097 | 
0098 |         assert callback.status_code == 302
0099 |         assert "gmail=connected" in callback.headers["location"]
0100 |         assert GmailService(db_session).connection(user.id).email == "user@gmail.com"
0101 |     finally:
0102 |         app.dependency_overrides.clear()
```

### Every-line explanation

**L0001.** Import datetime, timedelta, timezone from `datetime`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import parse_qs, urlparse from `urllib.parse`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import Mock, patch from `unittest.mock`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import Fernet from `cryptography.fernet`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Import settings from `app.config`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Import AuthenticatedUser, current_user from `app.api.auth`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Import Event, ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0010.** Import EmailAction from `app.core.actions.email`. Imported names become available in this module; aliases distinguish roles where used.

**L0011.** Import get_session from `app.db`. Imported names become available in this module; aliases distinguish roles where used.

**L0012.** Import app from `app.main`. Imported names become available in this module; aliases distinguish roles where used.

**L0013.** Import GmailConnection, User from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0014.** Import GmailService from `app.services.gmail`. Imported names become available in this module; aliases distinguish roles where used.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Define function/method `test_gmail_action_sends_message_without_exposing_token(db_session, monkeypatch)` with intended return type `None`. Store encrypted fake tokens, mock the Gmail network call, verify safe metadata and no token in context data.

**L0018.** Assign to `key`: convert bytes into text using the default UTF-8 encoding: `Fernet.generate_key().decode()`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'token_encryption_key', key)`.

**L0020.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'email_provider', 'gmail')`.

**L0021.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='gmail@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0022.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0023.** Perform the expression for its effect: flush the test transaction so IDs/config are available: `db_session.flush()`.

**L0024.** Perform the expression for its effect: encrypt and store this user's Gmail tokens: `GmailService(db_session).save_connection(user.id, 'sender@gmail.com', 'access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1))`.

**L0025.** Continue the statement starting at L24 with `user.id`. Perform the expression for its effect: encrypt and store this user's Gmail tokens: `GmailService(db_session).save_connection(user.id, 'sender@gmail.com', 'access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1))`.

**L0026.** Continue the statement starting at L24 with `"sender@gmail.com"`. Perform the expression for its effect: encrypt and store this user's Gmail tokens: `GmailService(db_session).save_connection(user.id, 'sender@gmail.com', 'access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1))`.

**L0027.** Continue the statement starting at L24 with `"access-token"`. Perform the expression for its effect: encrypt and store this user's Gmail tokens: `GmailService(db_session).save_connection(user.id, 'sender@gmail.com', 'access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1))`.

**L0028.** Continue the statement starting at L24 with `"refresh-token"`. Perform the expression for its effect: encrypt and store this user's Gmail tokens: `GmailService(db_session).save_connection(user.id, 'sender@gmail.com', 'access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1))`.

**L0029.** Continue the statement starting at L24 with `datetime.now(timezone.utc) + timedelta(hours=1)`. Perform the expression for its effect: encrypt and store this user's Gmail tokens: `GmailService(db_session).save_connection(user.id, 'sender@gmail.com', 'access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1))`.

**L0030.** Close the grouped expression/declaration introduced at L24; delimiters/commas complete the same statement rather than execute a separate operation.

**L0031.** Assign to `response`: create a programmable test double rather than a real provider response: `Mock(status_code=200)`. Assignment stores a value/reference; it is not an equality test.

**L0032.** Assign to `response.json.return_value`: construct a dictionary mapping the displayed keys to values: `{'id': 'gmail-message-1'}`. Assignment stores a value/reference; it is not an equality test.

**L0033.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0034.** Enter context manager(s): temporarily replace the name used by code under test: `patch('app.services.gmail.httpx.post', return_value=response)` bound as `request`. Exit cleanup also runs when the body raises.

**L0035.** Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(Event(type='manual', source='test'), user_id=user.id)`. Assignment stores a value/reference; it is not an equality test.

**L0036.** Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'Test', 'text': 'Body'}, gmail_service=GmailService(db_session)).execute(context)`.

**L0037.** Continue the statement starting at L36 with `{"to": ["recipient@example.com"], "subject": "Test", "text": "Body"}`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'Test', 'text': 'Body'}, gmail_service=GmailService(db_session)).execute(context)`.

**L0038.** Continue the statement starting at L36 with `gmail_service=GmailService(db_session)`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'Test', 'text': 'Body'}, gmail_service=GmailService(db_session)).execute(context)`.

**L0039.** Continue the statement starting at L36 with `).execute(context)`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'Test', 'text': 'Body'}, gmail_service=GmailService(db_session)).execute(context)`.

**L0040.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0041.** Test assertion: evaluate the comparison/membership/identity test `context.data['action_results'] == [{'type': 'email', 'provider': 'gmail', 'status': 'sent', 'provider_id': 'gmail-message-1'}]`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0042.** Continue the statement starting at L41 with `{"type": "email", "provider": "gmail", "status": "sent", "provider_id": "gmail-message-1"}`. Test assertion: evaluate the comparison/membership/identity test `context.data['action_results'] == [{'type': 'email', 'provider': 'gmail', 'status': 'sent', 'provider_id': 'gmail-message-1'}]`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0043.** Close the grouped expression/declaration introduced at L41; delimiters/commas complete the same statement rather than execute a separate operation.

**L0044.** Test assertion: evaluate the comparison/membership/identity test `request.call_args.kwargs['headers']['Authorization'] == 'Bearer access-token'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0045.** Test assertion: evaluate the comparison/membership/identity test `'refresh-token' not in str(context.data)`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0046.** Test assertion: evaluate the comparison/membership/identity test `'access-token' not in str(context.data)`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0047.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0048.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0049.** Define function/method `test_gmail_service_rejects_missing_connection(db_session, monkeypatch)` with intended return type `None`. Verify an unconnected user cannot send through Gmail.

**L0050.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'token_encryption_key', Fernet.generate_key().decode())`.

**L0051.** Assign to `service`: construct a session-bound Gmail integration service: `GmailService(db_session)`. Assignment stores a value/reference; it is not an equality test.

**L0052.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0053.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0054.** Perform the expression for its effect: invoke the receiver's delivery/send operation: `service.send('missing-user', ['recipient@example.com'], 'Test', 'Body', None)`.

**L0055.** Catch `RuntimeError` as `exc`; execute this error branch instead of continuing the failed statement.

**L0056.** Test assertion: evaluate the comparison/membership/identity test `str(exc) == 'Connect Gmail before using the email action'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0057.** Alternative branch when the preceding if condition is false, or the try completed without its expected exception (inspect the enclosing block).

**L0058.** Raise call `AssertionError` with the displayed positional/named arguments: `AssertionError('Expected missing Gmail connection to fail')`. Normal execution at this point stops.

**L0059.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0060.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0061.** Define function/method `test_gmail_connect_and_callback_store_user_connection(client, db_session, monkeypatch)` with intended return type `None`. Override session/identity and token exchange/profile to exercise OAuth connect/callback persistence without Google.

**L0062.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(id='supabase-user', email='user@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0063.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0064.** Perform the expression for its effect: commit fixture setup within the isolated test database: `db_session.commit()`.

**L0065.** Assign to `authenticated`: construct the immutable verified identity data object: `AuthenticatedUser(id=user.id, email=user.email)`. Assignment stores a value/reference; it is not an equality test.

**L0066.** Define function/method `override_session()`. 

**L0067.** Yield `db_session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0068.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0069.** Assign to `app.dependency_overrides[get_session]`: read/evaluate `override_session`. Assignment stores a value/reference; it is not an equality test.

**L0070.** Assign to `app.dependency_overrides[current_user]`: define a deferred anonymous function `lambda: authenticated`; its body runs when called. Assignment stores a value/reference; it is not an equality test.

**L0071.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'google_client_id', 'client-id')`.

**L0072.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'google_client_secret', 'client-secret')`.

**L0073.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(settings, 'token_encryption_key', Fernet.generate_key().decode())`.

**L0074.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0075.** Assign to `connect`: issue GET through this client (an in-process app request in API tests): `client.get('/api/integrations/gmail/connect')`. Assignment stores a value/reference; it is not an equality test.

**L0076.** Test assertion: evaluate the comparison/membership/identity test `connect.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0077.** Assign to `authorization_url`: look up/index `connect.json()` using `'authorization_url'`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0078.** Test assertion: evaluate the comparison/membership/identity test `'state=' in authorization_url`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0079.** Assign to `query`: call `parse_qs` with the displayed positional/named arguments: `parse_qs(urlparse(authorization_url).query)`. Assignment stores a value/reference; it is not an equality test.

**L0080.** Test assertion: evaluate the comparison/membership/identity test `query['scope'][0] == 'openid email https://www.googleapis.com/auth/gmail.send'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0081.** Assign to `state`: look up/index `query['state']` using `0`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0082.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0083.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0084.** Continue the statement starting at L83 with `GmailService`. Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0085.** Continue the statement starting at L83 with `"exchange_code"`. Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0086.** Continue the statement starting at L83 with `lambda _service, _code: (`. Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0087.** Continue the statement starting at L83 with `"access-token"`. Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0088.** Continue the statement starting at L83 with `"refresh-token"`. Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0089.** Continue the statement starting at L83 with `datetime.now(timezone.utc) + timedelta(hours=1)`. Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'exchange_code', lambda _service, _code: ('access-token', 'refresh-token', datetime.now(timezone.utc) + timedelta(hours=1)))`.

**L0090.** Close the grouped expression/declaration introduced at L83; delimiters/commas complete the same statement rather than execute a separate operation.

**L0091.** Close the grouped expression/declaration introduced at L83; delimiters/commas complete the same statement rather than execute a separate operation.

**L0092.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr(GmailService, 'profile', lambda _service, _token: 'user@gmail.com')`.

**L0093.** Assign to `callback`: issue GET through this client (an in-process app request in API tests): `client.get(f'/api/integrations/gmail/callback?code=oauth-code&state={state}', follow_redirects=False)`. Assignment stores a value/reference; it is not an equality test.

**L0094.** Continue the statement starting at L93 with `f"/api/integrations/gmail/callback?code=oauth-code&state={state}"`. Assign to `callback`: issue GET through this client (an in-process app request in API tests): `client.get(f'/api/integrations/gmail/callback?code=oauth-code&state={state}', follow_redirects=False)`. Assignment stores a value/reference; it is not an equality test.

**L0095.** Continue the statement starting at L93 with `follow_redirects=False`. Assign to `callback`: issue GET through this client (an in-process app request in API tests): `client.get(f'/api/integrations/gmail/callback?code=oauth-code&state={state}', follow_redirects=False)`. Assignment stores a value/reference; it is not an equality test.

**L0096.** Close the grouped expression/declaration introduced at L93; delimiters/commas complete the same statement rather than execute a separate operation.

**L0097.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0098.** Test assertion: evaluate the comparison/membership/identity test `callback.status_code == 302`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0099.** Test assertion: evaluate the comparison/membership/identity test `'gmail=connected' in callback.headers['location']`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0100.** Test assertion: evaluate the comparison/membership/identity test `GmailService(db_session).connection(user.id).email == 'user@gmail.com'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0101.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0102.** Perform the expression for its effect: remove temporary test dependency overrides or collection entries: `app.dependency_overrides.clear()`.


<a id="backend-tests-testhealthpy"></a>
## backend/tests/test_health.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `a87835f2ea3d76451dab7f6d15d271d79204cd68de9a10555fb628f0ac3a4f25`. Physical lines: 6.

### Numbered source

```python
0001 | def test_health_ok(client) -> None:
0002 |     response = client.get("/health")
0003 |     assert response.status_code == 200
0004 |     body = response.json()
0005 |     assert body["status"] == "ok"
0006 |     assert body["service"] == "flowforge"
```

### Every-line explanation

**L0001.** Define function/method `test_health_ok(client)` with intended return type `None`. Exercise liveness response fields through TestClient, not production readiness.

**L0002.** Assign to `response`: issue GET through this client (an in-process app request in API tests): `client.get('/health')`. Assignment stores a value/reference; it is not an equality test.

**L0003.** Test assertion: evaluate the comparison/membership/identity test `response.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0004.** Assign to `body`: decode this response's JSON body, potentially raising on invalid data: `response.json()`. Assignment stores a value/reference; it is not an equality test.

**L0005.** Test assertion: evaluate the comparison/membership/identity test `body['status'] == 'ok'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0006.** Test assertion: evaluate the comparison/membership/identity test `body['service'] == 'flowforge'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.


<a id="backend-tests-testintegrationspy"></a>
## backend/tests/test_integrations.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `e48c4bd1f00bb0f7e5e900fead4a82aa206b13051acd4a4c74bbb7e85c019d9f`. Physical lines: 89.

### Numbered source

```python
0001 | from unittest.mock import MagicMock, Mock, patch
0002 | 
0003 | import pytest
0004 | 
0005 | from app.core.actions.github import GitHubAction
0006 | from app.core.actions.email import EmailAction
0007 | from app.core.actions.http import HttpAction
0008 | from app.core.event import Event, ExecutionContext
0009 | 
0010 | 
0011 | def test_http_action_rejects_private_addresses() -> None:
0012 |     with pytest.raises(ValueError, match="private or local"):
0013 |         HttpAction({"url": "http://127.0.0.1:8080/hook"})
0014 | 
0015 | 
0016 | def test_http_action_rejects_unsupported_scheme() -> None:
0017 |     with pytest.raises(ValueError, match="http or https"):
0018 |         HttpAction({"url": "file:///etc/passwd"})
0019 | 
0020 | 
0021 | @patch("app.core.actions.http.httpx.Client")
0022 | def test_http_action_records_status_without_response_body(mock_client: Mock) -> None:
0023 |     response = Mock()
0024 |     response.is_error = False
0025 |     response.status_code = 204
0026 |     mock_client.return_value.__enter__.return_value.send.return_value = response
0027 | 
0028 |     context = ExecutionContext(Event(type="manual", source="test"))
0029 |     HttpAction({"url": "https://8.8.8.8/hook", "body": {"ok": True}}).execute(context)
0030 | 
0031 |     assert context.data["action_results"] == [{"type": "http", "status_code": 204}]
0032 |     request = mock_client.return_value.__enter__.return_value.send.call_args.args[0]
0033 |     assert request.url == "https://8.8.8.8/hook"
0034 | 
0035 | 
0036 | @patch("app.core.actions.github.httpx.Client")
0037 | def test_github_action_sends_token_without_storing_it(mock_client: Mock) -> None:
0038 |     response = Mock()
0039 |     response.is_error = False
0040 |     response.status_code = 204
0041 |     mock_client.return_value.__enter__.return_value.post.return_value = response
0042 | 
0043 |     context = ExecutionContext(Event(type="manual", source="test"))
0044 |     GitHubAction(
0045 |         {"token": "secret-token", "repository": "owner/repo", "event_type": "deploy"}
0046 |     ).execute(context)
0047 | 
0048 |     assert context.data["action_results"] == [{"type": "github", "status_code": 204}]
0049 |     headers = mock_client.return_value.__enter__.return_value.post.call_args.kwargs["headers"]
0050 |     assert headers["Authorization"] == "Bearer secret-token"
0051 | 
0052 | 
0053 | def test_email_action_sends_safe_metadata(monkeypatch) -> None:
0054 |     monkeypatch.setattr("app.core.actions.email.settings.email_api_key", "test-key")
0055 |     monkeypatch.setattr("app.core.actions.email.settings.email_from", "sender@example.com")
0056 |     response = Mock(is_error=False, status_code=200)
0057 |     response.json.return_value = {"id": "email-123"}
0058 |     client = MagicMock()
0059 |     client.__enter__.return_value.send.return_value = response
0060 | 
0061 |     with patch("app.core.actions.email.httpx.Client", return_value=client):
0062 |         context = ExecutionContext(Event(type="manual", source="test"))
0063 |         EmailAction(
0064 |             {
0065 |                 "to": ["recipient@example.com"],
0066 |                 "subject": "FlowForge test",
0067 |                 "text": "The workflow ran.",
0068 |             }
0069 |         ).execute(context)
0070 | 
0071 |     assert context.data["action_results"] == [
0072 |         {"type": "email", "provider": "resend", "status_code": 200, "provider_id": "email-123"}
0073 |     ]
0074 |     request = client.__enter__.return_value.send.call_args.args[0]
0075 |     assert "test-key" in request.headers["Authorization"]
0076 |     assert "test-key" not in str(context.data)
0077 | 
0078 | 
0079 | def test_email_action_validates_recipients(monkeypatch) -> None:
0080 |     monkeypatch.setattr("app.core.actions.email.settings.email_api_key", "test-key")
0081 |     with pytest.raises(ValueError, match="valid email"):
0082 |         EmailAction(
0083 |             {
0084 |                 "from": "sender@example.com",
0085 |                 "to": ["not-an-email"],
0086 |                 "subject": "Test",
0087 |                 "text": "Body",
0088 |             }
0089 |         )
```

### Every-line explanation

**L0001.** Import MagicMock, Mock, patch from `unittest.mock`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Import module(s) `pytest`. Top-level module code runs on first import.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Import GitHubAction from `app.core.actions.github`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import EmailAction from `app.core.actions.email`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Import HttpAction from `app.core.actions.http`. Imported names become available in this module; aliases distinguish roles where used.

**L0008.** Import Event, ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0009.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0010.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0011.** Define function/method `test_http_action_rejects_private_addresses()` with intended return type `None`. Verify loopback destination rejection without making the outbound request.

**L0012.** Enter context manager(s): assert that the enclosed operation raises the expected exception: `pytest.raises(ValueError, match='private or local')`. Exit cleanup also runs when the body raises.

**L0013.** Perform the expression for its effect: call `HttpAction` with the displayed positional/named arguments: `HttpAction({'url': 'http://127.0.0.1:8080/hook'})`.

**L0014.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0015.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0016.** Define function/method `test_http_action_rejects_unsupported_scheme()` with intended return type `None`. Verify file URLs are not accepted as generic HTTP action destinations.

**L0017.** Enter context manager(s): assert that the enclosed operation raises the expected exception: `pytest.raises(ValueError, match='http or https')`. Exit cleanup also runs when the body raises.

**L0018.** Perform the expression for its effect: call `HttpAction` with the displayed positional/named arguments: `HttpAction({'url': 'file:///etc/passwd'})`.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0021.** Apply/register the following definition with decorator `@patch("app.core.actions.http.httpx.Client")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0022.** Define function/method `test_http_action_records_status_without_response_body(mock_client: Mock)` with intended return type `None`. Mock the HTTP client and verify request destination and safe status metadata.

**L0023.** Assign to `response`: create a programmable test double rather than a real provider response: `Mock()`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Assign to `response.is_error`: use literal value `False` (bool). Assignment stores a value/reference; it is not an equality test.

**L0025.** Assign to `response.status_code`: use literal value `204` (int). Assignment stores a value/reference; it is not an equality test.

**L0026.** Assign to `mock_client.return_value.__enter__.return_value.send.return_value`: read/evaluate `response`. Assignment stores a value/reference; it is not an equality test.

**L0027.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0028.** Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(Event(type='manual', source='test'))`. Assignment stores a value/reference; it is not an equality test.

**L0029.** Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `HttpAction({'url': 'https://8.8.8.8/hook', 'body': {'ok': True}}).execute(context)`.

**L0030.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0031.** Test assertion: evaluate the comparison/membership/identity test `context.data['action_results'] == [{'type': 'http', 'status_code': 204}]`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0032.** Assign to `request`: look up/index `mock_client.return_value.__enter__.return_value.send.call_args.args` using `0`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0033.** Test assertion: evaluate the comparison/membership/identity test `request.url == 'https://8.8.8.8/hook'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0034.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0035.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0036.** Apply/register the following definition with decorator `@patch("app.core.actions.github.httpx.Client")`. Router decorators bind HTTP method/path/response schema; pytest decorators register fixtures or test patches according to their name.

**L0037.** Define function/method `test_github_action_sends_token_without_storing_it(mock_client: Mock)` with intended return type `None`. Verify a fake token enters the outbound Authorization header and only safe action metadata is recorded; it does not prove config encryption.

**L0038.** Assign to `response`: create a programmable test double rather than a real provider response: `Mock()`. Assignment stores a value/reference; it is not an equality test.

**L0039.** Assign to `response.is_error`: use literal value `False` (bool). Assignment stores a value/reference; it is not an equality test.

**L0040.** Assign to `response.status_code`: use literal value `204` (int). Assignment stores a value/reference; it is not an equality test.

**L0041.** Assign to `mock_client.return_value.__enter__.return_value.post.return_value`: read/evaluate `response`. Assignment stores a value/reference; it is not an equality test.

**L0042.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0043.** Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(Event(type='manual', source='test'))`. Assignment stores a value/reference; it is not an equality test.

**L0044.** Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `GitHubAction({'token': 'secret-token', 'repository': 'owner/repo', 'event_type': 'deploy'}).execute(context)`.

**L0045.** Continue the statement starting at L44 with `{"token": "secret-token", "repository": "owner/repo", "event_type": "deploy"}`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `GitHubAction({'token': 'secret-token', 'repository': 'owner/repo', 'event_type': 'deploy'}).execute(context)`.

**L0046.** Continue the statement starting at L44 with `).execute(context)`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `GitHubAction({'token': 'secret-token', 'repository': 'owner/repo', 'event_type': 'deploy'}).execute(context)`.

**L0047.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0048.** Test assertion: evaluate the comparison/membership/identity test `context.data['action_results'] == [{'type': 'github', 'status_code': 204}]`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0049.** Assign to `headers`: look up/index `mock_client.return_value.__enter__.return_value.post.call_args.kwargs` using `'headers'`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0050.** Test assertion: evaluate the comparison/membership/identity test `headers['Authorization'] == 'Bearer secret-token'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0051.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0052.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0053.** Define function/method `test_email_action_sends_safe_metadata(monkeypatch)` with intended return type `None`. Mock Resend and verify request auth plus selected result metadata without provider secrets in context data.

**L0054.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr('app.core.actions.email.settings.email_api_key', 'test-key')`.

**L0055.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr('app.core.actions.email.settings.email_from', 'sender@example.com')`.

**L0056.** Assign to `response`: create a programmable test double rather than a real provider response: `Mock(is_error=False, status_code=200)`. Assignment stores a value/reference; it is not an equality test.

**L0057.** Assign to `response.json.return_value`: construct a dictionary mapping the displayed keys to values: `{'id': 'email-123'}`. Assignment stores a value/reference; it is not an equality test.

**L0058.** Assign to `client`: create a mock supporting magic methods such as context-manager entry: `MagicMock()`. Assignment stores a value/reference; it is not an equality test.

**L0059.** Assign to `client.__enter__.return_value.send.return_value`: read/evaluate `response`. Assignment stores a value/reference; it is not an equality test.

**L0060.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0061.** Enter context manager(s): temporarily replace the name used by code under test: `patch('app.core.actions.email.httpx.Client', return_value=client)`. Exit cleanup also runs when the body raises.

**L0062.** Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(Event(type='manual', source='test'))`. Assignment stores a value/reference; it is not an equality test.

**L0063.** Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'FlowForge test', 'text': 'The workflow ran.'}).execute(context)`.

**L0064.** Continue the statement starting at L63 with `{`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'FlowForge test', 'text': 'The workflow ran.'}).execute(context)`.

**L0065.** Continue the statement starting at L63 with `"to": ["recipient@example.com"]`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'FlowForge test', 'text': 'The workflow ran.'}).execute(context)`.

**L0066.** Continue the statement starting at L63 with `"subject": "FlowForge test"`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'FlowForge test', 'text': 'The workflow ran.'}).execute(context)`.

**L0067.** Continue the statement starting at L63 with `"text": "The workflow ran."`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'FlowForge test', 'text': 'The workflow ran.'}).execute(context)`.

**L0068.** Close the grouped expression/declaration introduced at L63; delimiters/commas complete the same statement rather than execute a separate operation.

**L0069.** Continue the statement starting at L63 with `).execute(context)`. Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `EmailAction({'to': ['recipient@example.com'], 'subject': 'FlowForge test', 'text': 'The workflow ran.'}).execute(context)`.

**L0070.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0071.** Test assertion: evaluate the comparison/membership/identity test `context.data['action_results'] == [{'type': 'email', 'provider': 'resend', 'status_code': 200, 'provider_id': 'email-123'}]`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0072.** Continue the statement starting at L71 with `{"type": "email", "provider": "resend", "status_code": 200, "provider_id": "email-123"}`. Test assertion: evaluate the comparison/membership/identity test `context.data['action_results'] == [{'type': 'email', 'provider': 'resend', 'status_code': 200, 'provider_id': 'email-123'}]`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0073.** Close the grouped expression/declaration introduced at L71; delimiters/commas complete the same statement rather than execute a separate operation.

**L0074.** Assign to `request`: look up/index `client.__enter__.return_value.send.call_args.args` using `0`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0075.** Test assertion: evaluate the comparison/membership/identity test `'test-key' in request.headers['Authorization']`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0076.** Test assertion: evaluate the comparison/membership/identity test `'test-key' not in str(context.data)`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0077.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0078.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0079.** Define function/method `test_email_action_validates_recipients(monkeypatch)` with intended return type `None`. Verify malformed recipient config raises before any send.

**L0080.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr('app.core.actions.email.settings.email_api_key', 'test-key')`.

**L0081.** Enter context manager(s): assert that the enclosed operation raises the expected exception: `pytest.raises(ValueError, match='valid email')`. Exit cleanup also runs when the body raises.

**L0082.** Perform the expression for its effect: call `EmailAction` with the displayed positional/named arguments: `EmailAction({'from': 'sender@example.com', 'to': ['not-an-email'], 'subject': 'Test', 'text': 'Body'})`.

**L0083.** Continue the statement starting at L82 with `{`. Perform the expression for its effect: call `EmailAction` with the displayed positional/named arguments: `EmailAction({'from': 'sender@example.com', 'to': ['not-an-email'], 'subject': 'Test', 'text': 'Body'})`.

**L0084.** Continue the statement starting at L82 with `"from": "sender@example.com"`. Perform the expression for its effect: call `EmailAction` with the displayed positional/named arguments: `EmailAction({'from': 'sender@example.com', 'to': ['not-an-email'], 'subject': 'Test', 'text': 'Body'})`.

**L0085.** Continue the statement starting at L82 with `"to": ["not-an-email"]`. Perform the expression for its effect: call `EmailAction` with the displayed positional/named arguments: `EmailAction({'from': 'sender@example.com', 'to': ['not-an-email'], 'subject': 'Test', 'text': 'Body'})`.

**L0086.** Continue the statement starting at L82 with `"subject": "Test"`. Perform the expression for its effect: call `EmailAction` with the displayed positional/named arguments: `EmailAction({'from': 'sender@example.com', 'to': ['not-an-email'], 'subject': 'Test', 'text': 'Body'})`.

**L0087.** Continue the statement starting at L82 with `"text": "Body"`. Perform the expression for its effect: call `EmailAction` with the displayed positional/named arguments: `EmailAction({'from': 'sender@example.com', 'to': ['not-an-email'], 'subject': 'Test', 'text': 'Body'})`.

**L0088.** Close the grouped expression/declaration introduced at L82; delimiters/commas complete the same statement rather than execute a separate operation.

**L0089.** Close the grouped expression/declaration introduced at L82; delimiters/commas complete the same statement rather than execute a separate operation.


<a id="backend-tests-testmodelspy"></a>
## backend/tests/test_models.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `0701923c108b210da5ccc67bc30002eb7ac929d0a8c82c660bbdc3b3443154e9`. Physical lines: 26.

### Numbered source

```python
0001 | from app.models import User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger
0002 | 
0003 | 
0004 | def test_workflow_configuration_round_trip(db_session) -> None:
0005 |     user = User(email="builder@example.com")
0006 |     db_session.add(user)
0007 |     db_session.flush()
0008 | 
0009 |     workflow = Workflow(user_id=user.id, name="Notify on PR merge", enabled=True)
0010 |     workflow.trigger = WorkflowTrigger(trigger_type="manual", config={"source": "ui"})
0011 |     workflow.conditions.append(
0012 |         WorkflowCondition(condition_type="equals", config={"field": "repository", "value": "FlowForge"})
0013 |     )
0014 |     workflow.actions.append(
0015 |         WorkflowAction(position=0, action_type="noop", config={})
0016 |     )
0017 |     db_session.add(workflow)
0018 |     db_session.flush()
0019 | 
0020 |     stored = db_session.get(Workflow, workflow.id)
0021 |     assert stored is not None
0022 |     assert stored.trigger is not None
0023 |     assert stored.trigger.trigger_type == "manual"
0024 |     assert stored.trigger.config["source"] == "ui"
0025 |     assert stored.conditions[0].condition_type == "equals"
0026 |     assert stored.actions[0].action_type == "noop"
```

### Every-line explanation

**L0001.** Import User, Workflow, WorkflowAction, WorkflowCondition, WorkflowTrigger from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Define function/method `test_workflow_configuration_round_trip(db_session)` with intended return type `None`. Construct ORM rows/relationships and verify retrieval of saved workflow configuration.

**L0005.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='builder@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0006.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0007.** Perform the expression for its effect: flush the test transaction so IDs/config are available: `db_session.flush()`.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(user_id=user.id, name='Notify on PR merge', enabled=True)`. Assignment stores a value/reference; it is not an equality test.

**L0010.** Assign to `workflow.trigger`: call `WorkflowTrigger` with the displayed positional/named arguments: `WorkflowTrigger(trigger_type='manual', config={'source': 'ui'})`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `workflow.conditions.append(WorkflowCondition(condition_type='equals', config={'field': 'repository', 'value': 'FlowForge'}))`.

**L0012.** Continue the statement starting at L11 with `WorkflowCondition(condition_type="equals", config={"field": "repository", "value": "FlowForge"})`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `workflow.conditions.append(WorkflowCondition(condition_type='equals', config={'field': 'repository', 'value': 'FlowForge'}))`.

**L0013.** Close the grouped expression/declaration introduced at L11; delimiters/commas complete the same statement rather than execute a separate operation.

**L0014.** Perform the expression for its effect: mutate the receiver list by adding one item at its end: `workflow.actions.append(WorkflowAction(position=0, action_type='noop', config={}))`.

**L0015.** Continue the statement starting at L14 with `WorkflowAction(position=0, action_type="noop", config={})`. Perform the expression for its effect: mutate the receiver list by adding one item at its end: `workflow.actions.append(WorkflowAction(position=0, action_type='noop', config={}))`.

**L0016.** Close the grouped expression/declaration introduced at L14; delimiters/commas complete the same statement rather than execute a separate operation.

**L0017.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(workflow)`.

**L0018.** Perform the expression for its effect: flush the test transaction so IDs/config are available: `db_session.flush()`.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Assign to `stored`: look up the persisted fixture row by primary key: `db_session.get(Workflow, workflow.id)`. Assignment stores a value/reference; it is not an equality test.

**L0021.** Test assertion: evaluate the comparison/membership/identity test `stored is not None`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0022.** Test assertion: evaluate the comparison/membership/identity test `stored.trigger is not None`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0023.** Test assertion: evaluate the comparison/membership/identity test `stored.trigger.trigger_type == 'manual'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0024.** Test assertion: evaluate the comparison/membership/identity test `stored.trigger.config['source'] == 'ui'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0025.** Test assertion: evaluate the comparison/membership/identity test `stored.conditions[0].condition_type == 'equals'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0026.** Test assertion: evaluate the comparison/membership/identity test `stored.actions[0].action_type == 'noop'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.


<a id="backend-tests-testooppy"></a>
## backend/tests/test_oop.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `152f3514dcbc245b0ad59170c76638e4c3d345749a769072f43fe03fdb851e2e`. Physical lines: 55.

### Numbered source

```python
0001 | from app.core.actions import Action, NoOpAction
0002 | from app.core.conditions import EqualsCondition
0003 | from app.core.event import Event, ExecutionContext
0004 | from app.core.triggers import ManualTrigger, Trigger
0005 | from app.core.workflow import Workflow
0006 | 
0007 | 
0008 | def test_manual_trigger_matches_manual_event() -> None:
0009 |     trigger: Trigger = ManualTrigger()
0010 |     event = Event(type="manual", source="ui", payload={})
0011 |     assert trigger.should_execute(event) is True
0012 | 
0013 | 
0014 | def test_manual_trigger_rejects_webhook_event() -> None:
0015 |     trigger = ManualTrigger()
0016 |     event = Event(type="webhook", source="github", payload={})
0017 |     assert trigger.should_execute(event) is False
0018 | 
0019 | 
0020 | def test_equals_condition_true_and_false() -> None:
0021 |     condition = EqualsCondition(field="repository", value="FlowForge")
0022 |     matching = ExecutionContext(
0023 |         event=Event(type="manual", source="manual"),
0024 |         data={"repository": "FlowForge"},
0025 |     )
0026 |     other = ExecutionContext(
0027 |         event=Event(type="manual", source="manual"),
0028 |         data={"repository": "other"},
0029 |     )
0030 |     assert condition.evaluate(matching) is True
0031 |     assert condition.evaluate(other) is False
0032 | 
0033 | 
0034 | def test_workflow_composition_executes_actions_via_base_type() -> None:
0035 |     action = NoOpAction()
0036 |     workflow = Workflow(
0037 |         name="Notify on manual run",
0038 |         trigger=ManualTrigger(),
0039 |         condition=EqualsCondition(field="repository", value="FlowForge"),
0040 |         actions=[action],
0041 |     )
0042 |     event = Event(type="manual", source="manual", payload={"repository": "FlowForge"})
0043 |     context = ExecutionContext(event=event, data={"repository": "FlowForge"})
0044 | 
0045 |     assert workflow.trigger.should_execute(event) is True
0046 |     assert workflow.condition.evaluate(context) is True
0047 | 
0048 |     executed = 0
0049 |     for step in workflow.actions:
0050 |         assert isinstance(step, Action)
0051 |         step.execute(context)
0052 |         executed += 1
0053 | 
0054 |     assert executed == 1
0055 |     assert len(action.calls) == 1
```

### Every-line explanation

**L0001.** Import Action, NoOpAction from `app.core.actions`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import EqualsCondition from `app.core.conditions`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Import Event, ExecutionContext from `app.core.event`. Imported names become available in this module; aliases distinguish roles where used.

**L0004.** Import ManualTrigger, Trigger from `app.core.triggers`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import Workflow from `app.core.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Define function/method `test_manual_trigger_matches_manual_event()` with intended return type `None`. Check a manual normalized event matches the concrete trigger through its base type.

**L0009.** Declare `trigger` with intended type `Trigger` and initialize it: call `ManualTrigger` with the displayed positional/named arguments: `ManualTrigger()`.

**L0010.** Assign to `event`: construct a normalized input-event envelope: `Event(type='manual', source='ui', payload={})`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Test assertion: evaluate the comparison/membership/identity test `trigger.should_execute(event) is True`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0012.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Define function/method `test_manual_trigger_rejects_webhook_event()` with intended return type `None`. Check an ordinary GitHub webhook does not match ManualTrigger.

**L0015.** Assign to `trigger`: call `ManualTrigger` with the displayed positional/named arguments: `ManualTrigger()`. Assignment stores a value/reference; it is not an equality test.

**L0016.** Assign to `event`: construct a normalized input-event envelope: `Event(type='webhook', source='github', payload={})`. Assignment stores a value/reference; it is not an equality test.

**L0017.** Test assertion: evaluate the comparison/membership/identity test `trigger.should_execute(event) is False`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0018.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0019.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0020.** Define function/method `test_equals_condition_true_and_false()` with intended return type `None`. Check equality on matching and nonmatching context data.

**L0021.** Assign to `condition`: call `EqualsCondition` with the displayed positional/named arguments: `EqualsCondition(field='repository', value='FlowForge')`. Assignment stores a value/reference; it is not an equality test.

**L0022.** Assign to `matching`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'repository': 'FlowForge'})`. Assignment stores a value/reference; it is not an equality test.

**L0023.** Continue the statement starting at L22 with `event=Event(type="manual", source="manual")`. Assign to `matching`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'repository': 'FlowForge'})`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Continue the statement starting at L22 with `data={"repository": "FlowForge"}`. Assign to `matching`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'repository': 'FlowForge'})`. Assignment stores a value/reference; it is not an equality test.

**L0025.** Close the grouped expression/declaration introduced at L22; delimiters/commas complete the same statement rather than execute a separate operation.

**L0026.** Assign to `other`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'repository': 'other'})`. Assignment stores a value/reference; it is not an equality test.

**L0027.** Continue the statement starting at L26 with `event=Event(type="manual", source="manual")`. Assign to `other`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'repository': 'other'})`. Assignment stores a value/reference; it is not an equality test.

**L0028.** Continue the statement starting at L26 with `data={"repository": "other"}`. Assign to `other`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=Event(type='manual', source='manual'), data={'repository': 'other'})`. Assignment stores a value/reference; it is not an equality test.

**L0029.** Close the grouped expression/declaration introduced at L26; delimiters/commas complete the same statement rather than execute a separate operation.

**L0030.** Test assertion: evaluate the comparison/membership/identity test `condition.evaluate(matching) is True`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0031.** Test assertion: evaluate the comparison/membership/identity test `condition.evaluate(other) is False`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0032.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0033.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0034.** Define function/method `test_workflow_composition_executes_actions_via_base_type()` with intended return type `None`. Compose objects, evaluate the parts, and call an action through the shared interface.

**L0035.** Assign to `action`: call `NoOpAction` with the displayed positional/named arguments: `NoOpAction()`. Assignment stores a value/reference; it is not an equality test.

**L0036.** Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='Notify on manual run', trigger=ManualTrigger(), condition=EqualsCondition(field='repository', value='FlowForge'), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0037.** Continue the statement starting at L36 with `name="Notify on manual run"`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='Notify on manual run', trigger=ManualTrigger(), condition=EqualsCondition(field='repository', value='FlowForge'), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0038.** Continue the statement starting at L36 with `trigger=ManualTrigger()`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='Notify on manual run', trigger=ManualTrigger(), condition=EqualsCondition(field='repository', value='FlowForge'), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0039.** Continue the statement starting at L36 with `condition=EqualsCondition(field="repository", value="FlowForge")`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='Notify on manual run', trigger=ManualTrigger(), condition=EqualsCondition(field='repository', value='FlowForge'), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0040.** Continue the statement starting at L36 with `actions=[action]`. Assign to `workflow`: construct the imported Workflow class; the imports identify ORM versus runtime role: `Workflow(name='Notify on manual run', trigger=ManualTrigger(), condition=EqualsCondition(field='repository', value='FlowForge'), actions=[action])`. Assignment stores a value/reference; it is not an equality test.

**L0041.** Close the grouped expression/declaration introduced at L36; delimiters/commas complete the same statement rather than execute a separate operation.

**L0042.** Assign to `event`: construct a normalized input-event envelope: `Event(type='manual', source='manual', payload={'repository': 'FlowForge'})`. Assignment stores a value/reference; it is not an equality test.

**L0043.** Assign to `context`: construct per-run state, keeping input event and mutable data separate: `ExecutionContext(event=event, data={'repository': 'FlowForge'})`. Assignment stores a value/reference; it is not an equality test.

**L0044.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0045.** Test assertion: evaluate the comparison/membership/identity test `workflow.trigger.should_execute(event) is True`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0046.** Test assertion: evaluate the comparison/membership/identity test `workflow.condition.evaluate(context) is True`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0047.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0048.** Assign to `executed`: use literal value `0` (int). Assignment stores a value/reference; it is not an equality test.

**L0049.** Iterate over `workflow.actions`, binding each item/pair to `step`. The indented body runs once per item unless it returns/raises/breaks.

**L0050.** Test assertion: perform an actual runtime type check: `isinstance(step, Action)`. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0051.** Perform the expression for its effect: invoke this runtime engine/action operation; concrete dispatch depends on the receiver: `step.execute(context)`.

**L0052.** Update `executed` with `executed += 1`; here the completed-action count increases only after a normal action return.

**L0053.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0054.** Test assertion: evaluate the comparison/membership/identity test `executed == 1`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0055.** Test assertion: evaluate the comparison/membership/identity test `len(action.calls) == 1`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.


<a id="backend-tests-testworkflowapipy"></a>
## backend/tests/test_workflow_api.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `a72f6ae2356990417ab61370bea02d6f793110883f270b617b2099f2eb61a176`. Physical lines: 166.

### Numbered source

```python
0001 | import hashlib
0002 | import hmac
0003 | 
0004 | from app.db import get_session
0005 | from app.main import app
0006 | from app.models import User
0007 | 
0008 | 
0009 | def test_create_load_and_run_workflow_api(client, db_session) -> None:
0010 |     user = User(email="api@example.com")
0011 |     db_session.add(user)
0012 |     db_session.commit()
0013 | 
0014 |     def override_session():
0015 |         yield db_session
0016 | 
0017 |     app.dependency_overrides[get_session] = override_session
0018 |     try:
0019 |         create = client.post(
0020 |             "/api/workflows",
0021 |             json={
0022 |                 "user_id": user.id,
0023 |                 "name": "API workflow",
0024 |                 "enabled": True,
0025 |                 "trigger": {"type": "manual"},
0026 |                 "conditions": [],
0027 |                 "actions": [{"type": "noop"}],
0028 |             },
0029 |         )
0030 |         assert create.status_code == 201
0031 |         workflow_id = create.json()["id"]
0032 | 
0033 |         loaded = client.get(f"/api/workflows/{workflow_id}")
0034 |         run = client.post(f"/api/workflows/{workflow_id}/run", json={"payload": {"source": "test"}})
0035 | 
0036 |         assert loaded.status_code == 200
0037 |         assert loaded.json()["name"] == "API workflow"
0038 |         assert run.status_code == 200
0039 |         assert run.json()["status"] == "SUCCESS"
0040 |     finally:
0041 |         app.dependency_overrides.clear()
0042 | 
0043 | 
0044 | def test_github_webhook_runs_enabled_webhook_workflow(client, db_session) -> None:
0045 |     user = User(email="webhook@example.com")
0046 |     db_session.add(user)
0047 |     db_session.commit()
0048 | 
0049 |     def override_session():
0050 |         yield db_session
0051 | 
0052 |     app.dependency_overrides[get_session] = override_session
0053 |     try:
0054 |         create = client.post(
0055 |             "/api/workflows",
0056 |             json={
0057 |                 "user_id": user.id,
0058 |                 "name": "GitHub workflow",
0059 |                 "enabled": True,
0060 |                 "trigger": {"type": "webhook", "config": {"source": "github"}},
0061 |                 "actions": [{"type": "noop"}],
0062 |             },
0063 |         )
0064 |         assert create.status_code == 201
0065 | 
0066 |         webhook = client.post("/api/webhooks/github", json={"action": "opened"})
0067 | 
0068 |         assert webhook.status_code == 200
0069 |         assert webhook.json()[0]["status"] == "SUCCESS"
0070 |     finally:
0071 |         app.dependency_overrides.clear()
0072 | 
0073 | 
0074 | def test_github_webhook_requires_valid_signature(client, monkeypatch) -> None:
0075 |     monkeypatch.setattr("app.api.routes.webhooks.settings.github_webhook_secret", "test-secret")
0076 |     payload = b'{"action":"opened"}'
0077 |     signature = "sha256=" + hmac.new(b"test-secret", payload, hashlib.sha256).hexdigest()
0078 | 
0079 |     missing = client.post(
0080 |         "/api/webhooks/github",
0081 |         content=payload,
0082 |         headers={"content-type": "application/json"},
0083 |     )
0084 |     valid = client.post(
0085 |         "/api/webhooks/github",
0086 |         content=payload,
0087 |         headers={"content-type": "application/json", "x-hub-signature-256": signature},
0088 |     )
0089 | 
0090 |     assert missing.status_code == 401
0091 |     assert valid.status_code == 200
0092 | 
0093 | 
0094 | def test_workflow_can_be_updated_and_deleted(client, db_session) -> None:
0095 |     user = User(email="crud@example.com")
0096 |     db_session.add(user)
0097 |     db_session.commit()
0098 | 
0099 |     def override_session():
0100 |         yield db_session
0101 | 
0102 |     app.dependency_overrides[get_session] = override_session
0103 |     try:
0104 |         create = client.post(
0105 |             "/api/workflows",
0106 |             json={
0107 |                 "user_id": user.id,
0108 |                 "name": "Before",
0109 |                 "enabled": True,
0110 |                 "trigger": {"type": "manual"},
0111 |                 "actions": [{"type": "noop"}],
0112 |             },
0113 |         )
0114 |         workflow_id = create.json()["id"]
0115 | 
0116 |         update = client.put(
0117 |             f"/api/workflows/{workflow_id}",
0118 |             json={
0119 |                 "name": "After",
0120 |                 "enabled": False,
0121 |                 "trigger": {"type": "webhook", "config": {"source": "github"}},
0122 |                 "conditions": [{"type": "equals", "config": {"field": "action", "value": "opened"}}],
0123 |                 "actions": [{"type": "noop"}],
0124 |             },
0125 |         )
0126 |         assert update.status_code == 200
0127 |         assert update.json()["name"] == "After"
0128 |         assert update.json()["trigger"]["type"] == "webhook"
0129 | 
0130 |         deleted = client.delete(f"/api/workflows/{workflow_id}")
0131 |         assert deleted.status_code == 204
0132 |         assert client.get(f"/api/workflows/{workflow_id}").status_code == 404
0133 |     finally:
0134 |         app.dependency_overrides.clear()
0135 | 
0136 | 
0137 | def test_workflow_with_execution_can_be_deleted(client, db_session) -> None:
0138 |     user = User(email="delete-execution@example.com")
0139 |     db_session.add(user)
0140 |     db_session.commit()
0141 | 
0142 |     def override_session():
0143 |         yield db_session
0144 | 
0145 |     app.dependency_overrides[get_session] = override_session
0146 |     try:
0147 |         create = client.post(
0148 |             "/api/workflows",
0149 |             json={
0150 |                 "user_id": user.id,
0151 |                 "name": "Workflow with history",
0152 |                 "enabled": True,
0153 |                 "trigger": {"type": "manual"},
0154 |                 "actions": [{"type": "noop"}],
0155 |             },
0156 |         )
0157 |         workflow_id = create.json()["id"]
0158 |         run = client.post(f"/api/workflows/{workflow_id}/run", json={"payload": {}})
0159 |         assert run.status_code == 200
0160 | 
0161 |         deleted = client.delete(f"/api/workflows/{workflow_id}")
0162 | 
0163 |         assert deleted.status_code == 204
0164 |         assert client.get(f"/api/workflows/{workflow_id}").status_code == 404
0165 |     finally:
0166 |         app.dependency_overrides.clear()
```

### Every-line explanation

**L0001.** Import module(s) `hashlib`. Top-level module code runs on first import.

**L0002.** Import module(s) `hmac`. Top-level module code runs on first import.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Import get_session from `app.db`. Imported names become available in this module; aliases distinguish roles where used.

**L0005.** Import app from `app.main`. Imported names become available in this module; aliases distinguish roles where used.

**L0006.** Import User from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0009.** Define function/method `test_create_load_and_run_workflow_api(client, db_session)` with intended return type `None`. Exercise create/detail/manual-run HTTP endpoints with an overridden test database.

**L0010.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='api@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0011.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0012.** Perform the expression for its effect: commit fixture setup within the isolated test database: `db_session.commit()`.

**L0013.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0014.** Define function/method `override_session()`. 

**L0015.** Yield `db_session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0016.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0017.** Assign to `app.dependency_overrides[get_session]`: read/evaluate `override_session`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0019.** Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0020.** Continue the statement starting at L19 with `"/api/workflows"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0021.** Continue the statement starting at L19 with `json={`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0022.** Continue the statement starting at L19 with `"user_id": user.id`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0023.** Continue the statement starting at L19 with `"name": "API workflow"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0024.** Continue the statement starting at L19 with `"enabled": True`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0025.** Continue the statement starting at L19 with `"trigger": {"type": "manual"}`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0026.** Continue the statement starting at L19 with `"conditions": []`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0027.** Continue the statement starting at L19 with `"actions": [{"type": "noop"}]`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'API workflow', 'enabled': True, 'trigger': {'type': 'manual'}, 'conditions': [], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0028.** Close the grouped expression/declaration introduced at L19; delimiters/commas complete the same statement rather than execute a separate operation.

**L0029.** Close the grouped expression/declaration introduced at L19; delimiters/commas complete the same statement rather than execute a separate operation.

**L0030.** Test assertion: evaluate the comparison/membership/identity test `create.status_code == 201`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0031.** Assign to `workflow_id`: look up/index `create.json()` using `'id'`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0032.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0033.** Assign to `loaded`: issue GET through this client (an in-process app request in API tests): `client.get(f'/api/workflows/{workflow_id}')`. Assignment stores a value/reference; it is not an equality test.

**L0034.** Assign to `run`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post(f'/api/workflows/{workflow_id}/run', json={'payload': {'source': 'test'}})`. Assignment stores a value/reference; it is not an equality test.

**L0035.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0036.** Test assertion: evaluate the comparison/membership/identity test `loaded.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0037.** Test assertion: evaluate the comparison/membership/identity test `loaded.json()['name'] == 'API workflow'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0038.** Test assertion: evaluate the comparison/membership/identity test `run.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0039.** Test assertion: evaluate the comparison/membership/identity test `run.json()['status'] == 'SUCCESS'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0040.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0041.** Perform the expression for its effect: remove temporary test dependency overrides or collection entries: `app.dependency_overrides.clear()`.

**L0042.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0043.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0044.** Define function/method `test_github_webhook_runs_enabled_webhook_workflow(client, db_session)` with intended return type `None`. Create an enabled webhook workflow and exercise ingestion with unsigned local-mode test data.

**L0045.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='webhook@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0046.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0047.** Perform the expression for its effect: commit fixture setup within the isolated test database: `db_session.commit()`.

**L0048.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0049.** Define function/method `override_session()`. 

**L0050.** Yield `db_session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0051.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0052.** Assign to `app.dependency_overrides[get_session]`: read/evaluate `override_session`. Assignment stores a value/reference; it is not an equality test.

**L0053.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0054.** Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0055.** Continue the statement starting at L54 with `"/api/workflows"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0056.** Continue the statement starting at L54 with `json={`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0057.** Continue the statement starting at L54 with `"user_id": user.id`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0058.** Continue the statement starting at L54 with `"name": "GitHub workflow"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0059.** Continue the statement starting at L54 with `"enabled": True`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0060.** Continue the statement starting at L54 with `"trigger": {"type": "webhook", "config": {"source": "github"}}`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0061.** Continue the statement starting at L54 with `"actions": [{"type": "noop"}]`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'GitHub workflow', 'enabled': True, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0062.** Close the grouped expression/declaration introduced at L54; delimiters/commas complete the same statement rather than execute a separate operation.

**L0063.** Close the grouped expression/declaration introduced at L54; delimiters/commas complete the same statement rather than execute a separate operation.

**L0064.** Test assertion: evaluate the comparison/membership/identity test `create.status_code == 201`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0065.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0066.** Assign to `webhook`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', json={'action': 'opened'})`. Assignment stores a value/reference; it is not an equality test.

**L0067.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0068.** Test assertion: evaluate the comparison/membership/identity test `webhook.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0069.** Test assertion: evaluate the comparison/membership/identity test `webhook.json()[0]['status'] == 'SUCCESS'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0070.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0071.** Perform the expression for its effect: remove temporary test dependency overrides or collection entries: `app.dependency_overrides.clear()`.

**L0072.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0073.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0074.** Define function/method `test_github_webhook_requires_valid_signature(client, monkeypatch)` with intended return type `None`. Configure a fake secret and compare a missing-signature rejection with a correctly HMAC-signed request.

**L0075.** Perform the expression for its effect: temporarily replace an attribute for this test and restore it afterward: `monkeypatch.setattr('app.api.routes.webhooks.settings.github_webhook_secret', 'test-secret')`.

**L0076.** Assign to `payload`: use literal value `b'{"action":"opened"}'` (bytes). Assignment stores a value/reference; it is not an equality test.

**L0077.** Assign to `signature`: compute `'sha256=' + hmac.new(b'test-secret', payload, hashlib.sha256).hexdigest()` using the operator shown; datetime plus timedelta advances expiry, while numeric operators compute values. Assignment stores a value/reference; it is not an equality test.

**L0078.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0079.** Assign to `missing`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json'})`. Assignment stores a value/reference; it is not an equality test.

**L0080.** Continue the statement starting at L79 with `"/api/webhooks/github"`. Assign to `missing`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json'})`. Assignment stores a value/reference; it is not an equality test.

**L0081.** Continue the statement starting at L79 with `content=payload`. Assign to `missing`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json'})`. Assignment stores a value/reference; it is not an equality test.

**L0082.** Continue the statement starting at L79 with `headers={"content-type": "application/json"}`. Assign to `missing`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json'})`. Assignment stores a value/reference; it is not an equality test.

**L0083.** Close the grouped expression/declaration introduced at L79; delimiters/commas complete the same statement rather than execute a separate operation.

**L0084.** Assign to `valid`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json', 'x-hub-signature-256': signature})`. Assignment stores a value/reference; it is not an equality test.

**L0085.** Continue the statement starting at L84 with `"/api/webhooks/github"`. Assign to `valid`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json', 'x-hub-signature-256': signature})`. Assignment stores a value/reference; it is not an equality test.

**L0086.** Continue the statement starting at L84 with `content=payload`. Assign to `valid`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json', 'x-hub-signature-256': signature})`. Assignment stores a value/reference; it is not an equality test.

**L0087.** Continue the statement starting at L84 with `headers={"content-type": "application/json", "x-hub-signature-256": signature}`. Assign to `valid`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/webhooks/github', content=payload, headers={'content-type': 'application/json', 'x-hub-signature-256': signature})`. Assignment stores a value/reference; it is not an equality test.

**L0088.** Close the grouped expression/declaration introduced at L84; delimiters/commas complete the same statement rather than execute a separate operation.

**L0089.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0090.** Test assertion: evaluate the comparison/membership/identity test `missing.status_code == 401`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0091.** Test assertion: evaluate the comparison/membership/identity test `valid.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0092.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0093.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0094.** Define function/method `test_workflow_can_be_updated_and_deleted(client, db_session)` with intended return type `None`. Verify full configuration update and workflow deletion through routes.

**L0095.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='crud@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0096.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0097.** Perform the expression for its effect: commit fixture setup within the isolated test database: `db_session.commit()`.

**L0098.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0099.** Define function/method `override_session()`. 

**L0100.** Yield `db_session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0101.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0102.** Assign to `app.dependency_overrides[get_session]`: read/evaluate `override_session`. Assignment stores a value/reference; it is not an equality test.

**L0103.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0104.** Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0105.** Continue the statement starting at L104 with `"/api/workflows"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0106.** Continue the statement starting at L104 with `json={`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0107.** Continue the statement starting at L104 with `"user_id": user.id`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0108.** Continue the statement starting at L104 with `"name": "Before"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0109.** Continue the statement starting at L104 with `"enabled": True`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0110.** Continue the statement starting at L104 with `"trigger": {"type": "manual"}`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0111.** Continue the statement starting at L104 with `"actions": [{"type": "noop"}]`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Before', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0112.** Close the grouped expression/declaration introduced at L104; delimiters/commas complete the same statement rather than execute a separate operation.

**L0113.** Close the grouped expression/declaration introduced at L104; delimiters/commas complete the same statement rather than execute a separate operation.

**L0114.** Assign to `workflow_id`: look up/index `create.json()` using `'id'`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0115.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0116.** Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0117.** Continue the statement starting at L116 with `f"/api/workflows/{workflow_id}"`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0118.** Continue the statement starting at L116 with `json={`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0119.** Continue the statement starting at L116 with `"name": "After"`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0120.** Continue the statement starting at L116 with `"enabled": False`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0121.** Continue the statement starting at L116 with `"trigger": {"type": "webhook", "config": {"source": "github"}}`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0122.** Continue the statement starting at L116 with `"conditions": [{"type": "equals", "config": {"field": "action", "value": "opened"}}]`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0123.** Continue the statement starting at L116 with `"actions": [{"type": "noop"}]`. Assign to `update`: issue a replacement PUT request through the API test client: `client.put(f'/api/workflows/{workflow_id}', json={'name': 'After', 'enabled': False, 'trigger': {'type': 'webhook', 'config': {'source': 'github'}}, 'conditions': [{'type': 'equals', 'config': {'field': 'action', 'value': 'opened'}}], 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0124.** Close the grouped expression/declaration introduced at L116; delimiters/commas complete the same statement rather than execute a separate operation.

**L0125.** Close the grouped expression/declaration introduced at L116; delimiters/commas complete the same statement rather than execute a separate operation.

**L0126.** Test assertion: evaluate the comparison/membership/identity test `update.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0127.** Test assertion: evaluate the comparison/membership/identity test `update.json()['name'] == 'After'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0128.** Test assertion: evaluate the comparison/membership/identity test `update.json()['trigger']['type'] == 'webhook'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0129.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0130.** Assign to `deleted`: issue DELETE through the API test client: `client.delete(f'/api/workflows/{workflow_id}')`. Assignment stores a value/reference; it is not an equality test.

**L0131.** Test assertion: evaluate the comparison/membership/identity test `deleted.status_code == 204`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0132.** Test assertion: evaluate the comparison/membership/identity test `client.get(f'/api/workflows/{workflow_id}').status_code == 404`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0133.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0134.** Perform the expression for its effect: remove temporary test dependency overrides or collection entries: `app.dependency_overrides.clear()`.

**L0135.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0136.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0137.** Define function/method `test_workflow_with_execution_can_be_deleted(client, db_session)` with intended return type `None`. Regression proof that ORM cascading allows deletion after a persisted execution exists.

**L0138.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='delete-execution@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0139.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0140.** Perform the expression for its effect: commit fixture setup within the isolated test database: `db_session.commit()`.

**L0141.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0142.** Define function/method `override_session()`. 

**L0143.** Yield `db_session` to the dependency/fixture caller; code after yield is resumed during normal lifecycle/cleanup.

**L0144.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0145.** Assign to `app.dependency_overrides[get_session]`: read/evaluate `override_session`. Assignment stores a value/reference; it is not an equality test.

**L0146.** Start exception-aware operations; subsequent except/finally clauses define recovery/cleanup.

**L0147.** Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0148.** Continue the statement starting at L147 with `"/api/workflows"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0149.** Continue the statement starting at L147 with `json={`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0150.** Continue the statement starting at L147 with `"user_id": user.id`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0151.** Continue the statement starting at L147 with `"name": "Workflow with history"`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0152.** Continue the statement starting at L147 with `"enabled": True`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0153.** Continue the statement starting at L147 with `"trigger": {"type": "manual"}`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0154.** Continue the statement starting at L147 with `"actions": [{"type": "noop"}]`. Assign to `create`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post('/api/workflows', json={'user_id': user.id, 'name': 'Workflow with history', 'enabled': True, 'trigger': {'type': 'manual'}, 'actions': [{'type': 'noop'}]})`. Assignment stores a value/reference; it is not an equality test.

**L0155.** Close the grouped expression/declaration introduced at L147; delimiters/commas complete the same statement rather than execute a separate operation.

**L0156.** Close the grouped expression/declaration introduced at L147; delimiters/commas complete the same statement rather than execute a separate operation.

**L0157.** Assign to `workflow_id`: look up/index `create.json()` using `'id'`; missing keys/out-of-range indices can raise. Assignment stores a value/reference; it is not an equality test.

**L0158.** Assign to `run`: send POST through this client (TestClient in API tests, HTTPX in actions): `client.post(f'/api/workflows/{workflow_id}/run', json={'payload': {}})`. Assignment stores a value/reference; it is not an equality test.

**L0159.** Test assertion: evaluate the comparison/membership/identity test `run.status_code == 200`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0160.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0161.** Assign to `deleted`: issue DELETE through the API test client: `client.delete(f'/api/workflows/{workflow_id}')`. Assignment stores a value/reference; it is not an equality test.

**L0162.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0163.** Test assertion: evaluate the comparison/membership/identity test `deleted.status_code == 204`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0164.** Test assertion: evaluate the comparison/membership/identity test `client.get(f'/api/workflows/{workflow_id}').status_code == 404`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0165.** Cleanup block runs on normal completion and when control leaves through an exception/return; releases resources or restores test overrides.

**L0166.** Perform the expression for its effect: remove temporary test dependency overrides or collection entries: `app.dependency_overrides.clear()`.


<a id="backend-tests-testworkflowservicepy"></a>
## backend/tests/test_workflow_service.py

Test module. Each test definition's notes state its specific assertion scope. Network calls are mocked where indicated; test assertions do not establish live production behavior.

Source fingerprint: `36a961b103785900b75b2f2d869df80cdc985b164adb06e01db9043288662179`. Physical lines: 26.

### Numbered source

```python
0001 | from app.schemas.workflows import ComponentConfig, WorkflowCreate
0002 | from app.services.workflow import WorkflowService
0003 | 
0004 | 
0005 | def test_create_load_run_records_execution(db_session) -> None:
0006 |     from app.models import User
0007 | 
0008 |     user = User(email="engine@example.com")
0009 |     db_session.add(user)
0010 |     db_session.flush()
0011 | 
0012 |     request = WorkflowCreate(
0013 |         user_id=user.id,
0014 |         name="Run manually",
0015 |         enabled=True,
0016 |         trigger=ComponentConfig(type="manual"),
0017 |         conditions=[ComponentConfig(type="equals", config={"field": "repo", "value": "FlowForge"})],
0018 |         actions=[ComponentConfig(type="noop")],
0019 |     )
0020 |     service = WorkflowService(db_session)
0021 |     stored = service.create(request)
0022 |     execution = service.run_manual(stored.id, {"repo": "FlowForge"})
0023 | 
0024 |     assert execution.status == "SUCCESS"
0025 |     assert execution.result == {"action_count": 1}
0026 |     assert execution.error is None
```

### Every-line explanation

**L0001.** Import ComponentConfig, WorkflowCreate from `app.schemas.workflows`. Imported names become available in this module; aliases distinguish roles where used.

**L0002.** Import WorkflowService from `app.services.workflow`. Imported names become available in this module; aliases distinguish roles where used.

**L0003.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0004.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0005.** Define function/method `test_create_load_run_records_execution(db_session)` with intended return type `None`. Exercise service creation, hydration, execution, and history persistence together.

**L0006.** Import User from `app.models`. Imported names become available in this module; aliases distinguish roles where used.

**L0007.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0008.** Assign to `user`: call `User` with the displayed positional/named arguments: `User(email='engine@example.com')`. Assignment stores a value/reference; it is not an equality test.

**L0009.** Perform the expression for its effect: stage a fixture object in the isolated test database: `db_session.add(user)`.

**L0010.** Perform the expression for its effect: flush the test transaction so IDs/config are available: `db_session.flush()`.

**L0011.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0012.** Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0013.** Continue the statement starting at L12 with `user_id=user.id`. Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0014.** Continue the statement starting at L12 with `name="Run manually"`. Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0015.** Continue the statement starting at L12 with `enabled=True`. Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0016.** Continue the statement starting at L12 with `trigger=ComponentConfig(type="manual")`. Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0017.** Continue the statement starting at L12 with `conditions=[ComponentConfig(type="equals", config={"field": "repo", "value": "FlowForge"})]`. Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0018.** Continue the statement starting at L12 with `actions=[ComponentConfig(type="noop")]`. Assign to `request`: construct/validate workflow creation input: `WorkflowCreate(user_id=user.id, name='Run manually', enabled=True, trigger=ComponentConfig(type='manual'), conditions=[ComponentConfig(type='equals', config={'field': 'repo', 'value': 'FlowForge'})], actions=[ComponentConfig(type='noop')])`. Assignment stores a value/reference; it is not an equality test.

**L0019.** Close the grouped expression/declaration introduced at L12; delimiters/commas complete the same statement rather than execute a separate operation.

**L0020.** Assign to `service`: construct the use-case service with its database session: `WorkflowService(db_session)`. Assignment stores a value/reference; it is not an equality test.

**L0021.** Assign to `stored`: construct a component through a factory, or call a service create use case as identified by receiver: `service.create(request)`. Assignment stores a value/reference; it is not an equality test.

**L0022.** Assign to `execution`: wrap a request payload in a normalized manual Event and run it: `service.run_manual(stored.id, {'repo': 'FlowForge'})`. Assignment stores a value/reference; it is not an equality test.

**L0023.** Blank line: visual separation only; Python block membership is determined by indentation of actual statements.

**L0024.** Test assertion: evaluate the comparison/membership/identity test `execution.status == 'SUCCESS'`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0025.** Test assertion: evaluate the comparison/membership/identity test `execution.result == {'action_count': 1}`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.

**L0026.** Test assertion: evaluate the comparison/membership/identity test `execution.error is None`; this produces the branch/assertion's truth value. If false, pytest reports a failure; it is evidence for this property, not every possible behavior.


<a id="frontend-src-appcss"></a>
## frontend/src/App.css

INACTIVE starter stylesheet: App.tsx does not import this file. Its counter/hero/docs/ticks selectors and CSS variables are scaffold remnants, not workflow behavior. Notes explain the syntax without claiming these rules style the running product.

Source fingerprint: `c2571ce7245629994b8adc84f6c48e1920f047a4e7e29c89a4aeb51eeb1b5433`. Physical lines: 184.

### Numbered source

```css
0001 | .counter {
0002 |   font-size: 16px;
0003 |   padding: 5px 10px;
0004 |   border-radius: 5px;
0005 |   color: var(--accent);
0006 |   background: var(--accent-bg);
0007 |   border: 2px solid transparent;
0008 |   transition: border-color 0.3s;
0009 |   margin-bottom: 24px;
0010 | 
0011 |   &:hover {
0012 |     border-color: var(--accent-border);
0013 |   }
0014 |   &:focus-visible {
0015 |     outline: 2px solid var(--accent);
0016 |     outline-offset: 2px;
0017 |   }
0018 | }
0019 | 
0020 | .hero {
0021 |   position: relative;
0022 | 
0023 |   .base,
0024 |   .framework,
0025 |   .vite {
0026 |     inset-inline: 0;
0027 |     margin: 0 auto;
0028 |   }
0029 | 
0030 |   .base {
0031 |     width: 170px;
0032 |     position: relative;
0033 |     z-index: 0;
0034 |   }
0035 | 
0036 |   .framework,
0037 |   .vite {
0038 |     position: absolute;
0039 |   }
0040 | 
0041 |   .framework {
0042 |     z-index: 1;
0043 |     top: 34px;
0044 |     height: 28px;
0045 |     transform: perspective(2000px) rotateZ(300deg) rotateX(44deg) rotateY(39deg)
0046 |       scale(1.4);
0047 |   }
0048 | 
0049 |   .vite {
0050 |     z-index: 0;
0051 |     top: 107px;
0052 |     height: 26px;
0053 |     width: auto;
0054 |     transform: perspective(2000px) rotateZ(300deg) rotateX(40deg) rotateY(39deg)
0055 |       scale(0.8);
0056 |   }
0057 | }
0058 | 
0059 | #center {
0060 |   display: flex;
0061 |   flex-direction: column;
0062 |   gap: 25px;
0063 |   place-content: center;
0064 |   place-items: center;
0065 |   flex-grow: 1;
0066 | 
0067 |   @media (max-width: 1024px) {
0068 |     padding: 32px 20px 24px;
0069 |     gap: 18px;
0070 |   }
0071 | }
0072 | 
0073 | #next-steps {
0074 |   display: flex;
0075 |   border-top: 1px solid var(--border);
0076 |   text-align: left;
0077 | 
0078 |   & > div {
0079 |     flex: 1 1 0;
0080 |     padding: 32px;
0081 |     @media (max-width: 1024px) {
0082 |       padding: 24px 20px;
0083 |     }
0084 |   }
0085 | 
0086 |   .icon {
0087 |     margin-bottom: 16px;
0088 |     width: 22px;
0089 |     height: 22px;
0090 |   }
0091 | 
0092 |   @media (max-width: 1024px) {
0093 |     flex-direction: column;
0094 |     text-align: center;
0095 |   }
0096 | }
0097 | 
0098 | #docs {
0099 |   border-right: 1px solid var(--border);
0100 | 
0101 |   @media (max-width: 1024px) {
0102 |     border-right: none;
0103 |     border-bottom: 1px solid var(--border);
0104 |   }
0105 | }
0106 | 
0107 | #next-steps ul {
0108 |   list-style: none;
0109 |   padding: 0;
0110 |   display: flex;
0111 |   gap: 8px;
0112 |   margin: 32px 0 0;
0113 | 
0114 |   .logo {
0115 |     height: 18px;
0116 |   }
0117 | 
0118 |   a {
0119 |     color: var(--text-h);
0120 |     font-size: 16px;
0121 |     border-radius: 6px;
0122 |     background: var(--social-bg);
0123 |     display: flex;
0124 |     padding: 6px 12px;
0125 |     align-items: center;
0126 |     gap: 8px;
0127 |     text-decoration: none;
0128 |     transition: box-shadow 0.3s;
0129 | 
0130 |     &:hover {
0131 |       box-shadow: var(--shadow);
0132 |     }
0133 |     .button-icon {
0134 |       height: 18px;
0135 |       width: 18px;
0136 |     }
0137 |   }
0138 | 
0139 |   @media (max-width: 1024px) {
0140 |     margin-top: 20px;
0141 |     flex-wrap: wrap;
0142 |     justify-content: center;
0143 | 
0144 |     li {
0145 |       flex: 1 1 calc(50% - 8px);
0146 |     }
0147 | 
0148 |     a {
0149 |       width: 100%;
0150 |       justify-content: center;
0151 |       box-sizing: border-box;
0152 |     }
0153 |   }
0154 | }
0155 | 
0156 | #spacer {
0157 |   height: 88px;
0158 |   border-top: 1px solid var(--border);
0159 |   @media (max-width: 1024px) {
0160 |     height: 48px;
0161 |   }
0162 | }
0163 | 
0164 | .ticks {
0165 |   position: relative;
0166 |   width: 100%;
0167 | 
0168 |   &::before,
0169 |   &::after {
0170 |     content: '';
0171 |     position: absolute;
0172 |     top: -4.5px;
0173 |     border: 5px solid transparent;
0174 |   }
0175 | 
0176 |   &::before {
0177 |     left: 0;
0178 |     border-left-color: var(--border);
0179 |   }
0180 |   &::after {
0181 |     right: 0;
0182 |     border-right-color: var(--border);
0183 |   }
0184 | }
```

### Every-line explanation

**L0001.** Selector `.counter ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0002.** Continue this style rule. `font-size: 16px`: set text size.

**L0003.** Continue this style rule. `padding: 5px 10px`: set internal spacing.

**L0004.** Continue this style rule. `border-radius: 5px`: round the corners.

**L0005.** Continue this style rule. `color: var(--accent)`: set foreground/text color.

**L0006.** Continue this style rule. `background: var(--accent-bg)`: set background shorthand.

**L0007.** Continue this style rule. `border: 2px solid transparent`: set border width/style/color.

**L0008.** Continue this style rule. `transition: border-color 0.3s`: animate changes of named properties over a duration.

**L0009.** Continue this style rule. `margin-bottom: 24px`: set space below.

**L0010.** Blank formatting line; no CSS rule.

**L0011.** Selector `&:hover ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0012.** Continue this style rule. `border-color: var(--accent-border)`: set border colors.

**L0013.** Close the current selector or media-query block.

**L0014.** Selector `&:focus-visible ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0015.** Continue this style rule. `outline: 2px solid var(--accent)`: draw a focus/selection outline outside the border.

**L0016.** Continue this style rule. `outline-offset: 2px`: move an outline away from the box.

**L0017.** Close the current selector or media-query block.

**L0018.** Close the current selector or media-query block.

**L0019.** Blank formatting line; no CSS rule.

**L0020.** Selector `.hero ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0021.** Continue this style rule. `position: relative`: choose normal/relative/absolute positioning.

**L0022.** Blank formatting line; no CSS rule.

**L0023.** Continue the comma-separated selector group; the next selector shares the rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0024.** Continue the comma-separated selector group; the next selector shares the rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0025.** Selector `.vite ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0026.** Continue this style rule. `inset-inline: 0`: set logical left/right offsets according to writing direction.

**L0027.** Continue this style rule. `margin: 0 auto`: set outer spacing (one to four sides or auto centering).

**L0028.** Close the current selector or media-query block.

**L0029.** Blank formatting line; no CSS rule.

**L0030.** Selector `.base ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0031.** Continue this style rule. `width: 170px`: set element width.

**L0032.** Continue this style rule. `position: relative`: choose normal/relative/absolute positioning.

**L0033.** Continue this style rule. `z-index: 0`: set stacking priority within applicable stacking contexts.

**L0034.** Close the current selector or media-query block.

**L0035.** Blank formatting line; no CSS rule.

**L0036.** Continue the comma-separated selector group; the next selector shares the rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0037.** Selector `.vite ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0038.** Continue this style rule. `position: absolute`: choose normal/relative/absolute positioning.

**L0039.** Close the current selector or media-query block.

**L0040.** Blank formatting line; no CSS rule.

**L0041.** Selector `.framework ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0042.** Continue this style rule. `z-index: 1`: set stacking priority within applicable stacking contexts.

**L0043.** Continue this style rule. `top: 34px`: set top offset for positioned content.

**L0044.** Continue this style rule. `height: 28px`: set element height.

**L0045.** Continue this style rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0046.** Continue this style rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0047.** Close the current selector or media-query block.

**L0048.** Blank formatting line; no CSS rule.

**L0049.** Selector `.vite ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0050.** Continue this style rule. `z-index: 0`: set stacking priority within applicable stacking contexts.

**L0051.** Continue this style rule. `top: 107px`: set top offset for positioned content.

**L0052.** Continue this style rule. `height: 26px`: set element height.

**L0053.** Continue this style rule. `width: auto`: set element width.

**L0054.** Continue this style rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0055.** Continue this style rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0056.** Close the current selector or media-query block.

**L0057.** Close the current selector or media-query block.

**L0058.** Blank formatting line; no CSS rule.

**L0059.** Selector `#center ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0060.** Continue this style rule. `display: flex`: choose grid/flex/block display behavior.

**L0061.** Continue this style rule. `flex-direction: column`: choose row/column flow.

**L0062.** Continue this style rule. `gap: 25px`: set space between grid/flex items.

**L0063.** Continue this style rule. `place-content: center`: align the layout's content in both axes.

**L0064.** Continue this style rule. `place-items: center`: align items in both relevant axes.

**L0065.** Continue this style rule. `flex-grow: 1`: allow expansion within a flex container.

**L0066.** Blank formatting line; no CSS rule.

**L0067.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0068.** Continue this style rule. `padding: 32px 20px 24px`: set internal spacing.

**L0069.** Continue this style rule. `gap: 18px`: set space between grid/flex items.

**L0070.** Close the current selector or media-query block.

**L0071.** Close the current selector or media-query block.

**L0072.** Blank formatting line; no CSS rule.

**L0073.** Selector `#next-steps ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0074.** Continue this style rule. `display: flex`: choose grid/flex/block display behavior.

**L0075.** Continue this style rule. `border-top: 1px solid var(--border)`: set the upper border.

**L0076.** Continue this style rule. `text-align: left`: align inline text inside its box.

**L0077.** Blank formatting line; no CSS rule.

**L0078.** Selector `& > div ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0079.** Continue this style rule. `flex: 1 1 0`: set the grow/shrink/basis shorthand.

**L0080.** Continue this style rule. `padding: 32px`: set internal spacing.

**L0081.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0082.** Continue this style rule. `padding: 24px 20px`: set internal spacing.

**L0083.** Close the current selector or media-query block.

**L0084.** Close the current selector or media-query block.

**L0085.** Blank formatting line; no CSS rule.

**L0086.** Selector `.icon ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0087.** Continue this style rule. `margin-bottom: 16px`: set space below.

**L0088.** Continue this style rule. `width: 22px`: set element width.

**L0089.** Continue this style rule. `height: 22px`: set element height.

**L0090.** Close the current selector or media-query block.

**L0091.** Blank formatting line; no CSS rule.

**L0092.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0093.** Continue this style rule. `flex-direction: column`: choose row/column flow.

**L0094.** Continue this style rule. `text-align: center`: align inline text inside its box.

**L0095.** Close the current selector or media-query block.

**L0096.** Close the current selector or media-query block.

**L0097.** Blank formatting line; no CSS rule.

**L0098.** Selector `#docs ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0099.** Continue this style rule. `border-right: 1px solid var(--border)`: set the right border.

**L0100.** Blank formatting line; no CSS rule.

**L0101.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0102.** Continue this style rule. `border-right: none`: set the right border.

**L0103.** Continue this style rule. `border-bottom: 1px solid var(--border)`: set the lower border.

**L0104.** Close the current selector or media-query block.

**L0105.** Close the current selector or media-query block.

**L0106.** Blank formatting line; no CSS rule.

**L0107.** Selector `#next-steps ul ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0108.** Continue this style rule. `list-style: none`: control list markers.

**L0109.** Continue this style rule. `padding: 0`: set internal spacing.

**L0110.** Continue this style rule. `display: flex`: choose grid/flex/block display behavior.

**L0111.** Continue this style rule. `gap: 8px`: set space between grid/flex items.

**L0112.** Continue this style rule. `margin: 32px 0 0`: set outer spacing (one to four sides or auto centering).

**L0113.** Blank formatting line; no CSS rule.

**L0114.** Selector `.logo ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0115.** Continue this style rule. `height: 18px`: set element height.

**L0116.** Close the current selector or media-query block.

**L0117.** Blank formatting line; no CSS rule.

**L0118.** Selector `a ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0119.** Continue this style rule. `color: var(--text-h)`: set foreground/text color.

**L0120.** Continue this style rule. `font-size: 16px`: set text size.

**L0121.** Continue this style rule. `border-radius: 6px`: round the corners.

**L0122.** Continue this style rule. `background: var(--social-bg)`: set background shorthand.

**L0123.** Continue this style rule. `display: flex`: choose grid/flex/block display behavior.

**L0124.** Continue this style rule. `padding: 6px 12px`: set internal spacing.

**L0125.** Continue this style rule. `align-items: center`: align items on the cross/block axis.

**L0126.** Continue this style rule. `gap: 8px`: set space between grid/flex items.

**L0127.** Continue this style rule. `text-decoration: none`: set underline/other text decoration.

**L0128.** Continue this style rule. `transition: box-shadow 0.3s`: animate changes of named properties over a duration.

**L0129.** Blank formatting line; no CSS rule.

**L0130.** Selector `&:hover ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0131.** Continue this style rule. `box-shadow: var(--shadow)`: draw an outer shadow without changing layout dimensions.

**L0132.** Close the current selector or media-query block.

**L0133.** Selector `.button-icon ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0134.** Continue this style rule. `height: 18px`: set element height.

**L0135.** Continue this style rule. `width: 18px`: set element width.

**L0136.** Close the current selector or media-query block.

**L0137.** Close the current selector or media-query block.

**L0138.** Blank formatting line; no CSS rule.

**L0139.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0140.** Continue this style rule. `margin-top: 20px`: set space above.

**L0141.** Continue this style rule. `flex-wrap: wrap`: allow flex items to wrap.

**L0142.** Continue this style rule. `justify-content: center`: distribute/align items along the layout's main/inline axis.

**L0143.** Blank formatting line; no CSS rule.

**L0144.** Selector `li ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0145.** Continue this style rule. `flex: 1 1 calc(50% - 8px)`: set the grow/shrink/basis shorthand.

**L0146.** Close the current selector or media-query block.

**L0147.** Blank formatting line; no CSS rule.

**L0148.** Selector `a ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0149.** Continue this style rule. `width: 100%`: set element width.

**L0150.** Continue this style rule. `justify-content: center`: distribute/align items along the layout's main/inline axis.

**L0151.** Continue this style rule. `box-sizing: border-box`: choose whether declared dimensions include border/padding.

**L0152.** Close the current selector or media-query block.

**L0153.** Close the current selector or media-query block.

**L0154.** Close the current selector or media-query block.

**L0155.** Blank formatting line; no CSS rule.

**L0156.** Selector `#spacer ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0157.** Continue this style rule. `height: 88px`: set element height.

**L0158.** Continue this style rule. `border-top: 1px solid var(--border)`: set the upper border.

**L0159.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0160.** Continue this style rule. `height: 48px`: set element height.

**L0161.** Close the current selector or media-query block.

**L0162.** Close the current selector or media-query block.

**L0163.** Blank formatting line; no CSS rule.

**L0164.** Selector `.ticks ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0165.** Continue this style rule. `position: relative`: choose normal/relative/absolute positioning.

**L0166.** Continue this style rule. `width: 100%`: set element width.

**L0167.** Blank formatting line; no CSS rule.

**L0168.** Continue the comma-separated selector group; the next selector shares the rule. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0169.** Selector `&::after ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0170.** Continue this style rule. `content: ''`: generate pseudo-element content.

**L0171.** Continue this style rule. `position: absolute`: choose normal/relative/absolute positioning.

**L0172.** Continue this style rule. `top: -4.5px`: set top offset for positioned content.

**L0173.** Continue this style rule. `border: 5px solid transparent`: set border width/style/color.

**L0174.** Close the current selector or media-query block.

**L0175.** Blank formatting line; no CSS rule.

**L0176.** Selector `&::before ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0177.** Continue this style rule. `left: 0`: set left offset.

**L0178.** Continue this style rule. `border-left-color: var(--border)`: set left border color.

**L0179.** Close the current selector or media-query block.

**L0180.** Selector `&::after ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. The surrounding rule supplies context; parentheses group transform/function arguments and braces delimit style blocks.

**L0181.** Continue this style rule. `right: 0`: set right offset.

**L0182.** Continue this style rule. `border-right-color: var(--border)`: set right border color.

**L0183.** Close the current selector or media-query block.

**L0184.** Close the current selector or media-query block.


<a id="frontend-src-apptsx"></a>
## frontend/src/App.tsx

Single component for auth, Gmail, builder, list, and history. The builder loads/saves only the first condition and action, while the backend supports richer config. State/effects update the browser; the server executes workflows. No Router, Redux, Tailwind, or Axios is used.

Source fingerprint: `88a79d9534fa45cba3669cb1b8bffd4daa097b7190d9893589f25c0f939644d3`. Physical lines: 312.

### Numbered source

```tsx
0001 | import { useEffect, useState } from 'react'
0002 | import type { FormEvent } from 'react'
0003 | import type { Session } from '@supabase/supabase-js'
0004 | import { api } from './services/api'
0005 | import type { Component, Execution, GmailStatus, Workflow, WorkflowDetail } from './services/api'
0006 | import { supabase } from './lib/supabase'
0007 | 
0008 | const emptyComponent = (type: string): Component => ({ type, config: {} })
0009 | const apiBaseUrl = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'
0010 | const githubWebhookUrl = `${apiBaseUrl.replace(/\/$/, '')}/api/webhooks/github`
0011 | 
0012 | function App() {
0013 |   const [session, setSession] = useState<Session | null>(null)
0014 |   const [email, setEmail] = useState('')
0015 |   const [password, setPassword] = useState('')
0016 |   const [workflows, setWorkflows] = useState<Workflow[]>([])
0017 |   const [selected, setSelected] = useState<WorkflowDetail | null>(null)
0018 |   const [executions, setExecutions] = useState<Execution[]>([])
0019 |   const [name, setName] = useState('')
0020 |   const [triggerType, setTriggerType] = useState('manual')
0021 |   const [condition, setCondition] = useState<Component | null>(null)
0022 |   const [conditionField, setConditionField] = useState('')
0023 |   const [conditionValue, setConditionValue] = useState('')
0024 |   const [actionType, setActionType] = useState('noop')
0025 |   const [actionConfig, setActionConfig] = useState('{}')
0026 |   const [githubToken, setGithubToken] = useState('')
0027 |   const [githubRepository, setGithubRepository] = useState('')
0028 |   const [githubEventType, setGithubEventType] = useState('flowforge')
0029 |   const [githubPayload, setGithubPayload] = useState('{}')
0030 |   const [emailTo, setEmailTo] = useState('')
0031 |   const [emailSubject, setEmailSubject] = useState('')
0032 |   const [emailText, setEmailText] = useState('')
0033 |   const [emailHtml, setEmailHtml] = useState('')
0034 |   const [enabled, setEnabled] = useState(true)
0035 |   const [error, setError] = useState<string | null>(null)
0036 |   const [busy, setBusy] = useState(false)
0037 |   const [gmail, setGmail] = useState<GmailStatus>({ connected: false, email: null })
0038 | 
0039 |   useEffect(() => {
0040 |     if (!supabase) return
0041 |     void supabase.auth.getSession().then(({ data }) => setSession(data.session))
0042 |     const { data } = supabase.auth.onAuthStateChange((_event, nextSession) => setSession(nextSession))
0043 |     return () => data.subscription.unsubscribe()
0044 |   }, [])
0045 | 
0046 |   useEffect(() => {
0047 |     const query = new URLSearchParams(window.location.search)
0048 |     const gmailResult = query.get('gmail')
0049 |     const detail = query.get('detail')
0050 |     if (gmailResult === 'error') {
0051 |       setError(detail ?? `Gmail connection failed (${query.get('reason') ?? 'unknown error'})`)
0052 |       window.history.replaceState({}, '', window.location.pathname)
0053 |     }
0054 |   }, [])
0055 | 
0056 |   useEffect(() => {
0057 |     if (session?.user.id) void refreshWorkflows(session.user.id)
0058 |   }, [session?.user.id])
0059 | 
0060 |   useEffect(() => {
0061 |     if (session?.user.id) {
0062 |       void api.gmailStatus().then(setGmail).catch(() => setGmail({ connected: false, email: null }))
0063 |     }
0064 |   }, [session?.user.id])
0065 | 
0066 |   async function refreshWorkflows(userId: string) {
0067 |     try {
0068 |       setWorkflows(await api.listWorkflows(userId))
0069 |     } catch (caught) {
0070 |       setError(caught instanceof Error ? caught.message : 'Could not load workflows')
0071 |     }
0072 |   }
0073 | 
0074 |   async function login(event: FormEvent) {
0075 |     event.preventDefault()
0076 |     if (!supabase) {
0077 |       setError('Configure VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY first.')
0078 |       return
0079 |     }
0080 |     setBusy(true)
0081 |     setError(null)
0082 |     const { error: loginError } = await supabase.auth.signInWithPassword({ email, password })
0083 |     setBusy(false)
0084 |     if (loginError) setError(loginError.message)
0085 |   }
0086 | 
0087 |   function loadBuilder(workflow: WorkflowDetail | null) {
0088 |     setSelected(workflow)
0089 |     setName(workflow?.name ?? '')
0090 |     setEnabled(workflow?.enabled ?? true)
0091 |     setTriggerType(workflow?.trigger.type ?? 'manual')
0092 |     const firstCondition = workflow?.conditions[0] ?? null
0093 |     setCondition(firstCondition)
0094 |     setConditionField(typeof firstCondition?.config.field === 'string' ? firstCondition.config.field : '')
0095 |     setConditionValue(typeof firstCondition?.config.value === 'string' ? firstCondition.config.value : '')
0096 |     const action = workflow?.actions[0] ?? emptyComponent('noop')
0097 |     setActionType(action.type)
0098 |     setActionConfig(JSON.stringify(action.config, null, 2))
0099 |     setGithubToken(typeof action.config.token === 'string' ? action.config.token : '')
0100 |     setGithubRepository(typeof action.config.repository === 'string' ? action.config.repository : '')
0101 |     setGithubEventType(typeof action.config.event_type === 'string' ? action.config.event_type : 'flowforge')
0102 |     setGithubPayload(JSON.stringify(action.config.body ?? {}, null, 2))
0103 |     setEmailTo(Array.isArray(action.config.to) ? action.config.to.filter((item): item is string => typeof item === 'string').join(', ') : '')
0104 |     setEmailSubject(typeof action.config.subject === 'string' ? action.config.subject : '')
0105 |     setEmailText(typeof action.config.text === 'string' ? action.config.text : '')
0106 |     setEmailHtml(typeof action.config.html === 'string' ? action.config.html : '')
0107 |   }
0108 | 
0109 |   async function selectWorkflow(workflow: Workflow) {
0110 |     setError(null)
0111 |     try {
0112 |       const detail = await api.getWorkflow(workflow.id)
0113 |       loadBuilder(detail)
0114 |       setExecutions(await api.executions(workflow.id))
0115 |     } catch (caught) {
0116 |       setError(caught instanceof Error ? caught.message : 'Could not load workflow')
0117 |     }
0118 |   }
0119 | 
0120 |   async function saveWorkflow(event: FormEvent) {
0121 |     event.preventDefault()
0122 |     if (!session?.user.id || !name.trim()) return
0123 |     let parsedAction: Record<string, unknown> = {}
0124 |     if (actionType === 'email') {
0125 |       const recipients = emailTo.split(',').map((item) => item.trim()).filter(Boolean)
0126 |       if (recipients.length === 0 || !emailSubject.trim() || (!emailText.trim() && !emailHtml.trim())) {
0127 |         setError('Email requires recipients, a subject, and text or HTML content')
0128 |         return
0129 |       }
0130 |       parsedAction = {
0131 |         to: recipients,
0132 |         subject: emailSubject.trim(),
0133 |         ...(emailText ? { text: emailText } : {}),
0134 |         ...(emailHtml ? { html: emailHtml } : {}),
0135 |       }
0136 |     } else if (actionType === 'github') {
0137 |       if (!githubToken.trim() || !githubRepository.trim() || !githubEventType.trim()) {
0138 |         setError('GitHub dispatch requires a token, owner/repository, and event type')
0139 |         return
0140 |       }
0141 |       try {
0142 |         const payload: unknown = JSON.parse(githubPayload)
0143 |         if (typeof payload !== 'object' || payload === null || Array.isArray(payload)) {
0144 |           throw new Error('GitHub client payload must be a JSON object')
0145 |         }
0146 |         parsedAction = {
0147 |           token: githubToken.trim(),
0148 |           repository: githubRepository.trim(),
0149 |           event_type: githubEventType.trim(),
0150 |           body: payload,
0151 |         }
0152 |       } catch (caught) {
0153 |         setError(caught instanceof Error ? caught.message : 'Invalid GitHub client payload')
0154 |         return
0155 |       }
0156 |     } else {
0157 |       try {
0158 |         const value: unknown = JSON.parse(actionConfig)
0159 |         if (typeof value !== 'object' || value === null || Array.isArray(value)) throw new Error('Action config must be a JSON object')
0160 |         parsedAction = value as Record<string, unknown>
0161 |       } catch (caught) {
0162 |         setError(caught instanceof Error ? caught.message : 'Invalid action JSON')
0163 |         return
0164 |       }
0165 |     }
0166 |     const conditions = condition
0167 |       ? [{ type: condition.type, config: { field: conditionField, value: conditionValue } }]
0168 |       : []
0169 |     const payload = {
0170 |       name,
0171 |       enabled,
0172 |       trigger: { type: triggerType, config: triggerType === 'webhook' ? { source: 'github' } : {} },
0173 |       conditions,
0174 |       actions: [{ type: actionType, config: parsedAction }],
0175 |     }
0176 |     setBusy(true)
0177 |     setError(null)
0178 |     try {
0179 |       if (selected) {
0180 |         await api.updateWorkflow(selected.id, payload)
0181 |       } else {
0182 |         await api.createWorkflow({ user_id: session.user.id, ...payload })
0183 |       }
0184 |       await refreshWorkflows(session.user.id)
0185 |       setName('')
0186 |       loadBuilder(null)
0187 |     } catch (caught) {
0188 |       setError(caught instanceof Error ? caught.message : 'Could not save workflow')
0189 |     } finally {
0190 |       setBusy(false)
0191 |     }
0192 |   }
0193 | 
0194 |   async function deleteWorkflow() {
0195 |     if (!selected || !window.confirm(`Delete "${selected.name}"?`)) return
0196 |     setBusy(true)
0197 |     try {
0198 |       await api.deleteWorkflow(selected.id)
0199 |       if (session?.user.id) await refreshWorkflows(session.user.id)
0200 |       loadBuilder(null)
0201 |       setExecutions([])
0202 |     } catch (caught) {
0203 |       setError(caught instanceof Error ? caught.message : 'Could not delete workflow')
0204 |     } finally {
0205 |       setBusy(false)
0206 |     }
0207 |   }
0208 | 
0209 |   async function runWorkflow() {
0210 |     if (!selected) return
0211 |     setBusy(true)
0212 |     setError(null)
0213 |     try {
0214 |       await api.runWorkflow(selected.id, { source: 'dashboard' })
0215 |       setExecutions(await api.executions(selected.id))
0216 |     } catch (caught) {
0217 |       setError(caught instanceof Error ? caught.message : 'Could not run workflow')
0218 |     } finally {
0219 |       setBusy(false)
0220 |     }
0221 |   }
0222 | 
0223 |   async function disconnectGmail() {
0224 |     setBusy(true)
0225 |     try {
0226 |       await api.disconnectGmail()
0227 |       setGmail({ connected: false, email: null })
0228 |     } catch (caught) {
0229 |       setError(caught instanceof Error ? caught.message : 'Could not disconnect Gmail')
0230 |     } finally {
0231 |       setBusy(false)
0232 |     }
0233 |   }
0234 | 
0235 |   async function connectGmail() {
0236 |     setBusy(true)
0237 |     setError(null)
0238 |     try {
0239 |       const response = await api.connectGmail()
0240 |       window.location.href = response.authorization_url
0241 |     } catch (caught) {
0242 |       setError(caught instanceof Error ? caught.message : 'Could not start Gmail connection')
0243 |       setBusy(false)
0244 |     }
0245 |   }
0246 | 
0247 |   if (!session) {
0248 |     return (
0249 |       <main className="auth-shell">
0250 |         <section className="card auth-card">
0251 |           <p className="eyebrow">FLOWFORGE</p>
0252 |           <h1>Automate the work between your tools.</h1>
0253 |           <p className="muted">Sign in to configure triggers, conditions, and actions.</p>
0254 |           <form onSubmit={login}>
0255 |             <label>Email<input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required /></label>
0256 |             <label>Password<input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required /></label>
0257 |             <button disabled={busy}>{busy ? 'Signing in…' : 'Sign in'}</button>
0258 |           </form>
0259 |           {error && <p className="error">{error}</p>}
0260 |         </section>
0261 |       </main>
0262 |     )
0263 |   }
0264 | 
0265 |   return (
0266 |     <main className="app-shell">
0267 |       <header className="topbar">
0268 |         <div><p className="eyebrow">FLOWFORGE</p><p className="muted">Workflow operations</p></div>
0269 |         <button className="secondary" onClick={() => void supabase?.auth.signOut()}>Sign out</button>
0270 |       </header>
0271 |       <section className="content">
0272 |         <div className="page-heading"><p className="eyebrow">WORKFLOWS</p><h1>Your automations</h1></div>
0273 |         <section className="card">
0274 |           <div className="detail-heading">
0275 |             <div><h2>Gmail connection</h2><p className="muted">{gmail.connected ? `Connected as ${gmail.email}` : 'Connect Gmail to send email actions from your account.'}</p></div>
0276 |             {gmail.connected ? <button className="secondary" onClick={() => void disconnectGmail()} disabled={busy}>Disconnect</button> : <button onClick={() => void connectGmail()} disabled={busy}>Connect Gmail</button>}
0277 |           </div>
0278 |         </section>
0279 |         <div className="grid">
0280 |           <section className="card">
0281 |             <h2>{selected ? 'Edit workflow' : 'Create workflow'}</h2>
0282 |             <form onSubmit={saveWorkflow}>
0283 |               <label>Name<input value={name} onChange={(event) => setName(event.target.value)} required /></label>
0284 |               <label>Trigger<select value={triggerType} onChange={(event) => setTriggerType(event.target.value)}><option value="manual">Manual</option><option value="webhook">GitHub webhook</option></select></label>
0285 |               {triggerType === 'webhook' && <div className="setup-panel"><strong>Connect GitHub</strong><p className="muted">In the GitHub repository, open Settings → Webhooks → Add webhook.</p><code>{githubWebhookUrl}</code><p className="muted">Use <strong>application/json</strong>, enter the same secret configured as <code>GITHUB_WEBHOOK_SECRET</code> on the backend, and select the events this workflow should inspect.</p></div>}
0286 |               <label className="checkbox"><input type="checkbox" checked={enabled} onChange={(event) => setEnabled(event.target.checked)} /> Enabled</label>
0287 |               <label>Condition<select value={condition?.type ?? ''} onChange={(event) => setCondition(event.target.value ? emptyComponent(event.target.value) : null)}><option value="">No condition</option><option value="equals">Equals</option><option value="contains">Contains</option><option value="not_equals">Not equals</option></select></label>
0288 |               {condition && <div className="two-col"><input placeholder="Payload field" value={conditionField} onChange={(event) => setConditionField(event.target.value)} /><input placeholder="Expected value" value={conditionValue} onChange={(event) => setConditionValue(event.target.value)} /></div>}
0289 |               <label>Action<select value={actionType} onChange={(event) => setActionType(event.target.value)}><option value="noop">No-op</option><option value="http">HTTP request</option><option value="github">GitHub dispatch</option><option value="email">Email</option></select></label>
0290 |               {actionType === 'email' ? <><p className="muted">{gmail.connected ? `Sends from ${gmail.email}` : 'Connect Gmail before running this action.'}</p><label>Recipients (comma-separated)<input type="text" placeholder="you@example.com" value={emailTo} onChange={(event) => setEmailTo(event.target.value)} /></label><label>Subject<input type="text" value={emailSubject} onChange={(event) => setEmailSubject(event.target.value)} /></label><label>Text body<textarea rows={4} value={emailText} onChange={(event) => setEmailText(event.target.value)} /></label><label>HTML body (optional)<textarea rows={4} value={emailHtml} onChange={(event) => setEmailHtml(event.target.value)} /></label></> : actionType === 'github' ? <><p className="muted">FlowForge sends a <code>repository_dispatch</code> event to GitHub. Use a fine-grained token with Contents: Read and write on the target repository.</p><label>GitHub token<input type="password" value={githubToken} onChange={(event) => setGithubToken(event.target.value)} autoComplete="off" /></label><label>Repository<input placeholder="owner/repository" value={githubRepository} onChange={(event) => setGithubRepository(event.target.value)} /></label><label>Event type<input value={githubEventType} onChange={(event) => setGithubEventType(event.target.value)} /></label><label>Client payload (JSON)<textarea rows={5} value={githubPayload} onChange={(event) => setGithubPayload(event.target.value)} /></label></> : actionType !== 'noop' && <label>Action configuration (JSON)<textarea rows={5} value={actionConfig} onChange={(event) => setActionConfig(event.target.value)} /></label>}
0291 |               <div className="button-row"><button disabled={busy}>{busy ? 'Saving…' : selected ? 'Save changes' : 'Create workflow'}</button>{selected && <><button type="button" className="secondary" onClick={() => loadBuilder(null)}>Cancel</button><button type="button" className="danger" onClick={() => void deleteWorkflow()}>Delete</button></>}</div>
0292 |             </form>
0293 |             <div className="workflow-list">
0294 |               {workflows.length === 0 && <p className="muted">No workflows yet.</p>}
0295 |               {workflows.map((workflow) => <button className={`workflow-row ${selected?.id === workflow.id ? 'selected' : ''}`} key={workflow.id} onClick={() => void selectWorkflow(workflow)}><span>{workflow.name}</span><span className="status">{workflow.enabled ? 'ACTIVE' : 'DRAFT'}</span></button>)}
0296 |             </div>
0297 |           </section>
0298 |           <section className="card">
0299 |             <div className="detail-heading"><div><h2>{selected?.name ?? 'Select a workflow'}</h2><p className="muted">{selected ? `${selected.trigger.type} trigger · ${selected.actions[0]?.type ?? 'No'} action` : 'Configure a workflow to inspect it.'}</p></div>{selected && <button onClick={() => void runWorkflow()} disabled={busy}>Run now</button>}</div>
0300 |             <h3>Execution history</h3>
0301 |             {!selected && <p className="muted">Choose a workflow to inspect its runs.</p>}
0302 |             {selected && executions.length === 0 && <p className="muted">No executions recorded.</p>}
0303 |             {executions.map((execution) => <div className="execution-row" key={execution.id}><div><strong>{execution.status}</strong>{execution.error && <p className="execution-error">{execution.error}</p>}</div><code>{execution.id.slice(0, 8)}</code></div>)}
0304 |           </section>
0305 |         </div>
0306 |         {error && <p className="error">{error}</p>}
0307 |       </section>
0308 |     </main>
0309 |   )
0310 | }
0311 | 
0312 | export default App
```

### Every-line explanation

**L0001.** Import the two React hooks used for state and lifecycle synchronization.

**L0002.** Import only FormEvent's TypeScript type; it is erased from runtime output.

**L0003.** Import the Supabase session type, distinct from a SQLAlchemy database Session.

**L0004.** Import the shared endpoint client rather than repeating fetch wiring in each handler.

**L0005.** Import domain/API types for compile-time checking; they do not validate server JSON at runtime.

**L0006.** Import the nullable configured Supabase client.

**L0007.** Blank line: separates related declarations/statements; no runtime operation.

**L0008.** Arrow function returns a fresh configuration object; parentheses around the object distinguish it from a function block. The return type is the local Component type, not a React component.

**L0009.** Read the public Vite API URL and fall back only for null/undefined; an empty string is preserved by ??.

**L0010.** Remove one trailing slash with a regex and append the GitHub webhook route for setup instructions.

**L0011.** Blank line: separates related declarations/statements; no runtime operation.

**L0012.** Define the React function component. Its function body runs on each render; hooks preserve their own state between renders.

**L0013.** Create React state `session` for Supabase identity/session or null before sign-in/session loading; destructuring also names its setter `setSession`. `useState<Session | null>(null)` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0014.** Create React state `email` for login email text; destructuring also names its setter `setEmail`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0015.** Create React state `password` for login password text held in browser state; destructuring also names its setter `setPassword`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0016.** Create React state `workflows` for saved workflow summaries; destructuring also names its setter `setWorkflows`. `useState<Workflow[]>([])` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0017.** Create React state `selected` for full selected workflow or null for creation mode; destructuring also names its setter `setSelected`. `useState<WorkflowDetail | null>(null)` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0018.** Create React state `executions` for selected workflow's persisted history; destructuring also names its setter `setExecutions`. `useState<Execution[]>([])` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0019.** Create React state `name` for builder workflow name; destructuring also names its setter `setName`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0020.** Create React state `triggerType` for builder trigger discriminator; destructuring also names its setter `setTriggerType`. `useState('manual')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0021.** Create React state `condition` for optional builder condition configuration; destructuring also names its setter `setCondition`. `useState<Component | null>(null)` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0022.** Create React state `conditionField` for top-level payload/context key; destructuring also names its setter `setConditionField`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0023.** Create React state `conditionValue` for string expected condition value; destructuring also names its setter `setConditionValue`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0024.** Create React state `actionType` for builder action discriminator; destructuring also names its setter `setActionType`. `useState('noop')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0025.** Create React state `actionConfig` for generic action config as editable JSON text; destructuring also names its setter `setActionConfig`. `useState('{}')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0026.** Create React state `githubToken` for GitHub credential input, masked only by input presentation; destructuring also names its setter `setGithubToken`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0027.** Create React state `githubRepository` for target owner/repository; destructuring also names its setter `setGithubRepository`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0028.** Create React state `githubEventType` for repository dispatch event discriminator; destructuring also names its setter `setGithubEventType`. `useState('flowforge')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0029.** Create React state `githubPayload` for client payload as JSON text; destructuring also names its setter `setGithubPayload`. `useState('{}')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0030.** Create React state `emailTo` for comma-separated recipient input; destructuring also names its setter `setEmailTo`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0031.** Create React state `emailSubject` for email subject input; destructuring also names its setter `setEmailSubject`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0032.** Create React state `emailText` for plain text email input; destructuring also names its setter `setEmailText`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0033.** Create React state `emailHtml` for optional HTML email input; destructuring also names its setter `setEmailHtml`. `useState('')` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0034.** Create React state `enabled` for whether the saved workflow may execute; destructuring also names its setter `setEnabled`. `useState(true)` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0035.** Create React state `error` for displayed request/UI error or null; destructuring also names its setter `setError`. `useState<string | null>(null)` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0036.** Create React state `busy` for whether a UI operation is in progress; destructuring also names its setter `setBusy`. `useState(false)` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0037.** Create React state `gmail` for Gmail connection status and email only, without OAuth token values; destructuring also names its setter `setGmail`. `useState<GmailStatus>({ connected: false, email: null })` declares initial state and any explicit generic type. Calling the setter requests another render.

**L0038.** Blank line: separates related declarations/statements; no runtime operation.

**L0039.** Register the session synchronization effect. Its callback runs after React commits the component, with development StrictMode checks possible.

**L0040.** If no Supabase client was configured, finish effect setup immediately.

**L0041.** Request the SDK session asynchronously; destructure data from its result and update React session state. void discards the promise value, not its work.

**L0042.** Subscribe to auth changes. The unused event argument is prefixed with an underscore; the callback installs the new session in state.

**L0043.** Return an effect cleanup function to unsubscribe, avoiding stale auth subscriptions.

**L0044.** End the effect with an empty dependency array: no state dependency reruns it during ordinary updates; StrictMode may still test setup/cleanup in development.

**L0045.** Blank line: separates related declarations/statements; no runtime operation.

**L0046.** Register a mount-time effect that interprets query parameters after an OAuth redirect.

**L0047.** Construct the browser query parser from the current URL's search component.

**L0048.** Read the gmail outcome parameter; missing query values are null.

**L0049.** Read optional provider error detail from the URL.

**L0050.** Only the error outcome enters this branch.

**L0051.** Display supplied detail or a reason-based fallback. This direct state update inside the effect is the reported lint warning.

**L0052.** Replace the current history URL without navigating, removing callback query parameters from the visible URL.

**L0053.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0054.** End the callback-query effect; empty dependencies make it mount-oriented.

**L0055.** Blank line: separates related declarations/statements; no runtime operation.

**L0056.** Start an effect synchronizing the workflow list with the signed-in user ID.

**L0057.** Only refresh when an authenticated user ID exists; the async helper handles its own errors.

**L0058.** Rerun when the user ID changes, rather than whenever every session object reference changes.

**L0059.** Blank line: separates related declarations/statements; no runtime operation.

**L0060.** Start a separate user-dependent Gmail status synchronization effect.

**L0061.** Do not request Gmail connection status without a signed-in user.

**L0062.** Fetch status, pass success directly to the state setter, and fall back to disconnected on failure; this path intentionally hides the specific status error.

**L0063.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0064.** Depend on user ID so status refreshes when identities change.

**L0065.** Blank line: separates related declarations/statements; no runtime operation.

**L0066.** Define an async list-refresh helper; parameter type is string and its inferred return is a Promise.

**L0067.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0068.** Await the API list and replace workflows state with the returned summaries.

**L0069.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0070.** Narrow the caught value with instanceof Error before reading message, otherwise use a safe fallback.

**L0071.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0072.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0073.** Blank line: separates related declarations/statements; no runtime operation.

**L0074.** Define the form submit handler with React's FormEvent type.

**L0075.** Prevent the browser's normal form navigation/reload.

**L0076.** Guard against missing public authentication configuration.

**L0077.** Show an actionable configuration message without printing any key value.

**L0078.** Exit this handler without saving/executing the remaining operations.

**L0079.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0080.** Mark the UI busy, disabling relevant buttons on the next render.

**L0081.** Clear the previously displayed error.

**L0082.** Send email/password to Supabase's authentication client and rename its returned error field to loginError.

**L0083.** Clear the busy state after the awaited login response. This handler does not wrap the await in try/finally for unexpected rejections.

**L0084.** Show the SDK-reported login error, if one was returned.

**L0085.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0086.** Blank line: separates related declarations/statements; no runtime operation.

**L0087.** Load a detailed workflow into builder state, or reset the builder when passed null.

**L0088.** Store the selected detail object; selection controls edit mode and Run now.

**L0089.** Load name, defaulting to an empty string only when selection/name is nullish.

**L0090.** Load enabled while preserving a real false; ?? avoids replacing false with true.

**L0091.** Use the saved trigger type, or manual as the new-workflow default.

**L0092.** Take only the first condition. Additional backend conditions are not represented by this editor.

**L0093.** Update the optional condition selection.

**L0094.** Read config.field only if it is a string; unknown config requires runtime narrowing.

**L0095.** Read config.value only if it is a string. Numeric/boolean API condition values are not round-tripped faithfully here.

**L0096.** Take only the first action or a newly allocated no-op config. Saving an API-created multi-action workflow through this editor can discard extra actions.

**L0097.** Load the action discriminator used by conditional form rendering.

**L0098.** Pretty-print config with two-space JSON indentation for the generic configuration textarea.

**L0099.** Populate the GitHub password input from stored config when it is a string; masking does not mean the API redacted/encrypted it.

**L0100.** Load the target owner/repository string after type checking.

**L0101.** Load the event type or default flowforge; this must match a target repository workflow listener.

**L0102.** Pretty-print client payload, defaulting nullish body to a fresh empty object for display.

**L0103.** If recipients are an array, use a type-predicate filter to keep strings and join them for the comma-separated input. A single string config is not loaded into this input by this expression.

**L0104.** Load an email subject only when its config value is a string.

**L0105.** Load the plain text email body after type narrowing.

**L0106.** Load optional HTML after type narrowing.

**L0107.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0108.** Blank line: separates related declarations/statements; no runtime operation.

**L0109.** Define selection handling for a summary row; summary lacks full component config.

**L0110.** Clear an old error before loading the selected workflow.

**L0111.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0112.** Fetch full detail using the summary's ID.

**L0113.** Populate editor state from the fetched detail.

**L0114.** Fetch and display the selected workflow's persisted executions. This is a request, not a real-time subscription.

**L0115.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0116.** Show either the caught Error message or a selection-specific fallback.

**L0117.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0118.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0119.** Blank line: separates related declarations/statements; no runtime operation.

**L0120.** Define the create/update form handler; its behavior depends on whether selected is null.

**L0121.** Stop native form navigation so saving stays within the SPA.

**L0122.** Exit for missing identity or a blank trimmed name. The payload later uses the original name string rather than the trimmed one.

**L0123.** Declare a mutable local object whose values remain unknown until action-specific checks narrow them.

**L0124.** Choose dedicated email-field validation and configuration.

**L0125.** Split at commas, trim whitespace, and remove empty recipients with filter(Boolean). This is formatting; the backend validates addresses too.

**L0126.** Require recipients, a nonblank subject, and at least one nonblank text/HTML body in the UI.

**L0127.** Report the email validation requirement and leave the workflow unsaved.

**L0128.** Exit this handler without saving/executing the remaining operations.

**L0129.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0130.** Begin construction of the email action config object.

**L0131.** Store the normalized recipients array under the provider-independent to key.

**L0132.** Save the trimmed subject.

**L0133.** Conditionally spread a text property only if emailText is truthy.

**L0134.** Conditionally spread an html property only if emailHtml is truthy.

**L0135.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0136.** Choose GitHub-specific validation rather than the generic JSON textarea.

**L0137.** Require nonblank token, repository, and event type before attempting save.

**L0138.** Show the missing GitHub configuration error.

**L0139.** Exit this handler without saving/executing the remaining operations.

**L0140.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0141.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0142.** Parse the client payload string but assign the result to unknown so its shape must be checked.

**L0143.** Require a non-null, non-array object. JavaScript's typeof null is object, so the explicit null check matters.

**L0144.** Throw a local validation error that the surrounding catch will display.

**L0145.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0146.** Begin the dedicated GitHub config object.

**L0147.** Store the trimmed token in config. This MVP later persists it as ordinary JSON.

**L0148.** Store the trimmed owner/repository value.

**L0149.** Store the trimmed dispatch event type.

**L0150.** Use the validated object as client_payload data through the GitHub action's body setting.

**L0151.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0152.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0153.** Display JSON parse/shape error with a GitHub-specific fallback.

**L0154.** Exit this handler without saving/executing the remaining operations.

**L0155.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0156.** For no-op or generic HTTP, parse the generic action configuration string.

**L0157.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0158.** Parse user-entered JSON and keep its type unknown until the following guard.

**L0159.** Reject primitives, null, and arrays as the top-level configuration value.

**L0160.** Assert the checked object shape for TypeScript. The as assertion itself adds no runtime check.

**L0161.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0162.** Display parse/shape errors and avoid sending malformed config to the API.

**L0163.** Exit this handler without saving/executing the remaining operations.

**L0164.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0165.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0166.** Build the condition array from whether a condition is selected.

**L0167.** Create exactly one condition with a string expected value when enabled in this UI.

**L0168.** Otherwise send an empty condition array, meaning no condition gate.

**L0169.** Begin the workflow payload object shared by create and update.

**L0170.** Use object-property shorthand to include name state.

**L0171.** Include the enabled boolean state.

**L0172.** For a webhook trigger, restrict source to github; manual config is empty.

**L0173.** Include the just-constructed zero/one condition array.

**L0174.** Include exactly one action configuration; backend multiple-action capability is not exposed here.

**L0175.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0176.** Set busy before the save request to prevent ordinary duplicate button submissions.

**L0177.** Clear old errors before calling the backend.

**L0178.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0179.** A selected workflow means replacement update rather than creation.

**L0180.** Send PUT through the API wrapper for the selected ID.

**L0181.** Continue the surrounding typed module/configuration expression: `} else {`. The exact operation is introduced by the preceding function/object declaration; punctuation preserves that grouping.

**L0182.** For creation, add authenticated user_id and spread the common payload into a new object.

**L0183.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0184.** Refresh the user's list after a successful save.

**L0185.** Clear name state (loadBuilder(null) below also resets it).

**L0186.** Reset the selection/builder to new-workflow mode.

**L0187.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0188.** Display a save-specific error without throwing through the UI event callback.

**L0189.** Finally executes whether save succeeded or failed.

**L0190.** Clear busy so controls are usable again.

**L0191.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0192.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0193.** Blank line: separates related declarations/statements; no runtime operation.

**L0194.** Define the async workflow-deletion event operation.

**L0195.** Exit when no selection exists or the user declines the browser confirmation. Template interpolation shows the workflow name.

**L0196.** Mark deletion busy.

**L0197.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0198.** Request deletion of the selected workflow and its configured ORM dependents.

**L0199.** Refresh the list only if an identity is still present.

**L0200.** Clear the selection and reset editor defaults.

**L0201.** Clear history that belonged to the deleted workflow.

**L0202.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0203.** Show deletion errors.

**L0204.** Begin unconditional cleanup, used to clear busy after either success or error.

**L0205.** Always clear deletion's busy state.

**L0206.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0207.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0208.** Blank line: separates related declarations/statements; no runtime operation.

**L0209.** Define the manual-run event handler.

**L0210.** Ignore a run request if no workflow is selected.

**L0211.** Mark run busy to disable ordinary repeat clicks.

**L0212.** Clear an old error before executing.

**L0213.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0214.** Send payload.source=dashboard. The backend separately sets the normalized Event type/source to manual.

**L0215.** Reload persisted history after the run response. It is not continuously refreshed for external webhooks.

**L0216.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0217.** Display request-level run errors; FAILED/SKIPPED can still arrive in an HTTP-successful execution response.

**L0218.** Begin unconditional cleanup, used to clear busy after either success or error.

**L0219.** Clear busy even if the request/history refresh fails.

**L0220.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0221.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0222.** Blank line: separates related declarations/statements; no runtime operation.

**L0223.** Define Gmail disconnect handling.

**L0224.** Mark disconnect busy.

**L0225.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0226.** Ask the backend to delete the current user's stored Gmail connection.

**L0227.** Update the UI to disconnected with no email. This does not revoke provider consent.

**L0228.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0229.** Display disconnect errors.

**L0230.** Begin unconditional cleanup, used to clear busy after either success or error.

**L0231.** Always clear disconnect's busy state.

**L0232.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0233.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0234.** Blank line: separates related declarations/statements; no runtime operation.

**L0235.** Define Gmail authorization initiation.

**L0236.** Mark connection startup busy.

**L0237.** Clear an old error before initiating OAuth.

**L0238.** Begin a block whose thrown errors/rejected awaits are handled by the following catch/finally.

**L0239.** Ask the backend for an authorization URL tied to a stored state and the authenticated user.

**L0240.** Navigate the browser to Google consent. This intentionally leaves the FlowForge page.

**L0241.** End the protected body and catch a thrown/rejected value as caught; subsequent instanceof checks narrow it safely.

**L0242.** Display startup errors if the backend cannot prepare the flow.

**L0243.** Clear busy on failure; on success navigation takes over instead of a finally reset.

**L0244.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0245.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0246.** Blank line: separates related declarations/statements; no runtime operation.

**L0247.** Without an established session, render the sign-in branch rather than the dashboard.

**L0248.** Return begins the sign-in JSX expression; returning ends this render branch.

**L0249.** Semantic main region with a CSS class for centered authentication layout.

**L0250.** Card section for the login content; className is JSX's class attribute spelling.

**L0251.** Brand text; it is static UI content, not a backend operation.

**L0252.** Static introductory heading inside the auth card.

**L0253.** Instructional copy describing sign-in's purpose.

**L0254.** Form submits through the login function; passing the function does not execute it during render.

**L0255.** Controlled required email input. onChange copies the browser field value into email state; type=email adds browser-level validation hints.

**L0256.** Controlled required password input. type=password masks display but does not encrypt state.

**L0257.** Default submit button is disabled while busy and uses a ternary label.

**L0258.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0259.** Short-circuit rendering shows the error paragraph only for a truthy error value. React escapes the interpolated text.

**L0260.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0261.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0262.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0263.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0264.** Blank line: separates related declarations/statements; no runtime operation.

**L0265.** Return the signed-in dashboard's JSX tree.

**L0266.** Semantic app main region; max width/layout comes from active CSS.

**L0267.** Header region groups branding and sign-out control.

**L0268.** Static brand and description in a grouping div.

**L0269.** Pass a click callback that invokes optional Supabase signOut; void discards its promise value. There is no explicit rejection display in this handler.

**L0270.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0271.** Start the main content section.

**L0272.** Display workflow heading and eyebrow label.

**L0273.** Start the Gmail connection card.

**L0274.** Flex header layout for connection text and controls.

**L0275.** Choose connected email text or instructions with a ternary expression.

**L0276.** Render the relevant Connect/Disconnect button based on gmail.connected; callbacks defer execution until clicked and busy disables them.

**L0277.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0278.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0279.** Start the CSS grid holding builder/list and selected workflow history.

**L0280.** Start the workflow builder card.

**L0281.** Choose Edit workflow versus Create workflow according to selected.

**L0282.** Bind form submission to saveWorkflow.

**L0283.** Controlled required name input.

**L0284.** Controlled select exposes Manual and GitHub webhook only. ScheduledTrigger exists in the backend but is absent here.

**L0285.** Only for webhook type, render setup instructions and the computed URL. Displaying a secret variable's name is not revealing its value.

**L0286.** Controlled boolean checkbox uses checked and event.target.checked rather than value.

**L0287.** Controlled condition select supports none/equals/contains/not-equal. Selection constructs a fresh Component or null; ?? preserves valid non-null strings.

**L0288.** Only render field/value inputs when a condition exists. Both values are strings; no numeric/group editor is provided.

**L0289.** Controlled action select exposes no-op, HTTP, GitHub dispatch, and email.

**L0290.** Nested JSX ternaries render provider-specific fields: email recipient/content controls, GitHub token/repository/event/payload controls, or generic HTTP JSON. Fragments group fields without extra wrappers; each input is controlled. A password field only masks the GitHub token visually.

**L0291.** Submit saves; Cancel/Delete explicitly use type=button so they do not submit. Optional edit controls render inside a Fragment. Busy changes submit label and disables it.

**L0292.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0293.** Container for saved workflow summary buttons.

**L0294.** Show an empty-state message when the list is empty.

**L0295.** Map summaries to buttons with stable ID keys. A template string adds selected CSS styling; click fetches detail/history; the label shows ACTIVE/DRAFT from enabled.

**L0296.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0297.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0298.** Start selected workflow detail/history card.

**L0299.** Use optional chaining and nullish fallbacks for heading/action description. Show Run now only if selected; its callback requests backend manual execution.

**L0300.** Static execution history subheading.

**L0301.** Show selection instructions only when no workflow is selected.

**L0302.** If selected but history is empty, show a no-executions message.

**L0303.** Map execution rows using stable IDs; display status, optional stored error, and an eight-character ID preview. This does not show provider action_results because those are not persisted by the service.

**L0304.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0305.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0306.** Show request/UI errors below the dashboard. This message is distinct from each execution's stored error.

**L0307.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0308.** Close the JSX element named here; this completes UI nesting, not an HTTP/backend operation.

**L0309.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0310.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0311.** Blank line: separates related declarations/statements; no runtime operation.

**L0312.** Export App as this module's default so main.tsx can import it without braces.


<a id="frontend-src-indexcss"></a>
## frontend/src/index.css

Active product styling imported by main.tsx. Plain CSS implements cards, forms, grid/flex layout, status/errors, and a narrow-screen breakpoint at 720 CSS pixels. Naming Inter does not itself download the font.

Source fingerprint: `29d66563beffe264afeab0e54f256d01b471683f0e3932af41177d4e5c9a1ed7`. Physical lines: 35.

### Numbered source

```css
0001 | :root { font-family: Inter, ui-sans-serif, system-ui, sans-serif; color: #172033; background: #f5f7fb; font-synthesis: none; text-rendering: optimizeLegibility; }
0002 | * { box-sizing: border-box; }
0003 | body { margin: 0; min-width: 320px; }
0004 | button, input, select, textarea { font: inherit; }
0005 | button { border: 0; border-radius: 8px; padding: 10px 16px; color: #fff; background: #2563eb; cursor: pointer; }
0006 | button:disabled { opacity: .6; cursor: wait; }
0007 | select, textarea { width: 100%; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 12px; color: #172033; background: #fff; }
0008 | button.secondary { color: #334155; background: #e8edf5; }
0009 | .auth-shell, .app-shell { min-height: 100vh; }
0010 | .auth-shell { display: grid; place-items: center; padding: 24px; }
0011 | .app-shell { max-width: 1180px; margin: auto; }
0012 | .topbar, .content { padding: 28px 32px; }
0013 | .topbar { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; }
0014 | .page-heading { margin: 26px 0; }
0015 | .card { background: #fff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 24px; box-shadow: 0 8px 24px #1e293b0a; }
0016 | .auth-card { width: min(440px, 100%); }
0017 | .auth-card h1 { font-size: 32px; line-height: 1.15; margin: 8px 0 12px; }
0018 | h1, h2, h3 { margin-top: 0; } h2 { font-size: 20px; } h3 { margin: 26px 0 12px; font-size: 14px; text-transform: uppercase; letter-spacing: .08em; color: #64748b; }
0019 | .eyebrow { margin: 0; color: #2563eb; font-weight: 800; letter-spacing: .12em; font-size: 12px; }
0020 | .muted { color: #64748b; }
0021 | .error { color: #b42318; background: #fff1f0; border-radius: 8px; padding: 10px 12px; }
0022 | form { display: grid; gap: 14px; margin-top: 24px; } label { display: grid; gap: 6px; font-size: 14px; color: #475569; } input { width: 100%; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 12px; color: #172033; background: #fff; }
0023 | .grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr); gap: 20px; }
0024 | .inline-form { display: flex; margin: 14px 0 20px; } .inline-form input { flex: 1; margin-right: 8px; }
0025 | .checkbox { display: flex; grid-template-columns: auto 1fr; align-items: center; gap: 8px; } .checkbox input { width: auto; }
0026 | .two-col, .button-row { display: flex; gap: 8px; } .two-col > * { flex: 1; } .button-row { flex-wrap: wrap; }
0027 | .danger { background: #b42318; }
0028 | .workflow-list { display: grid; gap: 8px; } .workflow-row { display: flex; justify-content: space-between; text-align: left; color: #172033; background: #f8fafc; } .workflow-row.selected { outline: 2px solid #93c5fd; }
0029 | .status { color: #15803d; font-size: 11px; font-weight: 700; } .detail-heading { display: flex; justify-content: space-between; gap: 12px; align-items: start; }
0030 | .execution-row { display: flex; justify-content: space-between; padding: 12px 0; border-top: 1px solid #e2e8f0; } code { color: #475569; }
0031 | .execution-error { margin: 4px 0 0; color: #b42318; font-size: 13px; }
0032 | .setup-panel { display: grid; gap: 8px; padding: 14px; border: 1px solid #bfdbfe; border-radius: 10px; background: #eff6ff; color: #1e3a8a; }
0033 | .setup-panel p { margin: 0; }
0034 | .setup-panel code { overflow-wrap: anywhere; }
0035 | @media (max-width: 720px) { .topbar, .content { padding: 20px 16px; } .grid { grid-template-columns: 1fr; } .detail-heading { flex-direction: column; } }
```

### Every-line explanation

**L0001.** Selector `:root ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `font-family: Inter, ui-sans-serif, system-ui, sans-serif`: choose an ordered font fallback stack; listing a font does not download it; `color: #172033`: set foreground/text color; `background: #f5f7fb`: set background shorthand; `font-synthesis: none`: control whether the browser synthesizes missing font styles; `text-rendering: optimizeLegibility`: provide text rendering hints.

**L0002.** Selector `* ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `box-sizing: border-box`: choose whether declared dimensions include border/padding.

**L0003.** Selector `body ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `margin: 0`: set outer spacing (one to four sides or auto centering); `min-width: 320px`: set a lower bound on width.

**L0004.** Selector `button, input, select, textarea ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `font: inherit`: inherit or set the composite font style.

**L0005.** Selector `button ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `border: 0`: set border width/style/color; `border-radius: 8px`: round the corners; `padding: 10px 16px`: set internal spacing; `color: #fff`: set foreground/text color; `background: #2563eb`: set background shorthand; `cursor: pointer`: select pointer feedback.

**L0006.** Selector `button:disabled ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `opacity: .6`: set overall transparency; `cursor: wait`: select pointer feedback.

**L0007.** Selector `select, textarea ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `width: 100%`: set element width; `border: 1px solid #cbd5e1`: set border width/style/color; `border-radius: 8px`: round the corners; `padding: 10px 12px`: set internal spacing; `color: #172033`: set foreground/text color; `background: #fff`: set background shorthand.

**L0008.** Selector `button.secondary ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `color: #334155`: set foreground/text color; `background: #e8edf5`: set background shorthand.

**L0009.** Selector `.auth-shell, .app-shell ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `min-height: 100vh`: set a lower bound on height.

**L0010.** Selector `.auth-shell ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: grid`: choose grid/flex/block display behavior; `place-items: center`: align items in both relevant axes; `padding: 24px`: set internal spacing.

**L0011.** Selector `.app-shell ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `max-width: 1180px`: cap element width; `margin: auto`: set outer spacing (one to four sides or auto centering).

**L0012.** Selector `.topbar, .content ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `padding: 28px 32px`: set internal spacing.

**L0013.** Selector `.topbar ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: flex`: choose grid/flex/block display behavior; `justify-content: space-between`: distribute/align items along the layout's main/inline axis; `align-items: center`: align items on the cross/block axis; `border-bottom: 1px solid #e2e8f0`: set the lower border.

**L0014.** Selector `.page-heading ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `margin: 26px 0`: set outer spacing (one to four sides or auto centering).

**L0015.** Selector `.card ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `background: #fff`: set background shorthand; `border: 1px solid #e2e8f0`: set border width/style/color; `border-radius: 14px`: round the corners; `padding: 24px`: set internal spacing; `box-shadow: 0 8px 24px #1e293b0a`: draw an outer shadow without changing layout dimensions.

**L0016.** Selector `.auth-card ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `width: min(440px, 100%)`: set element width.

**L0017.** Selector `.auth-card h1 ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `font-size: 32px`: set text size; `line-height: 1.15`: set spacing/height of text lines; `margin: 8px 0 12px`: set outer spacing (one to four sides or auto centering).

**L0018.** Selector `h1, h2, h3 ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `margin-top: 0`: set space above; `font-size: 20px`: set text size; `margin: 26px 0 12px`: set outer spacing (one to four sides or auto centering); `font-size: 14px`: set text size; `text-transform: uppercase`: change displayed capitalization; `letter-spacing: .08em`: set spacing between characters; `color: #64748b`: set foreground/text color.

**L0019.** Selector `.eyebrow ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `margin: 0`: set outer spacing (one to four sides or auto centering); `color: #2563eb`: set foreground/text color; `font-weight: 800`: select font weight; `letter-spacing: .12em`: set spacing between characters; `font-size: 12px`: set text size.

**L0020.** Selector `.muted ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `color: #64748b`: set foreground/text color.

**L0021.** Selector `.error ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `color: #b42318`: set foreground/text color; `background: #fff1f0`: set background shorthand; `border-radius: 8px`: round the corners; `padding: 10px 12px`: set internal spacing.

**L0022.** Selector `form ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: grid`: choose grid/flex/block display behavior; `gap: 14px`: set space between grid/flex items; `margin-top: 24px`: set space above; `display: grid`: choose grid/flex/block display behavior; `gap: 6px`: set space between grid/flex items; `font-size: 14px`: set text size; `color: #475569`: set foreground/text color; `width: 100%`: set element width; `border: 1px solid #cbd5e1`: set border width/style/color; `border-radius: 8px`: round the corners; `padding: 10px 12px`: set internal spacing; `color: #172033`: set foreground/text color; `background: #fff`: set background shorthand.

**L0023.** Selector `.grid ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: grid`: choose grid/flex/block display behavior; `grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr)`: define grid column tracks; `gap: 20px`: set space between grid/flex items.

**L0024.** Selector `.inline-form ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: flex`: choose grid/flex/block display behavior; `margin: 14px 0 20px`: set outer spacing (one to four sides or auto centering); `flex: 1`: set the grow/shrink/basis shorthand; `margin-right: 8px`: set space to the right.

**L0025.** Selector `.checkbox ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: flex`: choose grid/flex/block display behavior; `grid-template-columns: auto 1fr`: define grid column tracks; `align-items: center`: align items on the cross/block axis; `gap: 8px`: set space between grid/flex items; `width: auto`: set element width.

**L0026.** Selector `.two-col, .button-row ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: flex`: choose grid/flex/block display behavior; `gap: 8px`: set space between grid/flex items; `flex: 1`: set the grow/shrink/basis shorthand; `flex-wrap: wrap`: allow flex items to wrap.

**L0027.** Selector `.danger ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `background: #b42318`: set background shorthand.

**L0028.** Selector `.workflow-list ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: grid`: choose grid/flex/block display behavior; `gap: 8px`: set space between grid/flex items; `display: flex`: choose grid/flex/block display behavior; `justify-content: space-between`: distribute/align items along the layout's main/inline axis; `text-align: left`: align inline text inside its box; `color: #172033`: set foreground/text color; `background: #f8fafc`: set background shorthand; `outline: 2px solid #93c5fd`: draw a focus/selection outline outside the border.

**L0029.** Selector `.status ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `color: #15803d`: set foreground/text color; `font-size: 11px`: set text size; `font-weight: 700`: select font weight; `display: flex`: choose grid/flex/block display behavior; `justify-content: space-between`: distribute/align items along the layout's main/inline axis; `gap: 12px`: set space between grid/flex items; `align-items: start`: align items on the cross/block axis.

**L0030.** Selector `.execution-row ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: flex`: choose grid/flex/block display behavior; `justify-content: space-between`: distribute/align items along the layout's main/inline axis; `padding: 12px 0`: set internal spacing; `border-top: 1px solid #e2e8f0`: set the upper border; `color: #475569`: set foreground/text color.

**L0031.** Selector `.execution-error ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `margin: 4px 0 0`: set outer spacing (one to four sides or auto centering); `color: #b42318`: set foreground/text color; `font-size: 13px`: set text size.

**L0032.** Selector `.setup-panel ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `display: grid`: choose grid/flex/block display behavior; `gap: 8px`: set space between grid/flex items; `padding: 14px`: set internal spacing; `border: 1px solid #bfdbfe`: set border width/style/color; `border-radius: 10px`: round the corners; `background: #eff6ff`: set background shorthand; `color: #1e3a8a`: set foreground/text color.

**L0033.** Selector `.setup-panel p ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `margin: 0`: set outer spacing (one to four sides or auto centering).

**L0034.** Selector `.setup-panel code ` starts a style rule. `.` names a class, `#` an ID, `:` a pseudo-class, `::` a pseudo-element, `&` a nested parent reference, and commas combine selector alternatives where present. `overflow-wrap: anywhere`: allow long text such as URLs to break.

**L0035.** Apply the enclosed rules only when the viewport matches the shown maximum CSS-pixel width. `padding: 20px 16px`: set internal spacing; `grid-template-columns: 1fr`: define grid column tracks; `flex-direction: column`: choose row/column flow.


<a id="frontend-src-lib-supabasets"></a>
## frontend/src/lib/supabase.ts

Creates a browser Supabase client only when public URL/key values exist. VITE_ values are build-time public configuration; no backend secret belongs here.

Source fingerprint: `404f0a52451d908fb907b5c261fe042559a4b42515816256aa13d30b8d1ab373`. Physical lines: 6.

### Numbered source

```typescript
0001 | import { createClient } from '@supabase/supabase-js'
0002 | 
0003 | const url = import.meta.env.VITE_SUPABASE_URL
0004 | const key = import.meta.env.VITE_SUPABASE_ANON_KEY
0005 | 
0006 | export const supabase = url && key ? createClient(url, key) : null
```

### Every-line explanation

**L0001.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0002.** Blank line: separates related declarations/statements; no runtime operation.

**L0003.** Read the public Supabase URL embedded by Vite from exposed build environment.

**L0004.** Read the public Supabase anonymous/publishable key; a privileged service-role key must never be used here.

**L0005.** Blank line: separates related declarations/statements; no runtime operation.

**L0006.** Export a real client only when both values are truthy; otherwise export null so callers can guard missing configuration.


<a id="frontend-src-maintsx"></a>
## frontend/src/main.tsx

Browser entry point. Imports the active index.css, finds the root element, and renders App in development StrictMode. The non-null assertion is erased and does not check root existence at runtime.

Source fingerprint: `484f93f3048565a86a47e308f5a12ee27aa12f5291f3b52a4bb5dc03d887dbc7`. Physical lines: 10.

### Numbered source

```tsx
0001 | import { StrictMode } from 'react'
0002 | import { createRoot } from 'react-dom/client'
0003 | import './index.css'
0004 | import App from './App.tsx'
0005 | 
0006 | createRoot(document.getElementById('root')!).render(
0007 |   <StrictMode>
0008 |     <App />
0009 |   </StrictMode>,
0010 | )
```

### Every-line explanation

**L0001.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0002.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0003.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0004.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0005.** Blank line: separates related declarations/statements; no runtime operation.

**L0006.** Find the HTML root and create a React DOM root, then call render. `!` is a non-null assertion, not a runtime existence check.

**L0007.** Wrap descendants in StrictMode for extra development lifecycle checks.

**L0008.** Render the App function component with JSX; this is not an immediate ordinary function call written as App().

**L0009.** Close the StrictMode element and separate render arguments with the trailing comma.

**L0010.** Close the render call.


<a id="frontend-src-services-apits"></a>
## frontend/src/services/api.ts

Shared typed fetch wrapper and endpoint methods. Generic assertions do not runtime-validate returned JSON. Tokens are propagated; 204 is handled without JSON parsing. There is no fetch cancellation timeout/retry/cache.

Source fingerprint: `8227d814c95d2692cd4f0eb38e4996df2733582b61f0e63b6d0830bc4d82cbe9`. Physical lines: 82.

### Numbered source

```typescript
0001 | import { supabase } from '../lib/supabase'
0002 | 
0003 | export type Workflow = {
0004 |   id: string
0005 |   user_id: string
0006 |   name: string
0007 |   enabled: boolean
0008 | }
0009 | 
0010 | export type Component = {
0011 |   type: string
0012 |   config: Record<string, unknown>
0013 | }
0014 | 
0015 | export type WorkflowDetail = Workflow & {
0016 |   trigger: Component
0017 |   conditions: Component[]
0018 |   actions: Component[]
0019 | }
0020 | 
0021 | export type Execution = {
0022 |   id: string
0023 |   workflow_id: string
0024 |   status: string
0025 |   trigger_data: Record<string, unknown>
0026 |   result: Record<string, unknown>
0027 |   error: string | null
0028 | }
0029 | 
0030 | export type GmailStatus = {
0031 |   connected: boolean
0032 |   email: string | null
0033 | }
0034 | 
0035 | export type GmailConnectResponse = {
0036 |   authorization_url: string
0037 | }
0038 | 
0039 | const apiUrl = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'
0040 | 
0041 | async function request<T>(path: string, options?: RequestInit): Promise<T> {
0042 |   const { data } = (await supabase?.auth.getSession()) ?? { data: { session: null } }
0043 |   const accessToken = data.session?.access_token
0044 |   const response = await fetch(`${apiUrl}${path}`, {
0045 |     ...options,
0046 |     headers: {
0047 |       'Content-Type': 'application/json',
0048 |       ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
0049 |       ...(options?.headers ?? {}),
0050 |     },
0051 |   })
0052 |   if (!response.ok) {
0053 |     const body = await response.json().catch(() => ({}))
0054 |     throw new Error(typeof body.detail === 'string' ? body.detail : 'Request failed')
0055 |   }
0056 |   if (response.status === 204) return undefined as T
0057 |   return response.json() as Promise<T>
0058 | }
0059 | 
0060 | export const api = {
0061 |   listWorkflows: (userId: string) =>
0062 |     request<Workflow[]>(`/api/workflows?user_id=${encodeURIComponent(userId)}`),
0063 |   getWorkflow: (id: string) => request<WorkflowDetail>(`/api/workflows/${id}`),
0064 |   createWorkflow: (payload: unknown) =>
0065 |     request<Workflow>('/api/workflows', { method: 'POST', body: JSON.stringify(payload) }),
0066 |   updateWorkflow: (id: string, payload: unknown) =>
0067 |     request<WorkflowDetail>(`/api/workflows/${id}`, {
0068 |       method: 'PUT',
0069 |       body: JSON.stringify(payload),
0070 |     }),
0071 |   deleteWorkflow: (id: string) =>
0072 |     request<void>(`/api/workflows/${id}`, { method: 'DELETE' }),
0073 |   runWorkflow: (id: string, payload: Record<string, unknown>) =>
0074 |     request<Execution>(`/api/workflows/${id}/run`, {
0075 |       method: 'POST',
0076 |       body: JSON.stringify({ payload }),
0077 |     }),
0078 |   executions: (id: string) => request<Execution[]>(`/api/workflows/${id}/executions`),
0079 |   gmailStatus: () => request<GmailStatus>('/api/integrations/gmail/status'),
0080 |   connectGmail: () => request<GmailConnectResponse>('/api/integrations/gmail/connect'),
0081 |   disconnectGmail: () => request<void>('/api/integrations/gmail', { method: 'DELETE' }),
0082 | }
```

### Every-line explanation

**L0001.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0002.** Blank line: separates related declarations/statements; no runtime operation.

**L0003.** Define the compile-time workflow summary object type. It contains no trigger/action config.

**L0004.** Declare compile-time property `id` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0005.** Declare compile-time property `user_id` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0006.** Declare compile-time property `name` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0007.** Declare compile-time property `enabled` with type `boolean`. This describes expected shape; it does not create a runtime validator.

**L0008.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0009.** Blank line: separates related declarations/statements; no runtime operation.

**L0010.** Define the reusable component-configuration type; this is not React.Component.

**L0011.** Declare compile-time property `type` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0012.** Record<string, unknown> permits string keys but requires narrowing values before assuming operations.

**L0013.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0014.** Blank line: separates related declarations/statements; no runtime operation.

**L0015.** Intersect Workflow's summary fields with the following detail fields.

**L0016.** Declare compile-time property `trigger` with type `Component`. This describes expected shape; it does not create a runtime validator.

**L0017.** Conditions is an array in the API even though this UI edits only the first.

**L0018.** Actions is an ordered array in the API even though this UI edits only the first.

**L0019.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0020.** Blank line: separates related declarations/statements; no runtime operation.

**L0021.** Describe persisted execution JSON, distinct from a runtime EngineResult class.

**L0022.** Declare compile-time property `id` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0023.** Declare compile-time property `workflow_id` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0024.** Declare compile-time property `status` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0025.** Declare compile-time property `trigger_data` with type `Record<string, unknown>`. This describes expected shape; it does not create a runtime validator.

**L0026.** Declare compile-time property `result` with type `Record<string, unknown>`. This describes expected shape; it does not create a runtime validator.

**L0027.** An execution error can be a string or explicitly null.

**L0028.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0029.** Blank line: separates related declarations/statements; no runtime operation.

**L0030.** Public Gmail status contains only connection flag and account email.

**L0031.** Declare compile-time property `connected` with type `boolean`. This describes expected shape; it does not create a runtime validator.

**L0032.** Declare compile-time property `email` with type `string | null`. This describes expected shape; it does not create a runtime validator.

**L0033.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0034.** Blank line: separates related declarations/statements; no runtime operation.

**L0035.** Describe the backend connect response containing Google's consent destination.

**L0036.** Declare compile-time property `authorization_url` with type `string`. This describes expected shape; it does not create a runtime validator.

**L0037.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0038.** Blank line: separates related declarations/statements; no runtime operation.

**L0039.** Read the public backend URL with a localhost development fallback.

**L0040.** Blank line: separates related declarations/statements; no runtime operation.

**L0041.** Define an async generic request wrapper: T is the expected response type, RequestInit is the optional native fetch options type, and the result is Promise<T>.

**L0042.** Safely call a configured Supabase client; if absent, supply a compatible null-session data shape. Destructure data from the awaited/default result.

**L0043.** Read the access token only if there is a session.

**L0044.** Call native fetch with the configured origin plus API path.

**L0045.** Spread caller method/body/options before constructing the explicit headers below.

**L0046.** Begin the headers object.

**L0047.** Set JSON request content type by default.

**L0048.** Conditionally add a Bearer header when a token exists. The template expression constructs the header value.

**L0049.** Spread caller headers last so matching defaults can be overridden. This assumes compatible spreadable headers rather than normalizing every HeadersInit variant.

**L0050.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0051.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0052.** fetch does not reject just because a server returns 4xx/5xx, so explicitly inspect response.ok.

**L0053.** Try parsing error JSON; if it is not JSON, replace the parse rejection with an empty object.

**L0054.** Throw a useful detail string if provided, or a generic error. Structured validation-detail arrays are not formatted by this wrapper.

**L0055.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0056.** 204 has no body: return undefined asserted as T instead of parsing JSON.

**L0057.** Return JSON with an asserted generic promise type. This is not runtime schema validation.

**L0058.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0059.** Blank line: separates related declarations/statements; no runtime operation.

**L0060.** Export a collection of endpoint functions sharing request/token/error behavior.

**L0061.** List method accepts a user ID; backend must independently verify ownership.

**L0062.** URL-encode the query value and expect an array of summary objects.

**L0063.** Retrieve full editable detail for one ID.

**L0064.** Creation accepts unknown payload; the server's Pydantic schema is the runtime trust boundary.

**L0065.** POST JSON-serialized config and expect a workflow summary.

**L0066.** Replacement update accepts a workflow ID and payload.

**L0067.** PUT to the selected resource and expect full detail.

**L0068.** Specify replacement update HTTP method.

**L0069.** Serialize the replacement payload into request body text.

**L0070.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0071.** Define deletion for one workflow ID.

**L0072.** Expect no meaningful return value for a DELETE that responds with 204.

**L0073.** Manual run accepts a dictionary payload with unknown values.

**L0074.** Expect an execution record from the run operation.

**L0075.** Use POST for the run request.

**L0076.** Wrap custom event input inside the ManualRunRequest payload field and serialize it.

**L0077.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.

**L0078.** Retrieve persisted execution history; no streaming/subscription is established.

**L0079.** Retrieve only the Gmail connection flag/account email.

**L0080.** Ask the server to prepare an OAuth state and authorization URL.

**L0081.** Delete the local Gmail connection; this endpoint's default response differs from the workflow 204 route but the wrapper still parses it.

**L0082.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.


<a id="backend-requirementstxt"></a>
## backend/requirements.txt

Backend dependency lower bounds. These are not a reproducible exact version lock. The Python standard library is not installed from this list.

Source fingerprint: `ec7f55e73262ec95ce47f0fb5445d1bf19c70967329d2b7ddd92debe81f59c0f`. Physical lines: 10.

### Numbered source

```text
0001 | fastapi>=0.115.0
0002 | uvicorn[standard]>=0.32.0
0003 | sqlalchemy>=2.0.36
0004 | psycopg[binary]>=3.2.0
0005 | pydantic>=2.9.0
0006 | pydantic-settings>=2.6.0
0007 | httpx>=0.27.0
0008 | cryptography>=43.0.0
0009 | pytest>=8.3.0
0010 | python-dotenv>=1.0.1
```

### Every-line explanation

**L0001.** Declare install requirement `fastapi>=0.115.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0002.** Declare install requirement `uvicorn[standard]>=0.32.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0003.** Declare install requirement `sqlalchemy>=2.0.36`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0004.** Declare install requirement `psycopg[binary]>=3.2.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0005.** Declare install requirement `pydantic>=2.9.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0006.** Declare install requirement `pydantic-settings>=2.6.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0007.** Declare install requirement `httpx>=0.27.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0008.** Declare install requirement `cryptography>=43.0.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0009.** Declare install requirement `pytest>=8.3.0`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.

**L0010.** Declare install requirement `python-dotenv>=1.0.1`. >= is a lower bound; bracket extras request optional bundled capabilities. See master chapter 20 for this dependency's role and alternative.


<a id="backend-pytestini"></a>
## backend/pytest.ini

pytest import/discovery settings for normal backend execution.

Source fingerprint: `e621dabb0551d82e234c399c39d035481d1b20a1ccbeb7a3ade640fc9dd1a151`. Physical lines: 3.

### Numbered source

```text
0001 | [pytest]
0002 | pythonpath = .
0003 | testpaths = tests
```

### Every-line explanation

**L0001.** Start pytest's configuration section.

**L0002.** Add the configured backend directory to imports for app package resolution.

**L0003.** Use tests as the normal test discovery directory.


<a id="frontend-packagejson"></a>
## frontend/package.json

Actual package/script manifest. build performs tsc -b then Vite; lint is Oxlint. Caret/tilde ranges are compatible-version declarations, not exact installed versions. No npm test/typecheck script exists.

Source fingerprint: `39f15a9b846fb38923fe0f90eee1628a3262eb7af0939f020b1b40f07515bbc8`. Physical lines: 26.

### Numbered source

```json
0001 | {
0002 |   "name": "frontend",
0003 |   "private": true,
0004 |   "version": "0.0.0",
0005 |   "type": "module",
0006 |   "scripts": {
0007 |     "dev": "vite",
0008 |     "build": "tsc -b && vite build",
0009 |     "lint": "oxlint",
0010 |     "preview": "vite preview"
0011 |   },
0012 |   "dependencies": {
0013 |     "@supabase/supabase-js": "^2.117.2",
0014 |     "react": "^19.2.8",
0015 |     "react-dom": "^19.2.8"
0016 |   },
0017 |   "devDependencies": {
0018 |     "@types/node": "^24.13.3",
0019 |     "@types/react": "^19.2.18",
0020 |     "@types/react-dom": "^19.2.7",
0021 |     "@vitejs/plugin-react": "^6.1.1",
0022 |     "oxlint": "^1.81.0",
0023 |     "typescript": "~6.0.2",
0024 |     "vite": "^8.3.0"
0025 |   }
0026 | }
```

### Every-line explanation

**L0001.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0002.** Set `name`: package identifier.

**L0003.** Set `private`: prevent accidental npm publication.

**L0004.** Set `version`: package metadata version, not the React version.

**L0005.** Set `type`: ES module interpretation when module.

**L0006.** Set `scripts`: named npm commands.

**L0007.** Set `dev`: run the Vite development server.

**L0008.** Set `build`: type-check referenced TS projects, then build only if that succeeds.

**L0009.** Set `lint`: run the installed Oxlint checker.

**L0010.** Set `preview`: serve the already built frontend locally.

**L0011.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0012.** Set `dependencies`: packages required by runtime application imports.

**L0013.** Declare `@supabase/supabase-js` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0014.** Declare `react` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0015.** Declare `react-dom` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0016.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0017.** Set `devDependencies`: tooling/type packages used while developing/building.

**L0018.** Declare `@types/node` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0019.** Declare `@types/react` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0020.** Declare `@types/react-dom` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0021.** Declare `@vitejs/plugin-react` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0022.** Declare `oxlint` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0023.** Declare `typescript` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0024.** Declare `vite` with its version range. A caret allows compatible updates within the package's major-version convention; tilde is narrower. Actual installed resolution may differ from this literal range. See dependency rationale in master chapter 20.

**L0025.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0026.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.


<a id="frontend-indexhtml"></a>
## frontend/index.html

Static HTML shell with an empty React root and a module entry. Browser receives generated production assets after Vite builds. Current title remains frontend.

Source fingerprint: `802bff73f103056273b18d331fee9998b84207e96bc5f5d734163163339515c1`. Physical lines: 13.

### Numbered source

```html
0001 | <!doctype html>
0002 | <html lang="en">
0003 |   <head>
0004 |     <meta charset="UTF-8" />
0005 |     <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
0006 |     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
0007 |     <title>frontend</title>
0008 |   </head>
0009 |   <body>
0010 |     <div id="root"></div>
0011 |     <script type="module" src="/src/main.tsx"></script>
0012 |   </body>
0013 | </html>
```

### Every-line explanation

**L0001.** Declare HTML5 parsing mode.

**L0002.** Start the HTML document and identify English as its language.

**L0003.** Start metadata rather than visible body content.

**L0004.** Declare UTF-8 text encoding.

**L0005.** Link the public SVG favicon asset; it is a UI icon, not workflow execution logic.

**L0006.** Use device width and initial scale for responsive mobile rendering.

**L0007.** Set the browser tab title; the current scaffold title is frontend.

**L0008.** Close document metadata.

**L0009.** Start visible/document body content.

**L0010.** Provide the root DOM mount point into which React renders App.

**L0011.** Load main.tsx as an ES module through Vite's development/build handling.

**L0012.** Close body.

**L0013.** Close HTML document.


<a id="frontend-viteconfigts"></a>
## frontend/vite.config.ts

Vite configuration enabling the React plugin; not a Python server or the workflow engine.

Source fingerprint: `f58edcc886dbf642f0aad60dce0c36a378df3022aa88cec76592532b12d529cc`. Physical lines: 7.

### Numbered source

```typescript
0001 | import react from '@vitejs/plugin-react'
0002 | import { defineConfig } from 'vite'
0003 | 
0004 | // https://vite.dev/config/
0005 | export default defineConfig({
0006 |   plugins: [react()],
0007 | })
```

### Every-line explanation

**L0001.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0002.** Import the displayed module/export into this ES module. Relative paths refer to project files; package names resolve installed dependencies.

**L0003.** Blank line: separates related declarations/statements; no runtime operation.

**L0004.** Comment/reference for developers; not executed: https://vite.dev/config/

**L0005.** Export Vite's configuration using defineConfig for tool typing/conventions.

**L0006.** Enable the React Vite plugin; this is build/development integration, not a backend route.

**L0007.** Close the current object/function/callback/argument grouping. Braces delimit blocks or object/JSX expressions according to the surrounding code; no separate side effect occurs on this delimiter line.


<a id="frontend-tsconfigjson"></a>
## frontend/tsconfig.json

TypeScript project configuration. Root references split browser and tooling concerns. No explicit strict:true is enabled in these configs. The build uses tsc -b to follow references.

Source fingerprint: `ad28d132ee48d6e23917cf5827cace785d0fc01a44ca68b0dda51cc8c3fd3f52`. Physical lines: 7.

### Numbered source

```json
0001 | {
0002 |   "files": [],
0003 |   "references": [
0004 |     { "path": "./tsconfig.app.json" },
0005 |     { "path": "./tsconfig.node.json" }
0006 |   ]
0007 | }
```

### Every-line explanation

**L0001.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0002.** Set `files`: root file list; empty here because projects are referenced below.

**L0003.** Set `references`: TypeScript project references used by tsc -b.

**L0004.** Set `path`: relative referenced project configuration.

**L0005.** Set `path`: relative referenced project configuration.

**L0006.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0007.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.


<a id="frontend-tsconfigappjson"></a>
## frontend/tsconfig.app.json

TypeScript project configuration. Root references split browser and tooling concerns. No explicit strict:true is enabled in these configs. The build uses tsc -b to follow references.

Source fingerprint: `bbcd078c923aa26585b32222f966a047948210372f3adbf41617e7553ef73e13`. Physical lines: 26.

### Numbered source

```json
0001 | {
0002 |   "compilerOptions": {
0003 |     "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
0004 |     "target": "es2023",
0005 |     "lib": ["ES2023", "DOM"],
0006 |     "module": "esnext",
0007 |     "types": ["vite/client"],
0008 |     "allowArbitraryExtensions": true,
0009 |     "skipLibCheck": true,
0010 | 
0011 |     /* Bundler mode */
0012 |     "moduleResolution": "bundler",
0013 |     "allowImportingTsExtensions": true,
0014 |     "verbatimModuleSyntax": true,
0015 |     "moduleDetection": "force",
0016 |     "noEmit": true,
0017 |     "jsx": "react-jsx",
0018 | 
0019 |     /* Linting */
0020 |     "noUnusedLocals": true,
0021 |     "noUnusedParameters": true,
0022 |     "erasableSyntaxOnly": true,
0023 |     "noFallthroughCasesInSwitch": true
0024 |   },
0025 |   "include": ["src"]
0026 | }
```

### Every-line explanation

**L0001.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0002.** Set `compilerOptions`: TypeScript compiler settings.

**L0003.** Set `tsBuildInfoFile`: location for incremental build metadata.

**L0004.** Set `target`: modern JavaScript output/type-check target.

**L0005.** Set `lib`: ambient API declarations to include, such as DOM.

**L0006.** Set `module`: module interpretation/output target.

**L0007.** Set `types`: ambient declaration packages, not runtime imports.

**L0008.** Set `allowArbitraryExtensions`: permit arbitrary-extension imports when declaration resolution permits them.

**L0009.** Set `skipLibCheck`: skip checking dependency declaration files, not all application checking.

**L0010.** Blank formatting line.

**L0011.** JSON-with-comments developer note, not an executable operation. TypeScript config accepts comments even though strict JSON does not.

**L0012.** Set `moduleResolution`: how the compiler resolves imports.

**L0013.** Set `allowImportingTsExtensions`: allow imports naming .ts/.tsx extensions with compatible emit settings.

**L0014.** Set `verbatimModuleSyntax`: preserve ordinary module syntax while removing type-only imports.

**L0015.** Set `moduleDetection`: treat files as modules according to force setting.

**L0016.** Set `noEmit`: type-check without emitting JavaScript; Vite owns the asset build.

**L0017.** Set `jsx`: use the modern React JSX transform.

**L0018.** Blank formatting line.

**L0019.** JSON-with-comments developer note, not an executable operation. TypeScript config accepts comments even though strict JSON does not.

**L0020.** Set `noUnusedLocals`: report unused local declarations.

**L0021.** Set `noUnusedParameters`: report unused parameters subject to compiler conventions.

**L0022.** Set `erasableSyntaxOnly`: restrict TS features to forms erasable without runtime language transformation.

**L0023.** Set `noFallthroughCasesInSwitch`: report accidental switch case fallthrough.

**L0024.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0025.** Set `include`: source paths included in this project.

**L0026.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.


<a id="frontend-tsconfignodejson"></a>
## frontend/tsconfig.node.json

TypeScript project configuration. Root references split browser and tooling concerns. No explicit strict:true is enabled in these configs. The build uses tsc -b to follow references.

Source fingerprint: `a9e6c7f6fd3ec455a6fe1d4fbb83091e774b62fe116008ab6d8c5e1e88af4629`. Physical lines: 23.

### Numbered source

```json
0001 | {
0002 |   "compilerOptions": {
0003 |     "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
0004 |     "target": "es2023",
0005 |     "lib": ["ES2023"],
0006 |     "types": ["node"],
0007 |     "skipLibCheck": true,
0008 | 
0009 |     /* Bundler mode */
0010 |     "module": "nodenext",
0011 |     "allowImportingTsExtensions": true,
0012 |     "verbatimModuleSyntax": true,
0013 |     "moduleDetection": "force",
0014 |     "noEmit": true,
0015 | 
0016 |     /* Linting */
0017 |     "noUnusedLocals": true,
0018 |     "noUnusedParameters": true,
0019 |     "erasableSyntaxOnly": true,
0020 |     "noFallthroughCasesInSwitch": true
0021 |   },
0022 |   "include": ["vite.config.ts"]
0023 | }
```

### Every-line explanation

**L0001.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0002.** Set `compilerOptions`: TypeScript compiler settings.

**L0003.** Set `tsBuildInfoFile`: location for incremental build metadata.

**L0004.** Set `target`: modern JavaScript output/type-check target.

**L0005.** Set `lib`: ambient API declarations to include, such as DOM.

**L0006.** Set `types`: ambient declaration packages, not runtime imports.

**L0007.** Set `skipLibCheck`: skip checking dependency declaration files, not all application checking.

**L0008.** Blank formatting line.

**L0009.** JSON-with-comments developer note, not an executable operation. TypeScript config accepts comments even though strict JSON does not.

**L0010.** Set `module`: module interpretation/output target.

**L0011.** Set `allowImportingTsExtensions`: allow imports naming .ts/.tsx extensions with compatible emit settings.

**L0012.** Set `verbatimModuleSyntax`: preserve ordinary module syntax while removing type-only imports.

**L0013.** Set `moduleDetection`: treat files as modules according to force setting.

**L0014.** Set `noEmit`: type-check without emitting JavaScript; Vite owns the asset build.

**L0015.** Blank formatting line.

**L0016.** JSON-with-comments developer note, not an executable operation. TypeScript config accepts comments even though strict JSON does not.

**L0017.** Set `noUnusedLocals`: report unused local declarations.

**L0018.** Set `noUnusedParameters`: report unused parameters subject to compiler conventions.

**L0019.** Set `erasableSyntaxOnly`: restrict TS features to forms erasable without runtime language transformation.

**L0020.** Set `noFallthroughCasesInSwitch`: report accidental switch case fallthrough.

**L0021.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0022.** Set `include`: source paths included in this project.

**L0023.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.


<a id="frontend-oxlintrcjson"></a>
## frontend/.oxlintrc.json

Actual Oxlint settings; React hooks rules are enabled. Linting catches patterns distinct from TypeScript type checking.

Source fingerprint: `3f46d4038fd69c0011da897b887d747e3d66f0bbda8b523a54891fbd473d67ef`. Physical lines: 8.

### Numbered source

```json
0001 | {
0002 |   "$schema": "./node_modules/oxlint/configuration_schema.json",
0003 |   "plugins": ["react", "typescript", "oxc"],
0004 |   "rules": {
0005 |     "react/rules-of-hooks": "error",
0006 |     "react/only-export-components": ["warn", { "allowConstantExport": true }]
0007 |   }
0008 | }
```

### Every-line explanation

**L0001.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0002.** Set `$schema`: editor/schema reference for configuration validation.

**L0003.** Set `plugins`: enable named linter plugins.

**L0004.** Set `rules`: configure individual linter rules.

**L0005.** Set `react/rules-of-hooks`: enforce valid React hook call placement.

**L0006.** Set `react/only-export-components`: warn about exports affecting fast refresh conventions.

**L0007.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.

**L0008.** Open/close the JSON object/array or separate its properties. Braces hold objects, brackets hold arrays, colons pair names with values, and commas separate entries.


<a id="github-workflows-flowforge-dispatchyml"></a>
## .github/workflows/flowforge-dispatch.yml

Read-only explanation of the existing GitHub Actions demonstration. A repository_dispatch type flowforge runs a hosted job that creates an issue. Runtime GITHUB_TOKEN is distinct from FlowForge's dispatch token. No workflow/infrastructure changes were made.

Source fingerprint: `5d294bc4ff7fca90985ddcf77cf4966e0ec08276c9af749846d542cd1d9f4153`. Physical lines: 23.

### Numbered source

```yaml
0001 | name: FlowForge dispatch
0002 | 
0003 | on:
0004 |   repository_dispatch:
0005 |     types: [flowforge]
0006 | 
0007 | permissions:
0008 |   issues: write
0009 | 
0010 | jobs:
0011 |   create-flowforge-issue:
0012 |     runs-on: ubuntu-latest
0013 |     steps:
0014 |       - name: Create visible issue
0015 |         env:
0016 |           GH_TOKEN: ${{ github.token }}
0017 |           FLOWFORGE_SOURCE: ${{ github.event.client_payload.source }}
0018 |           FLOWFORGE_PAYLOAD: ${{ toJson(github.event.client_payload) }}
0019 |         run: |
0020 |           gh issue create \
0021 |             --repo "$GITHUB_REPOSITORY" \
0022 |             --title "FlowForge event received" \
0023 |             --body "$(printf 'A FlowForge repository dispatch was received.\n\nSource: %s\n\nPayload:\n```json\n%s\n```' "$FLOWFORGE_SOURCE" "$FLOWFORGE_PAYLOAD")"
```

### Every-line explanation

**L0001.** Name this GitHub Actions workflow in the repository UI.

**L0002.** Blank formatting line.

**L0003.** Start event trigger definitions.

**L0004.** Listen for externally initiated repository_dispatch events.

**L0005.** Only match event_type flowforge; a different FlowForge event type will not start this job.

**L0006.** Blank formatting line.

**L0007.** Declare workflow token permissions.

**L0008.** Allow the Actions runtime token to create repository issues; this is not the external dispatch token.

**L0009.** Blank formatting line.

**L0010.** Define jobs executed after a matching dispatch.

**L0011.** Name the single issue-creation job.

**L0012.** Choose a GitHub-hosted Ubuntu runner; no workflow code is running inside FlowForge's backend process.

**L0013.** Start ordered job steps.

**L0014.** Name the issue-creation step.

**L0015.** Declare environment variables for the step rather than embedding payload data directly as shell source.

**L0016.** Expose GitHub's short-lived job token as GH_TOKEN for gh CLI authentication; this placeholder is not a literal credential value.

**L0017.** Pass the dispatched source field into a quoted shell environment variable.

**L0018.** Serialize the client payload to JSON text and pass it through an environment variable.

**L0019.** Use a YAML literal multiline scalar for the shell commands below.

**L0020.** Invoke gh issue create; backslash continues the shell command to the next line.

**L0021.** Target the current GitHub repository, quoting the shell variable expansion.

**L0022.** Set a fixed visible issue title.

**L0023.** Build an issue body with printf using payload variables as data arguments, then pass the resulting string as one quoted --body argument. Command substitution executes printf; it does not evaluate payload text as new shell code.

## Non-code assets and deliberate exclusions

frontend/src/assets/hero.png is a raster image; react.svg/vite.svg are starter vector assets. They are not imported by the current App. frontend/public/favicon.svg is linked by index.html. frontend/public/icons.svg is a static vector asset without workflow execution behavior. Binary/image data and SVG path coordinates are not Python/TypeScript algorithms and are not copied here.

The coverage set deliberately excludes actual .env files, database files, credentials, private logs, dependency packages, generated dist files, lockfile entries, and agent/tool configuration. Their exclusion does not mean hidden implementation features were inferred. The master guide explains public configuration variable names and deployment concepts without reading secret values.

Coverage total: 71 files; 3067 physical lines; 2613 nonblank lines. Each selected physical line has exactly one explanatory note.
