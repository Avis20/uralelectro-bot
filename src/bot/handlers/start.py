from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.keyboards.inline.menu import main_keyboard

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    """Welcome message."""
    message_text = (
        "Привет! Я чат-бот компании ООО ТД \"УралЭнергоКомплект\"\n"
        "Я помогу вам сделать заказ наших товаров\n"
        "Для того, чтобы начать, пожалуйста, выберите один из пунктов меню\n"
        "Если у вас возникнут вопросы, вы можете обратиться в нашу тех. поддержку\n"
        "Спасибо за ваш выбор!"
    )
    await message.answer(message_text, reply_markup=main_keyboard())
