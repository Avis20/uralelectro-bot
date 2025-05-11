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
        "customer": "Заказчик",
        "product": "Товар",
        "employee": "Сотрудник",
        "order_number": "Номер заказа",
        "order_status": "Статус заказа",
        "payment_id": "ID платежа",
        "payment_status": "Статус платежа",
        "order_date": "Дата заказа",
        "address": "Адрес доставки",
        "comment": "Комментарий к заказу",
        "quantity": "Количество товара",
        "actual_delivery_date": "Фактическая дата отгрузки",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_list = [
        # Order.id,
        Order.order_number,
        Order.customer,
        Order.order_status,
        Order.product,
        Order.quantity,
        Order.employee,
        Order.payment_id,
        Order.payment_status,
        Order.address,
        Order.order_date,
        Order.actual_delivery_date,
    ]

    column_sortable_list = [
        # Order.id,
        Order.order_number,
        Order.order_status,
        Order.customer,
        Order.product,
        Order.employee,
        Order.order_date,
        Order.actual_delivery_date,
    ]

    column_details_list = [
        Order.id,
        Order.order_number,
        Order.customer,
        Order.order_status,
        Order.product,
        Order.employee,
        Order.address,
        Order.comment,
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
