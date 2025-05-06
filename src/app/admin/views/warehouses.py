import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.inventory.warehouses import Warehouse


class WarehouseAdminView(ModelView, model=Warehouse):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Склады"
    name_plural = "Склады"

    column_labels = {
        "arrivals": "Поступления",
        "products": "Товары",
        "name": "Название склада",
        "address": "Адрес склада",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_list = [
        # Warehouse.id,
        Warehouse.name,
        Warehouse.address,
        Warehouse.ts_create,
        Warehouse.ts_modify,
    ]

    column_sortable_list = [
        Warehouse.ts_create,
        Warehouse.name,
        Warehouse.address,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
