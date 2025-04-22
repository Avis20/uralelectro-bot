from datetime import date
import uuid
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel, RestrictForeignKey
from app.models.customer.customers import Customer
from app.models.employee.employees import Employee
from app.models.inventory.nomenclature import Nomenclature
from app.models.mixins import BaseUUIDMixin


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

    nomenclature_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Nomenclature.id, name="inventory_nomenclature_id_fkey"),
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

    order_status: Mapped[str] = Column(
        String,
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

    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="orders",
        lazy="immediate",
        init=False,
        foreign_keys=[customer_id],
    )

    nomenclature: Mapped["Nomenclature"] = relationship(
        "Nomenclature",
        back_populates="orders",
        lazy="immediate",
        init=False,
        foreign_keys=[nomenclature_id],
    )

    employee: Mapped["Employee"] = relationship(
        "Employee",
        back_populates="orders",
        lazy="immediate",
        init=False,
        foreign_keys=[employee_id],
    )
