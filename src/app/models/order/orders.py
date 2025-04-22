from datetime import date
import uuid
from sqlalchemy import Date
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel, RestrictForeignKey
from app.models.customer.customers import Customer
from app.models.employee.employees import Employee
from app.models.inventory.products import Product
from app.models.mixins import BaseUUIDMixin
from app.models.order.status import OrderStatus


class Order(BaseModel, BaseUUIDMixin):

    __tablename__ = "orders"
    __table_args__ = {"schema": "order"}

    def __str__(self) -> str:
        return f"Заказ №{self.id}"

    customer_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Customer.id, name="customers_customer_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор заказчика",
    )

    product_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Product.id, name="inventory_product_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор номенклатуры",
    )

    employee_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Employee.id, name="employee_employees_id_fkey"),
        nullable=True,
        init=False,
        comment="Идентификатор сотрудника",
    )

    order_status_id: Mapped[str] = Column(
        RestrictForeignKey(OrderStatus.id, name="order_status_id_fkey"),
        nullable=False,
        init=False,
        comment="Статус заказа",
    )

    order_date: Mapped[date] = Column(
        Date,
        nullable=False,
        init=False,
        comment="Дата заказа",
    )

    actual_delivery_date: Mapped[date] = Column(
        Date,
        nullable=True,
        init=False,
        comment="Фактическая дата отгрузки",
    )

    order_status: Mapped["OrderStatus"] = relationship(
        "OrderStatus",
        lazy="immediate",
        init=False,
        foreign_keys=[order_status_id],
    )

    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="orders",
        lazy="immediate",
        init=False,
        foreign_keys=[customer_id],
    )

    product: Mapped["Product"] = relationship(
        "Product",
        back_populates="orders",
        lazy="immediate",
        init=False,
        foreign_keys=[product_id],
    )

    employee: Mapped["Employee"] = relationship(
        "Employee",
        back_populates="orders",
        lazy="immediate",
        init=False,
        foreign_keys=[employee_id],
    )
