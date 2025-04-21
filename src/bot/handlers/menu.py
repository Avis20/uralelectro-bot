from aiogram import F, Router, types
from aiogram.filters import Command

from bot.keyboards.inline.menu import main_keyboard

router = Router(name="menu")


@router.message(Command(commands=["menu", "main"]))
async def menu_handler(message: types.Message) -> None:
    """Return main menu."""
    await message.answer("Выберите один из пунктов меню", reply_markup=main_keyboard())


@router.callback_query(F.data == "menu")
async def menu_callback(query: types.CallbackQuery) -> None:
    await menu_handler(query.message)
