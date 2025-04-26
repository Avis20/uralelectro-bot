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
        Product.category: "Категория",
        Product.warehouse: "Склад",
        Product.arrival: "Поступление",
        Product.orders: "Заказы",
        Product.article_number: "Артикул",
        Product.name: "Наименование товара",
        Product.description: "Описание товара",
        Product.unit_of_measure: "Единица измерения",
        Product.quantity: "Количество товара",
        Product.image_url: "Ссылка на изображение товара",
        Product.price: "Цена",
    }

    column_list = [
        # Product.id,
        Product.name,
        Product.description,
        Product.unit_of_measure,
        Product.quantity,
        Product.price,
        Product.category,
        Product.warehouse,
        Product.arrival,
        Product.article_number,
        Product.ts_create,
        Product.ts_modify,
    ]

    column_details_list = [
        Product.id,
        Product.category,
        Product.warehouse,
        Product.arrival,
        Product.name,
        Product.unit_of_measure,
        Product.article_number,
        Product.price,
        Product.ts_create,
        Product.ts_modify,
        Product.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
