import uuid
from typing import Any

from fastapi import Request
from sqladmin import ModelView

from app.models.user.items import UserItem


class UserAdminView(ModelView, model=UserItem):
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True

    column_list = [
        UserItem.id,
        UserItem.name,
    ]
    # Исключить редактирование полей
    form_excluded_columns = [
        UserItem.id,
        UserItem.is_deleted,
        UserItem.ts_create,
        UserItem.ts_modify,
    ]

    async def on_model_change(self, data: dict, model: Any, is_created: bool, request: Request):
        if is_created:
            model.id = uuid.uuid4()
