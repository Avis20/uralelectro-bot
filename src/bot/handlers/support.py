from aiogram import F, Router, types
from aiogram.filters import Command

from loguru import logger

from bot.keyboards.inline.support import support_keyboard

router = Router(name="support")


@router.message(Command(commands=["supports", "support", "support", "contact"]))
async def support_handler(message: types.Message) -> None:
    """Return a button with a link to the project."""
    await message.answer("Какой вопрос Вас интересует?", reply_markup=support_keyboard())


@router.callback_query(F.data == "support")
async def support_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    logger.info(query.data)
    await support_handler(query.message)
