import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.customer.customers import Customer


class CustomerAdminView(ModelView, model=Customer):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True

    name = "Заказчик"
    name_plural = "Заказчики"

    column_labels = {
        Customer.contact_person: "Контактное лицо",
        Customer.address: "Адрес",
        Customer.city: "Город",
        Customer.region: "Регион",
        Customer.postal_code: "Почтовый индекс",
        Customer.country: "Страна",
        Customer.phone_number: "Номер телефона",
        Customer.email: "Электронная почта",
        Customer.inn: "ИНН",
    }

    column_list = [
        Customer.id,
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
    ]

    column_details_list = [
        Customer.id,
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