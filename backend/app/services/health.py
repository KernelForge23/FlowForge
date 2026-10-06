from app.schemas.health import HealthResponse


class HealthService:
    def status(self) -> HealthResponse:
        return HealthResponse(status="ok", service="flowforge")
