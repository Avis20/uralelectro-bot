from aiogram import Router, types
from aiogram.filters import Command

from bot3.keyboards.inline.contacts import contacts_keyboard

router = Router(name="support")


@router.message(Command(commands=["supports", "support", "contacts", "contact"]))
async def support_handler(message: types.Message) -> None:
    """Return a button with a link to the project."""
    await message.answer(("support text"), reply_markup=contacts_keyboard())
