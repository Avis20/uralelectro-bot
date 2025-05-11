from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO


@dataclass
class UserCreateDTO(DTO):
    telegram_user_id: int
    contact_person: str | None = None


@dataclass
class UserUpdateDTO(DTO):
    user_id: UUID
    phone_number: str | None = None


@dataclass
class UserDTO(DTO):
    id: UUID
    telegram_user_id: int
    contact_person: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone_number: str | None = None
    email: str | None = None
    inn: str | None = None
