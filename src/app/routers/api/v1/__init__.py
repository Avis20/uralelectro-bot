from fastapi import APIRouter

from .user.base import router as user_base_router
from .callback.base import router as callback_base_router

router = APIRouter(prefix="/v1")
router.include_router(user_base_router)
router.include_router(callback_base_router)
