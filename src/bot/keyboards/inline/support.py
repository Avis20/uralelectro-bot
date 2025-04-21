from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def support_keyboard() -> InlineKeyboardMarkup:
    """Use when call support query."""
    buttons = [
        [InlineKeyboardButton(text="Проблемы с заказом", callback_data="truble")],
        [InlineKeyboardButton(text="Назад", callback_data="menu")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    return keyboard.as_markup()
