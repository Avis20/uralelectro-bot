from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class Employee(BaseModel, BaseUUIDMixin):

    __tablename__ = "employees"
    __table_args__ = {"schema": "employee"}

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    first_name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Имя сотрудника",
    )

    last_name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Фамилия сотрудника",
    )

    position: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Должность сотрудника",
    )

    phone_number: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Телефон сотрудника",
    )

    email: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Электронная почта сотрудника",
    )

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="employee",
        lazy="immediate",
        init=False,
        foreign_keys="[Order.employee_id]",
        cascade="all, delete-orphan",
    )