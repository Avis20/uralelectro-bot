from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

# from bot.middlewares.logging import LoggingMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    # dp.update.outer_middleware(LoggingMiddleware())
    # from .auth import AuthMiddleware
    # from .database import DatabaseMiddleware
    # from .throttling import ThrottlingMiddleware

    # dp.message.outer_middleware(ThrottlingMiddleware())
    # dp.update.outer_middleware(DatabaseMiddleware())
    # dp.message.middleware(AuthMiddleware())
    dp.callback_query.middleware(CallbackAnswerMiddleware())
