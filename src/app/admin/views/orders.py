import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.order.orders import Order


class OrderAdminView(ModelView, model=Order):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Заказ"
    name_plural = "Заказы"

    column_labels = {
        Order.customer: "Заказчик",
        Order.product: "Номенклатура",
        Order.employee: "Сотрудник",
        Order.order_status: "Статус заказа",
        Order.order_date: "Дата заказа",
        Order.actual_delivery_date: "Фактическая дата отгрузки",
    }

    column_list = [
        Order.id,
        Order.order_status,
        Order.customer,
        Order.product,
        Order.employee,
        Order.order_date,
        Order.actual_delivery_date,
    ]

    column_details_list = [
        Order.id,
        Order.customer,
        Order.product,
        Order.employee,
        Order.order_status,
        Order.order_date,
        Order.actual_delivery_date,
        Order.ts_create,
        Order.ts_modify,
        Order.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
        else:
            if not data.get("employee"):
                raise ValueError("Необходимо указать сотрудника")
