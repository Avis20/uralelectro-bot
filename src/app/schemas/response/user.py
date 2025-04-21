from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.response.base import ResponseSchema


class UserItemResponseSchema(BaseModel):
    id: UUID
    name: str | None
    alias: str | None
    ts_create: datetime
    ts_modify: datetime


class UserResponseSchema(ResponseSchema):
    item: UserItemResponseSchema


class UserListResponseSchema(ResponseSchema):
    list: list[UserItemResponseSchema]
