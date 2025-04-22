# app/admin/views/inventory/nomenclature.py
import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView
from sqlalchemy.orm import joinedload

from app.models.inventory.nomenclature import Nomenclature


class NomenclatureAdminView(ModelView, model=Nomenclature):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True

    name = "Номенклатура"
    name_plural = "Номенклатура"

    column_labels = {
        Nomenclature.category: "Категория",
        Nomenclature.warehouse: "Склад",
        Nomenclature.arrival: "Поступление",
        Nomenclature.orders: "Заказы",
        Nomenclature.name: "Наименование товара",
        Nomenclature.unit_of_measure: "Единица измерения",
        Nomenclature.article_number: "Артикул",
        Nomenclature.price: "Цена",
    }

    column_list = [
        Nomenclature.id,
        Nomenclature.category,
        Nomenclature.warehouse,
        Nomenclature.arrival,
        Nomenclature.name,
        Nomenclature.unit_of_measure,
        Nomenclature.article_number,
        Nomenclature.price,
        Nomenclature.ts_create,
        Nomenclature.ts_modify,
    ]

    column_details_list = [
        Nomenclature.id,
        Nomenclature.category,
        Nomenclature.warehouse,
        Nomenclature.arrival,
        Nomenclature.name,
        Nomenclature.unit_of_measure,
        Nomenclature.article_number,
        Nomenclature.price,
        Nomenclature.ts_create,
        Nomenclature.ts_modify,
        Nomenclature.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
