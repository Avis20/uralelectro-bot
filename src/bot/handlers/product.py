from uuid import UUID
from aiogram import F, Router, types

from aiogram.filters import Command

from loguru import logger

from bot.keyboards.inline.product import product_by_keyboard, product_keyboard
from bot.services.product_service import ProductService

router = Router(name="product")


@router.message(Command(commands=["products", "product"]))
async def product_handler(message: types.Message) -> None:
    page = 1
    per_page = 5

    products, total_pages = await ProductService.get_products(page, per_page)

    if products:
        keyboard = product_keyboard(products, page, total_pages)
        image_url = ""
        for product in products:
            if product.image_url:
                image_url = product.image_url
                break

        await message.answer_photo(
            photo=image_url,
            caption="Каталог товаров:",
            reply_markup=keyboard,
        )
    else:
        await message.answer(text="Продукты не найдены.", reply_markup=None)


@router.callback_query(F.data == "product")
async def product_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    await product_handler(query.message)


async def product_by_id_handler(message: types.Message, product_id: str) -> None:
    product = await ProductService.get_product_by_id(UUID(product_id))

    if not product:
        await message.answer(text="Продукт не найден.")
        return

    keyboard = product_by_keyboard()
    procudt_text = f"Название: {product.name}\nЦена: {product.price} руб."
    if product.category:
        procudt_text += f"\nКатегория: {product.category.name}\n"

    await message.answer_photo(
        photo=product.image_url,
        caption=procudt_text,
        reply_markup=keyboard,
    )


@router.callback_query(F.data.startswith('product_'))
async def product_number_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    product_id = query.data.split("_")[1]  # type: ignore
    logger.info(f"Product ID: {product_id}")
    await product_by_id_handler(query.message, product_id)
