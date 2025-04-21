from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_keyboard() -> InlineKeyboardMarkup:
    """Use in main menu."""
    buttons = [
        [InlineKeyboardButton(text="Каталог товаров", callback_data="product")],
        # [InlineKeyboardButton(text="Сделать запрос", callback_data="request")],
        [InlineKeyboardButton(text="О компании", callback_data="info")],
        [InlineKeyboardButton(text="Служба поддержки", callback_data="support")],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)

    keyboard.adjust(1, 1, 2)

    return keyboard.as_markup()
