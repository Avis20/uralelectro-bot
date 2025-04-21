from __future__ import annotations
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import Command

from bot3.filters.admin import AdminFilter
from bot3.services.users import get_all_users, get_user_count
from bot3.utils.users_export import convert_users_to_csv

if TYPE_CHECKING:
    from aiogram.types import BufferedInputFile, Message
    from sqlalchemy.ext.asyncio import AsyncSession

    from bot3.database.models import UserModel


router = Router(name="export_users")


@router.message(Command(commands="export_users"), AdminFilter())
async def export_users_handler(message: Message, session: AsyncSession) -> None:
    """Export all users in csv file."""
    all_users: list[UserModel] = await get_all_users(session)
    document: BufferedInputFile = await convert_users_to_csv(all_users)
    count: int = await get_user_count(session)

    await message.answer_document(document=document, caption=("user counter: <b>{count}</b>").format(count=count))
