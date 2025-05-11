import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.customer.customers import Customer


class CustomerAdminView(ModelView, model=Customer):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Заказчик"
    name_plural = "Заказчики"

    column_labels = {
        "telegram_user_id": "Telegram ID",
        "contact_person": "Контактное лицо",
        "address": "Адрес",
        "city": "Город",
        "region": "Регион",
        "postal_code": "Почтовый индекс",
        "country": "Страна",
        "phone_number": "Номер телефона",
        "email": "Электронная почта",
        "inn": "ИНН",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_list = [
        # Customer.id,
        Customer.contact_person,
        Customer.telegram_user_id,
        Customer.address,
        Customer.city,
        Customer.region,
        Customer.postal_code,
        Customer.country,
        Customer.phone_number,
        Customer.email,
        Customer.inn,
        Customer.ts_create,
        Customer.ts_modify,
    ]

    column_sortable_list = [
        Customer.contact_person,
        Customer.telegram_user_id,
        Customer.address,
        Customer.city,
        Customer.region,
        Customer.postal_code,
        Customer.country,
        Customer.phone_number,
        Customer.email,
        Customer.inn,
        Customer.ts_create,
    ]

    column_details_list = [
        Customer.id,
        Customer.telegram_user_id,
        Customer.contact_person,
        Customer.address,
        Customer.city,
        Customer.region,
        Customer.postal_code,
        Customer.country,
        Customer.phone_number,
        Customer.email,
        Customer.inn,
        Customer.ts_create,
        Customer.ts_modify,
        Customer.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
