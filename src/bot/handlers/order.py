from aiogram import F, Router, types
from aiogram.filters import Command

router = Router(name="order")


@router.message(Command(commands=["order"]))
async def order_handler(message: types.Message) -> None:
    await message.answer(message_text)


@router.callback_query(F.data == "order")
async def order_callback(query: types.CallbackQuery) -> None:
    await order_handler(query.message)
