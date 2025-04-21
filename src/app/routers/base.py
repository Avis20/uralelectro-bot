from app.routers.api import router as api_router
from app.routers.index import router as index_router
from fastapi import APIRouter, FastAPI


def setup_routers(app: FastAPI):
    root_router = APIRouter()
    root_router.include_router(index_router)
    root_router.include_router(api_router)
    app.include_router(root_router)
