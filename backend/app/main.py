from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import api_router
from app.db import init_db


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(title="FlowForge", lifespan=lifespan)
app.include_router(api_router)
