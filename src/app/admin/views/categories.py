import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.inventory.categories import Category


class CategoryAdminView(ModelView, model=Category):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Категория товаров"
    name_plural = "Категории товаров"

    column_labels = {
        "products": "Товары",
        "name": "Наименование категории",
        "description": "Описание категории",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_sortable_list = [
        Category.name,
        Category.description,
        Category.ts_create,
    ]

    column_list = [
        # Category.id,
        Category.name,
        Category.description,
        Category.ts_create,
        Category.ts_modify,
    ]

    column_details_list = [
        Category.products,
        Category.id,
        Category.name,
        Category.description,
        Category.ts_create,
        Category.ts_modify,
        Category.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
