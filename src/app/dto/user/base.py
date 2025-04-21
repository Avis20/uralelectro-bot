from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.dto.base import DTO


@dataclass
class UserCreateDTO(DTO):
    name: str
    alias: str


@dataclass
class UserUpdateDTO(DTO):
    name: str | None = None
    alias: str | None = None


@dataclass
class UserItemDTO(DTO):
    id: UUID
    name: str
    alias: str
    ts_create: datetime
    ts_modify: datetime
