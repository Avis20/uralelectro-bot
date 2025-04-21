from pydantic import BaseModel

from app.schemas.request.base import PaginationRequestSchema


class UserCreateSchema(BaseModel):
    name: str
    alias: str


class UserUpdateSchema(BaseModel):
    name: str | None = None
    alias: str | None = None


class UserListSchema(PaginationRequestSchema):
    pass
