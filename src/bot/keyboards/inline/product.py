from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def product_keyboard() -> InlineKeyboardMarkup:
    """Use when call product query."""
    buttons = [
        [InlineKeyboardButton(text="Продукт 1", callback_data="menu")],
        [InlineKeyboardButton(text="Продукт 2", callback_data="menu")],
        [InlineKeyboardButton(text="Продукт 3", callback_data="menu")],
        [InlineKeyboardButton(text="Назад", callback_data="menu")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()
