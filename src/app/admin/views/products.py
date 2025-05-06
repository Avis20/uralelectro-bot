import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.inventory.products import Product


class ProductAdminView(ModelView, model=Product):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Товар"
    name_plural = "Товары"

    column_labels = {
        "category": "Категория",
        "warehouse": "Склад",
        "arrival": "Поступление",
        "orders": "Заказы",
        "article_number": "Артикул",
        "name": "Наименование товара",
        "description": "Описание товара",
        "unit_of_measure": "Единица измерения",
        "quantity": "Количество товара",
        "image_url": "Ссылка на изображение товара",
        "price": "Цена",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_list = [
        # Product.id,
        Product.article_number,
        Product.name,
        Product.description,
        Product.unit_of_measure,
        Product.quantity,
        Product.price,
        Product.category,
        Product.warehouse,
        Product.arrival,
        Product.image_url,
        Product.ts_create,
        Product.ts_modify,
    ]

    column_sortable_list = [
        Product.article_number,
        Product.name,
        Product.description,
        Product.quantity,
        Product.price,
        Product.ts_create,
    ]

    column_details_list = [
        Product.id,
        Product.article_number,
        Product.name,
        Product.description,
        Product.unit_of_measure,
        Product.quantity,
        Product.price,
        Product.category,
        Product.warehouse,
        Product.arrival,
        Product.image_url,
        Product.ts_create,
        Product.ts_modify,
        Product.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
