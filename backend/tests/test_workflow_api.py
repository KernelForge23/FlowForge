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
