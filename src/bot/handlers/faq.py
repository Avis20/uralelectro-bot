from aiogram import F, Router, types
from aiogram.filters import Command

router = Router(name="faq")
faq_data = {
    "Как оформить заказ?": "Для оформления заказа воспользуйтесь командой /products...",
    "Как узнать статус моего заказа?": "Чтобы узнать статус заказа, используйте команду /status...",
    "Как узнать контакты компании?": "Контакты компании: +7 (343) 272-30-69, 8 (912) 660-63-90, uek2010@mail.ru",
    "Как узнать адрес компании?": "Адрес компании: 620050 Свердловская обл.,г. Екатеринбург,ул. Монтажников, 26А, офис 109",
    "Как связаться с поддержкой?": "Для связи с поддержкой используйте команду /support. Опишите вашу проблему, и менеджер свяжется с вами в ближайшее время.",
    "Как узнать часы работы компании?": "Часы работы компании: C понедельника по пятницу работаем с 9:00 до 18:00, Суббота, Воскресенье — выходные дни",
    "Как рассчитать стоимость заказа с доставкой?": "Используйте команду /calculator, чтобы рассчитать стоимость заказа. Укажите товар, количество и адрес доставки, а бот автоматически произведет расчет.",
}


@router.message(Command(commands=["faq"]))
async def faq_handler(message: types.Message) -> None:
    """FAQ about bot."""
    faq_text = ""
    i = 1
    for q, a in faq_data.items():
        faq_text += f"<b>{i}. {q}</b>\n{a}\n\n"
        i += 1
    await message.answer(faq_text)


@router.callback_query(F.data == "faq")
async def faq_callback(query: types.CallbackQuery) -> None:
    await faq_handler(query.message)
