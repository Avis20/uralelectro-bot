from aiogram import F, Router, types
from aiogram.filters import Command


router = Router(name="truble")


@router.message(Command(commands=["truble", "truble"]))
async def truble_handler(message: types.Message) -> None:
    await message.answer("Опишите Вашу проблему и наш специалист скоро с вами свяжется")


@router.callback_query(F.data == "truble")
async def truble_callback(query: types.CallbackQuery) -> None:
    await truble_handler(query.message)
