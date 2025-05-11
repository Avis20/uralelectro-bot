import asyncio

from datetime import datetime, timedelta
from uuid import UUID
from aiogram import F, Router, types

from aiogram.types import CallbackQuery

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loguru import logger

from bot.callback.product import DeliveryCallbackData, ProductCallbackData
from bot.dto.order import OrderCreateDTO
from bot.keyboards.inline.product import product_by_keyboard, product_keyboard, product_question_keyboard
from bot.services.delivery_service import DeliveryService
from bot.services.order_service import OrderService
from bot.services.payment_service import PaymentService
from bot.services.product_service import ProductService
from bot.services.user_service import UserService

router = Router(name="product")

WAITING_TIME_MINUTES = 10


class UserState(StatesGroup):
    waiting_for_data_quantity = State()
    waiting_for_data_address = State()
    waiting_for_data_delivery_date = State()
    waiting_for_data_comment = State()
    waiting_for_data_confirm = State()


@router.message(Command(commands=["products", "product"]))
async def product_handler(message: types.Message, category_id: UUID | None = None) -> None:
    page = 1
    per_page = 5

    products, total_pages = await ProductService.get_products(
        page=page,
        per_page=per_page,
        category_id=category_id,
    )

    if products:
        keyboard = product_keyboard(products, page, total_pages)
        image_url = None
        for product in products:
            if product.image_url:
                image_url = product.image_url
                break
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption="Каталог товаров:",
                reply_markup=keyboard,
            )
        else:
            await message.answer(
                text="Каталог товаров:",
                reply_markup=keyboard,
            )
    else:
        await message.answer(text="Продукты не найдены.", reply_markup=None)


@router.callback_query(F.data == "product")
async def product_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    await product_handler(query.message)


async def product_by_id_handler(message: types.Message, product_id: str) -> None:
    product = await ProductService.get_product_by_id(UUID(product_id))

    if not product:
        await message.answer(text="Продукт не найден.")
        return

    keyboard = product_by_keyboard(product_id)
    procudt_text = (
        f"Название: {product.name}\n"
        f"Описание: {product.description}\n"
        f"Количество: {product.quantity} {product.unit_of_measure}\n"
        f"Цена за штуку: {product.price} руб."
    )
    if product.category:
        procudt_text += f"\nКатегория: {product.category.name}\n"

    if product.image_url:
        await message.answer_photo(photo=product.image_url, caption=procudt_text, reply_markup=keyboard)
    else:
        await message.answer(text=procudt_text, reply_markup=keyboard)


@router.callback_query(F.data.startswith('product_'))
async def product_number_callback(query: types.CallbackQuery) -> None:
    """Return a button with a link to the project."""
    product_id = query.data.split("_")[1]  # type: ignore
    logger.info(f"Product ID: {product_id}")
    await product_by_id_handler(query.message, product_id)


@router.callback_query(ProductCallbackData.filter())
async def product_callback_order(query: CallbackQuery, callback_data: ProductCallbackData, state: FSMContext) -> None:
    message_test = "Укажите количество товара"
    await query.message.answer(text=message_test)

    user_data = await state.get_data()
    user_data["product_id"] = str(callback_data.product_id)
    await state.set_data(user_data)
    await state.set_state(UserState.waiting_for_data_quantity)


