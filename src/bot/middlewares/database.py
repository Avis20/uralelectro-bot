from __future__ import annotations
from typing import TYPE_CHECKING, Any

from loguru import logger

from aiogram import BaseMiddleware

from bot.database.pg_database import SQLAlchemyDatabaseConnector

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from aiogram.types import TelegramObject


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        sessionmaker = SQLAlchemyDatabaseConnector().get_master_session_maker()
        async with sessionmaker() as session:
            data["session"] = session
            # logger.info('\n\n')
            # logger.info(data)
            # logger.info('\n\n')
            # logger.info(handler)
            # logger.info(type(handler))
            # logger.info('\n\n')
            return await handler(event, data)
