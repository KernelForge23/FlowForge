import hashlib
import hmac

from app.db import get_session
from app.main import app
from app.models import User


def test_create_load_and_run_workflow_api(client, db_session) -> None:
    user = User(email="api@example.com")
    db_session.add(user)
    db_session.commit()

    def override_session():
        yield db_session

    app.dependency_overrides[get_session] = override_session
    try:
        create = client.post(
            "/api/workflows",
            json={
                "user_id": user.id,
                "name": "API workflow",
                "enabled": True,
                "trigger": {"type": "manual"},
                "conditions": [],
                "actions": [{"type": "noop"}],
            },
        )
        assert create.status_code == 201
        workflow_id = create.json()["id"]

        loaded = client.get(f"/api/workflows/{workflow_id}")
        run = client.post(f"/api/workflows/{workflow_id}/run", json={"payload": {"source": "test"}})

        assert loaded.status_code == 200
        assert loaded.json()["name"] == "API workflow"
        assert run.status_code == 200
        assert run.json()["status"] == "SUCCESS"
    finally:
        app.dependency_overrides.clear()


def test_github_webhook_runs_enabled_webhook_workflow(client, db_session) -> None:
    user = User(email="webhook@example.com")
    db_session.add(user)
    db_session.commit()

    def override_session():
        yield db_session

    app.dependency_overrides[get_session] = override_session
    try:
        create = client.post(
            "/api/workflows",
            json={
                "user_id": user.id,
                "name": "GitHub workflow",
                "enabled": True,
                "trigger": {"type": "webhook", "config": {"source": "github"}},
                "actions": [{"type": "noop"}],
            },
        )
        assert create.status_code == 201

        webhook = client.post("/api/webhooks/github", json={"action": "opened"})

        assert webhook.status_code == 200
        assert webhook.json()[0]["status"] == "SUCCESS"
    finally:
        app.dependency_overrides.clear()


def test_github_webhook_requires_valid_signature(client, monkeypatch) -> None:
    monkeypatch.setattr("app.api.routes.webhooks.settings.github_webhook_secret", "test-secret")
    payload = b'{"action":"opened"}'
    signature = "sha256=" + hmac.new(b"test-secret", payload, hashlib.sha256).hexdigest()

    missing = client.post(
        "/api/webhooks/github",
        content=payload,
        headers={"content-type": "application/json"},
    )
    valid = client.post(
        "/api/webhooks/github",
        content=payload,
        headers={"content-type": "application/json", "x-hub-signature-256": signature},
    )

    assert missing.status_code == 401
    assert valid.status_code == 200


def test_workflow_can_be_updated_and_deleted(client, db_session) -> None:
    user = User(email="crud@example.com")
    db_session.add(user)
    db_session.commit()

    def override_session():
        yield db_session

    app.dependency_overrides[get_session] = override_session
    try:
        create = client.post(
            "/api/workflows",
            json={
                "user_id": user.id,
                "name": "Before",
                "enabled": True,
                "trigger": {"type": "manual"},
                "actions": [{"type": "noop"}],
            },
        )
        workflow_id = create.json()["id"]

        update = client.put(
            f"/api/workflows/{workflow_id}",
            json={
                "name": "After",
                "enabled": False,
                "trigger": {"type": "webhook", "config": {"source": "github"}},
                "conditions": [{"type": "equals", "config": {"field": "action", "value": "opened"}}],
                "actions": [{"type": "noop"}],
            },
        )
        assert update.status_code == 200
        assert update.json()["name"] == "After"
        assert update.json()["trigger"]["type"] == "webhook"

        deleted = client.delete(f"/api/workflows/{workflow_id}")
        assert deleted.status_code == 204
        assert client.get(f"/api/workflows/{workflow_id}").status_code == 404
    finally:
        app.dependency_overrides.clear()


def test_workflow_with_execution_can_be_deleted(client, db_session) -> None:
    user = User(email="delete-execution@example.com")
    db_session.add(user)
    db_session.commit()

    def override_session():
        yield db_session

    app.dependency_overrides[get_session] = override_session
    try:
        create = client.post(
            "/api/workflows",
            json={
                "user_id": user.id,
                "name": "Workflow with history",
                "enabled": True,
                "trigger": {"type": "manual"},
                "actions": [{"type": "noop"}],
            },
        )
        workflow_id = create.json()["id"]
        run = client.post(f"/api/workflows/{workflow_id}/run", json={"payload": {}})
        assert run.status_code == 200

        deleted = client.delete(f"/api/workflows/{workflow_id}")

        assert deleted.status_code == 204
        assert client.get(f"/api/workflows/{workflow_id}").status_code == 404
    finally:
        app.dependency_overrides.clear()
