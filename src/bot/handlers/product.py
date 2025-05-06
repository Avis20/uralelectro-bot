from datetime import datetime
from uuid import UUID
from aiogram import F, Router, types

from aiogram.types import CallbackQuery

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loguru import logger

from bot.callback.product import ProductCallbackData
from bot.dto.order import OrderCreateDTO
from bot.keyboards.inline.product import product_by_keyboard, product_keyboard
from bot.services.order_service import OrderService
from bot.services.product_service import ProductService
from bot.services.user_service import UserService

router = Router(name="product")


class UserState(StatesGroup):
    waiting_for_data = State()


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
        f"Количество: {product.quantity}\n"
        f"Цена: {product.price} руб."
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
    message_test = "Укажите количество товара, адрес доставки и дату доставки в формате\n" "кол-во:адрес:ДД.ММ.ГГГГ"
    await query.message.answer(text=message_test)

    user_data = await state.get_data()
    user_data["product_id"] = str(callback_data.product_id)
    await state.set_data(user_data)
    await state.set_state(UserState.waiting_for_data)


@router.message(UserState.waiting_for_data)
async def process_data(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data_message = message.text
    user_data_message = message.text.split(":")
    if len(user_data_message) != 3:
        await message.answer("Неверный формат данных. Пожалуйста, введите данные в формате\nкол-во:адрес:ДД.ММ.ГГГГ")
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

    user_dto = await UserService.get_user_by_telegram_id(user_id)
    if not user_dto:
        await message.answer("Ошибка: пользователь не найден.")
        return

    quantity = int(user_data_message[0])
    address = user_data_message[1]
    delivery_date = user_data_message[2]
    try:
        delivery_date = datetime.strptime(delivery_date, "%d.%m.%Y").date()
    except ValueError:
        await message.answer("Ошибка: неверный формат даты доставки.")
        return

    if delivery_date < datetime.now().date():
        await message.answer("Ошибка: дата доставки должна быть больше текущей даты.")
        return

    if quantity <= 0:
        await message.answer("Ошибка: количество товара должно быть больше 0.")
        return

    if product_dto.quantity and quantity > product_dto.quantity:
        await message.answer("Ошибка: недостаточно товара на складе.")
        return

    order_create_dto = OrderCreateDTO(
        customer_id=user_dto.id,
        product_id=product_dto.id,
        quantity=quantity,
        address=address,
        order_date=delivery_date,
    )
    order_create_dto = await OrderService.create_order(order_create_dto)

    await message.answer("Спасибо за ваш заказ!")
