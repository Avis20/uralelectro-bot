from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.dto.user import UserCreateDTO
from bot.keyboards.inline.menu import main_keyboard
from bot.services.user_service import UserService

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    """Welcome message."""
    user_id = message.from_user.id
    print('\n\n')
    print(user_id)
    print('\n\n')
    if user_id:
        user_dto = await UserService.get_user_by_telegram_id(user_id)
        if not user_dto:
            user_create_dto = UserCreateDTO(
                telegram_user_id=user_id,
                contact_person=message.from_user.full_name,
            )
            user_dto = await UserService.create_user(user_create_dto)
    message_text = (
        "Привет! Я чат-бот компании ООО ТД \"УралЭнергоКомплект\"\n"
        "Я помогу вам сделать заказ наших товаров\n"
        "Для того, чтобы начать, пожалуйста, выберите один из пунктов меню\n"
        "Если у вас возникнут вопросы, вы можете обратиться в нашу тех. поддержку\n"
        "Спасибо за ваш выбор!"
    )
    await message.answer(message_text, reply_markup=main_keyboard())
