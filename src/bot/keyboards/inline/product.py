from uuid import UUID
from aiogram.types import InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram import F

from bot.callback.product import ProductCallbackData
from bot.dto.product import ProductDTO


def product_keyboard(
    products: list[ProductDTO],
    current_page: int = 1,
    total_pages: int = 10,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for product in products:
        product_text = f"{product.name} ({product.price} руб.)"
        builder.button(
            text=product_text,
            callback_data=f"product_{product.id}",
        )

    if current_page > 1:
        builder.button(text="<< Предыдущая", callback_data=f"prev_{current_page - 1}")

    if current_page < total_pages:
        builder.button(text="Следующая >>", callback_data=f"next_{current_page + 1}")

    builder.button(text="Назад", callback_data="menu")
    builder.adjust(1, repeat=True)

    return builder.as_markup()


def product_by_keyboard(product_id: UUID) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Оформить заказ",
        callback_data=ProductCallbackData(product_id=product_id).pack(),
    )
    builder.button(text="Назад", callback_data="menu")
    builder.adjust(1, repeat=True)
    return builder.as_markup()
