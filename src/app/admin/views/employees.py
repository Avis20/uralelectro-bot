# app/admin/views/inventory/categories.py
import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.employee.employees import Employee


class EmployeeAdminView(ModelView, model=Employee):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

    name = "Сотрудник"
    name_plural = "Сотрудники"

    column_labels = {
        "first_name": "Имя сотрудника",
        "last_name": "Фамилия сотрудника",
        "position": "Должность сотрудника",
        "phone_number": "Телефон сотрудника",
        "email": "Электронная почта сотрудника",
        "ts_create": "Дата и время создания",
        "ts_modify": "Дата и время обновления",
        "is_deleted": "Флаг, что запись удалена",
    }

    column_list = [
        # Employee.id,
        Employee.first_name,
        Employee.last_name,
        Employee.position,
        Employee.phone_number,
        Employee.email,
        Employee.ts_create,
        Employee.ts_modify,
    ]

    column_sortable_list = [
        Employee.first_name,
        Employee.last_name,
        Employee.position,
        Employee.phone_number,
        Employee.email,
        Employee.ts_create,
    ]

    column_details_list = [
        Employee.id,
        Employee.first_name,
        Employee.last_name,
        Employee.position,
        Employee.ts_create,
        Employee.ts_modify,
        Employee.is_deleted,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
