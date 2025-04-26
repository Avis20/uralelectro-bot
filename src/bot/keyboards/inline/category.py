from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.dto.product import CategoryDTO


def category_keyboard(
    categories: list[CategoryDTO],
    current_page: int = 1,
    total_pages: int = 10,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for category in categories:
        builder.button(
            text=category.name,
            callback_data=f"category_{category.id}",
        )

    builder.button(text="Назад", callback_data="menu")
    builder.adjust(1, repeat=True)

    return builder.as_markup()


def category_by_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Да", callback_data="category")
    builder.button(text="Нет", callback_data="category")
    builder.button(text="Назад", callback_data="menu")
    builder.adjust(1, repeat=True)
    return builder.as_markup()
