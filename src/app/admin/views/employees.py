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
        Employee.first_name: "Имя сотрудника",
        Employee.last_name: "Фамилия сотрудника",
        Employee.position: "Должность сотрудника",
        Employee.phone_number: "Телефон сотрудника",
        Employee.email: "Электронная почта сотрудника",
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