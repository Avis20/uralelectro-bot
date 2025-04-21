from aiogram import F, Router, types
from aiogram.filters import Command

router = Router(name="info")


@router.message(Command(commands=["info", "help", "about"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""
    message_text = (
        "ООО ТД «УралЭнергоКомплект»\n"
        "Юридический адрес: 620050 Свердловская обл.,г. Екатеринбург,ул. Монтажников, 26А, офис 109\n"
        "Фактический адрес: 624187 Свердловская обл. Невьянский р-н п.Ребристый ул. Свердлова, 26\n"
        "Телефоны: Номер для связи: +7 (343) 272-30-69\n"
        "Отдел снабжения: 8 (912) 660-63-90\n"
        "Руководство: +7 (922) 117-84-03\n"
        "Email: uek2010@mail.ru\n"
        "Часы работы: C понедельника по пятницу работаем с 9:00 до 18:00\n"
        "Обеденный перерыв: с 12:00 до 13:00\n"
        "Суббота, Воскресенье — выходные дни\n"
    )
    await message.answer(message_text)


@router.callback_query(F.data == "info")
async def info_callback(query: types.CallbackQuery) -> None:
    await info_handler(query.message)
