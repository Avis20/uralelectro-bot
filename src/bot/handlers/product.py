from aiogram import F, Router, types
from aiogram.filters import Command

from loguru import logger

from bot.keyboards.inline.product import product_keyboard

router = Router(name="product")


@router.message(Command(commands=["products", "product"]))
async def product_handler(message: types.Message) -> None:
    await message.answer("Каталог товаров", reply_markup=product_keyboard())


@router.callback_query(F.data == "product")
async def product_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    logger.info(query.data)
    await product_handler(query.message)
