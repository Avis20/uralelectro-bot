from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from bot3.middlewares.logging import LoggingMiddleware

# from bot.middlewares.auth import AuthMiddleware
# from bot.middlewares.database import DatabaseMiddleware
# from bot.middlewares.i18n import ACLMiddleware
# from bot.middlewares.throttling import ThrottlingMiddleware


def register_middlewares(dp: Dispatcher) -> None:

    # dp.message.outer_middleware(ThrottlingMiddleware())

    dp.update.outer_middleware(LoggingMiddleware())

    # dp.update.outer_middleware(DatabaseMiddleware())

    # dp.message.middleware(AuthMiddleware())

    # ACLMiddleware(i18n=_i18n).setup(dp)

    dp.callback_query.middleware(CallbackAnswerMiddleware())