@router.message(UserState.waiting_for_data_quantity)
async def process_quantity_data(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_dto = await UserService.get_user_by_telegram_id(user_id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    user_data_message = message.text

    if not user_data_message or not user_data_message.isdigit():
        await message.answer("Ошибка: неверный формат данных.")
        return

    quantity = int(user_data_message or 0)
    if quantity <= 0:
        await message.answer("Ошибка: количество товара должно быть больше 0.")
        return

    user_data = await state.get_data()
    product_id = user_data.get("product_id")
    if not product_id:
        await message.answer("Ошибка: не удалось получить идентификатор продукта.")
        return

    product_dto = await ProductService.get_product_by_id(UUID(product_id))
    if not product_dto:
        await message.answer("Ошибка: продукт не найден.")
        return

    if product_dto.quantity and quantity > product_dto.quantity:
        await message.answer("Ошибка: недостаточно товара на складе. На складе осталось: " + str(product_dto.quantity))
        return

    user_data["quantity"] = quantity
    await state.set_data(user_data)
    await state.set_state(UserState.waiting_for_data_address)

    message_test = "Укажите адрес доставки"
    await message.answer(text=message_test)


@router.message(UserState.waiting_for_data_address)
async def process_address_data(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_dto = await UserService.get_user_by_telegram_id(user_id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    user_data_message = message.text
    address = user_data_message
    if not address:
        await message.answer("Ошибка: неверный формат данных.")
        return
    user_data = await state.get_data()
    user_data["address"] = user_data_message
    await state.set_data(user_data)

    await message.answer(text="Рассчитываю стоимость...")
    await asyncio.sleep(2)

    user_data = await state.get_data()
    product_id = user_data.get("product_id")
    quantity = user_data.get("quantity", 0)
    if not product_id:
        await message.answer("Ошибка: не удалось получить идентификатор продукта.")
        return

    product_dto = await ProductService.get_product_by_id(UUID(product_id))
    if not product_dto:
        await message.answer("Ошибка: продукт не найден.")
        return

    total_order_price = await DeliveryService.calculate_delivery_cost(
        price=product_dto.price, quantity=quantity, address=address
    )
    if not total_order_price:
        await message.answer("Ошибка: не удалось рассчитать стоимость доставки.")
        return

    user_data["total_price"] = total_order_price.total_price
    await state.set_data(user_data)

    price_answer = (
        f"Итоговая стоимость заказа:"
        f"\nТовар: {product_dto.name} x {quantity} шт. = {total_order_price.product_price:,.0f} руб."
        f"\nДоставка: {total_order_price.delivery_price:,.0f} руб."
        f"\nНДС (20%): {total_order_price.vat_price:,.0f} руб."
        f"\n<b>Общая сумма: {total_order_price.total_price:,.0f} руб.</b>"
    )
    await message.answer(text=price_answer)
    await message.answer(text="Продолжить оформление заказа?", reply_markup=product_question_keyboard())


@router.callback_query(DeliveryCallbackData.filter())
async def product_delivery_yes(query: CallbackQuery, callback_data: DeliveryCallbackData, state: FSMContext) -> None:
    message_test = "Укажите дату доставки в формате ДД.ММ.ГГГГ"
    await query.message.answer(text=message_test)
    await state.set_state(UserState.waiting_for_data_delivery_date)


@router.message(UserState.waiting_for_data_delivery_date)
async def process_delivery_date_data(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_dto = await UserService.get_user_by_telegram_id(user_id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    error_message = "Ошибка: неверный формат даты доставки. Укажите дату доставки в формате ДД.ММ.ГГГГ"
    user_data_message = message.text
    delivery_date = user_data_message
    if not delivery_date:
        await message.answer(error_message)
        return

    try:
        delivery_date = datetime.strptime(delivery_date, "%d.%m.%Y").date()
    except ValueError:
        await message.answer(error_message)
        return

    if delivery_date < datetime.now().date():
        await message.answer("Ошибка: дата доставки должна быть больше текущей даты.")
        return

    user_data = await state.get_data()
    user_data["delivery_date"] = delivery_date.strftime("%d.%m.%Y")
    await state.set_data(user_data)
    await state.set_state(UserState.waiting_for_data_comment)
    message_test = "Укажите комментарий к заказу"
    await message.answer(text=message_test)


@router.message(UserState.waiting_for_data_comment)
async def process_comment_date_data(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_data_message = message.text
    comment = user_data_message
    if not comment:
        await message.answer("Ошибка: неверный формат данных.")
        return
    user_data["comment"] = user_data_message
    await state.set_data(user_data)

    user_dto = await UserService.get_user_by_telegram_id(message.from_user.id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    product_id = user_data.get("product_id")
    if not product_id:
        await message.answer("Ошибка: не удалось получить идентификатор продукта.")
        return

    product_dto = await ProductService.get_product_by_id(UUID(product_id))
    if not product_dto:
        await message.answer("Ошибка: продукт не найден.")
        return

    delivery_date = datetime.strptime(user_data["delivery_date"], "%d.%m.%Y").date()

    payment_link, payment_id = await PaymentService.create_payment_link(
        user_id=user_dto.id,
        product_id=user_data["product_id"],
        quantity=user_data["quantity"],
        total_price=user_data["total_price"],
    )
    if not payment_link:
        await message.answer("Ошибка: не удалось создать счет на оплату.")
        return

    order_number = await OrderService.generate_order_number()
    order_create_dto = OrderCreateDTO(
        order_number=order_number,
        customer_id=user_dto.id,
        product_id=product_dto.id,
        payment_id=payment_id,
        quantity=user_data["quantity"],
        address=user_data["address"],
        order_date=delivery_date,
        comment=user_data["comment"],
    )
    order_dto = await OrderService.create_order(order_create_dto)
    if not order_dto:
        await message.answer("Ошибка: не удалось создать заказ.")
        return

    confirm_message = (
        "🛒 <b>Проверьте данные вашего заказа:</b>\n\n"
        f"📄 <b>Номер заказа:</b> {str(order_number)}\n"
        f"📦 <b>Товар:</b> {product_dto.name} × {user_data['quantity']} {product_dto.unit_of_measure}\n"
        f"📍 <b>Адрес доставки:</b> {user_data['address']}\n"
        f"📅 <b>Дата доставки:</b> {user_data['delivery_date']}\n"
        f"💬 <b>Комментарий:</b> {user_data['comment'] or 'Нет'}\n\n"
        f"💰 <b>Общая сумма:</b> {user_data['total_price']:,.2f} руб.\n\n"
        f"💳 <b>Ссылка на оплату:</b> <a href='{payment_link}'>Перейти к оплате</a>"
    )
    await message.answer(text=confirm_message, parse_mode="HTML")

    current_time = datetime.now()
    end_time = current_time + timedelta(minutes=WAITING_TIME_MINUTES)
    while datetime.now() < end_time:
        logger.info(f"Current time: {datetime.now()}")
        await asyncio.sleep(5)
        check_order = await OrderService.get_order_by_id(order_id=order_dto.id)
        logger.info(f"Check order: {check_order}")
        if check_order and check_order.order_status.name == "В обработке":
            await message.answer("✅ Ваш заказ успешно принят в обработку.")
            break
    await message.answer("❌ Время на оплату истекло. Пожалуйста, повторите заказ.")
