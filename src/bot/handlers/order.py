from aiogram import F, Router, types
from aiogram.filters import Command

from bot.services.order_service import OrderService
from bot.services.user_service import UserService

router = Router(name="order")


@router.message(Command(commands=["order"]))
async def order_handler(message: types.Message, user_id: int) -> None:
    user_dto = await UserService.get_user_by_telegram_id(user_id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    orders = await OrderService.get_orders_by_user_id(user_id=user_dto.id)
    if not orders:
        await message.answer("У вас нет заказов.")
        return

    await message.answer("Ваши заказы:")
    for order in orders:
        order_message = (
            f"📄 <b>Номер заказа:</b> {str(order.order_number)}\n"
            f"🏷 <b>Статус:</b> {order.order_status.name}\n"
            f"📦 <b>Товар:</b> {order.product.name} x {order.quantity} {order.product.unit_of_measure}\n"
            f"📍 <b>Адрес доставки:</b> {order.address}\n"
            f"📅 <b>Дата доставки:</b> {order.order_date}\n"
            f"💬 <b>Комментарий:</b> {order.comment or 'Нет'}\n"
        )
        await message.answer(text=order_message, parse_mode="HTML")


@router.callback_query(F.data == "order")
async def order_callback(query: types.CallbackQuery) -> None:
    user_id = query.from_user.id
    await order_handler(message=query.message, user_id=user_id)
