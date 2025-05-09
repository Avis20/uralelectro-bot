from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Константы для callback_data
CALLBACK_CATEGORY = "category"
CALLBACK_INFO = "info"
CALLBACK_SUPPORT = "support"
CALLBACK_FAQ = "faq"


def main_keyboard() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для главного меню.

    Returns:
        InlineKeyboardMarkup: Объект клавиатуры с кнопками меню
    """
    buttons = [
        [InlineKeyboardButton(text="Каталог товаров", callback_data=CALLBACK_CATEGORY)],
        # [InlineKeyboardButton(text="Сделать запрос", callback_data="request")],
        [InlineKeyboardButton(text="О компании", callback_data=CALLBACK_INFO)],
        [InlineKeyboardButton(text="Служба поддержки", callback_data=CALLBACK_SUPPORT)],
        [InlineKeyboardButton(text="FAQ", callback_data=CALLBACK_FAQ)],
    ]

    keyboard = InlineKeyboardBuilder(markup=buttons)
    keyboard.adjust(1)  # Размещаем все кнопки в один столбец

    return keyboard.as_markup()
