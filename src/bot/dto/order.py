from datetime import date
from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO


@dataclass
class OrderCreateDTO(DTO):
    customer_id: UUID
    product_id: UUID
    order_date: date
    quantity: int = 1
    address: str = ""
    order_status_id: UUID | None = None
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None


@dataclass
class OrderDTO(DTO):
    id: UUID
    customer_id: UUID
    product_id: UUID
    order_date: date
    order_status_id: str = "1"
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None
