from datetime import date
from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO


@dataclass
class TotalOrderPrice(DTO):
    product_price: float
    delivery_price: float
    vat_price: float
    total_price: float


@dataclass
class OrderCreateDTO(DTO):
    order_number: str
    customer_id: UUID
    product_id: UUID
    order_date: date
    quantity: int = 1
    address: str = ""
    comment: str = ""
    order_status_id: UUID | None = None
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None


@dataclass
class OrderDTO(DTO):
    id: UUID
    order_number: str
    customer_id: UUID
    product_id: UUID
    order_date: date
    quantity: int
    address: str
    comment: str
    order_status_id: str = "1"
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None
