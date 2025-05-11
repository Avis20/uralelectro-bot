from datetime import date
from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO


@dataclass
class OrderStatusDTO(DTO):
    id: UUID
    name: str


@dataclass
class OrderUpdateDTO(DTO):
    payment_id: str
    status: str
    success: bool | None = False


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
    order_status: OrderStatusDTO

    order_status_id: UUID | None = None
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None
