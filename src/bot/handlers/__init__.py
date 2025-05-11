from aiogram import Router

from bot.handlers.start import router as start_router
from bot.handlers.menu import router as menu_router
from bot.handlers.support import router as support_router
from bot.handlers.info import router as info_router
from bot.handlers.truble import router as truble_router
from bot.handlers.product import router as product_router
from bot.handlers.category import router as category_router
from bot.handlers.faq import router as faq_router
from bot.handlers.order import router as order_router


def get_handlers_router() -> Router:
    router = Router()
    router.include_router(start_router)
    router.include_router(menu_router)
    router.include_router(info_router)
    router.include_router(support_router)
    router.include_router(truble_router)
    router.include_router(product_router)
    router.include_router(category_router)
    router.include_router(faq_router)
    router.include_router(order_router)
    return router
