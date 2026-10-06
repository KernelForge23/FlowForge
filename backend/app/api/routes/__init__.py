from fastapi import APIRouter

from app.api.routes import health, integrations, webhooks, workflows

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(workflows.router)
api_router.include_router(webhooks.router)
api_router.include_router(integrations.router)
