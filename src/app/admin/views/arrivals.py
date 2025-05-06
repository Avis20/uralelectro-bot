# app/admin/views/inventory/arrivals.py
import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.inventory.arrivals import Arrival


class ArrivalAdminView(ModelView, model=Arrival):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Поступление"
    name_plural = "Поступления"

    column_labels = {
        "supplier": "Поставщик",
        "warehouse": "Склад",
        "products": "Товары",
        "arrival_date": "Дата поступления",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_sortable_list = [
        Arrival.supplier,
        Arrival.warehouse,
        Arrival.arrival_date,
    ]

    column_list = [
        # Arrival.id,
        Arrival.supplier,
        Arrival.warehouse,
        Arrival.arrival_date,
    ]

    column_details_list = [
        Arrival.id,
        Arrival.supplier,
        Arrival.warehouse,
        Arrival.arrival_date,
        Arrival.ts_create,
        Arrival.ts_modify,
        Arrival.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
