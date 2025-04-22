# app/admin/views/inventory/arrivals.py
import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView
from sqlalchemy.orm import joinedload

from app.models.inventory.arrivals import Arrival


class ArrivalAdminView(ModelView, model=Arrival):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True

    name = "Поступление"
    name_plural = "Поступления"

    column_labels = {
        Arrival.supplier: "Поставщик",
        Arrival.warehouse: "Склад",
        Arrival.nomenclatures: "Товары",
        Arrival.arrival_date: "Дата поступления",
    }

    column_list = [
        Arrival.id,
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
