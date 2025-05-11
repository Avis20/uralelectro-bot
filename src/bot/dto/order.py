from datetime import date
from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO
from bot.dto.product import ProductDTO


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
    payment_id: UUID | None = None
    order_status_id: UUID | None = None
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None


@dataclass
class OrderStatusDTO(DTO):
    id: UUID
    name: str


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
    product: ProductDTO
    order_status: OrderStatusDTO

    order_status_id: UUID | None = None
    employee_id: UUID | None = None
    actual_delivery_date: date | None = None
