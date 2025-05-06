import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.supplier.suppliers import Supplier


class SupplierAdminView(ModelView, model=Supplier):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Поставщики"
    name_plural = "Поставщики"

    column_labels = {
        "arrivals": "Поставки",
        "company_name": "Наименование компании",
        "contact_person": "Контактное лицо",
        "address": "Адрес",
        "city": "Город",
        "region": "Регион",
        "postal_code": "Почтовый индекс",
        "phone_number": "Телефон",
        "email": "Электронная почта",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_sortable_list = [
        Supplier.company_name,
        Supplier.contact_person,
        Supplier.address,
        Supplier.city,
        Supplier.region,
        Supplier.postal_code,
        Supplier.phone_number,
        Supplier.email,
        Supplier.ts_create,
    ]

    column_list = [
        # Supplier.id,
        Supplier.company_name,
        Supplier.contact_person,
        Supplier.address,
        Supplier.city,
        Supplier.region,
        Supplier.postal_code,
        Supplier.phone_number,
        Supplier.email,
        Supplier.ts_create,
        Supplier.ts_modify,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
