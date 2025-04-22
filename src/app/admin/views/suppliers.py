import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.supplier.suppliers import Supplier


class SupplierAdminView(ModelView, model=Supplier):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True

    name = "Поставщики"
    name_plural = "Поставщики"

    column_labels = {
        Supplier.arrivals: "Поставки",
        Supplier.company_name: "Наименование компании",
        Supplier.contact_person: "Контактное лицо",
        Supplier.address: "Адрес",
        Supplier.city: "Город",
        Supplier.region: "Регион",
        Supplier.postal_code: "Почтовый индекс",
        Supplier.phone_number: "Телефон",
        Supplier.email: "Электронная почта",
    }

    column_list = [
        Supplier.id,
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
