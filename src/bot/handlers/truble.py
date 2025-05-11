from aiogram import F, Router, types
from aiogram.filters import Command

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot.dto.user import UserUpdateDTO
from bot.services.user_service import UserService


router = Router(name="truble")


class UserTrubleState(StatesGroup):
    waiting_for_data_phone = State()


@router.callback_query(F.data == "truble")
async def truble_callback(query: types.CallbackQuery, state: FSMContext) -> None:
    await query.message.answer("Укажите номер телефона и с вами свяжется специалист")
    await state.set_state(UserTrubleState.waiting_for_data_phone)


@router.message(UserTrubleState.waiting_for_data_phone)
async def process_phone_data(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_dto = await UserService.get_user_by_telegram_id(user_id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    user_data_message = message.text
    phone = user_data_message
    if not phone:
        await message.answer("Ошибка: неверный формат данных.")
        return

    update_user_dto = UserUpdateDTO(user_id=user_dto.id, phone_number=phone)
    await UserService.update_user(update_user_dto)
    await message.answer("Ваша заявка принята. Ожидайте звонка")
