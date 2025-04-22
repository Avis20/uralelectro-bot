import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.inventory.warehouses import Warehouse


class WarehouseAdminView(ModelView, model=Warehouse):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True

    name = "Склады"
    name_plural = "Склады"

    column_labels = {
        Warehouse.arrivals: "Поступления",
        Warehouse.nomenclatures: "Товары",
        Warehouse.name: "Название склада",
        Warehouse.address: "Адрес склада",
    }

    column_list = [
        Warehouse.name,
        Warehouse.address,
        Warehouse.id,
        Warehouse.ts_create,
        Warehouse.ts_modify,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
