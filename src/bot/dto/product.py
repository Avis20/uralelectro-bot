from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO


@dataclass
class CategoryDTO(DTO):
    id: UUID
    name: str


@dataclass
class ProductDTO(DTO):
    id: UUID
    name: str
    price: float
    unit_of_measure: str
    image_url: str
    description: str | None = None
    quantity: int | None = None

    category: CategoryDTO | None = None
