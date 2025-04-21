from fastapi import APIRouter

from .user.base import router as user_base_router

router = APIRouter(prefix="/v1")
router.include_router(user_base_router)
