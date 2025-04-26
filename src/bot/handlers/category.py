from uuid import UUID
from aiogram import F, Router, types

from aiogram.filters import Command

from loguru import logger

from bot.handlers.product import product_handler
from bot.keyboards.inline.category import category_keyboard
from bot.services.category_service import CategoryService
from bot.services.product_service import ProductService

router = Router(name="category")


@router.message(Command(commands=["categories", "category"]))
async def category_handler(message: types.Message) -> None:
    page = 1
    per_page = 5

    categories, total_pages = await CategoryService.get_categories(page, per_page)
    keyboard = category_keyboard(categories, page, total_pages)
    await message.answer("Выберите категорию", reply_markup=keyboard)


@router.callback_query(F.data == "category")
async def category_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    await category_handler(query.message)


async def category_by_id_handler(message: types.Message, category_id: str) -> None:
    await product_handler(message, category_id)


@router.callback_query(F.data.startswith('category_'))
async def category_number_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    category_id = query.data.split("_")[1]  # type: ignore
    logger.info(f"Category ID: {category_id}")
    await category_by_id_handler(query.message, category_id)
