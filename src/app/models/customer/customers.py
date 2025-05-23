# app/models/customer/customers.py
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class Customer(BaseModel, BaseUUIDMixin):

    __tablename__ = "customers"
    __table_args__ = {"schema": "customer"}

    def __str__(self) -> str:
        return f"{self.contact_person}"

    telegram_user_id: Mapped[int] = Column(
        Integer,
        nullable=True,
        init=False,
        comment="Telegram user id",
    )

    contact_person: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Контактное лицо",
    )

    address: Mapped[str] = Column(
        Text,
        nullable=True,
        init=False,
        comment="Адрес",
    )

    city: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Город",
    )

    region: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Регион",
    )

    postal_code: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Почтовый индекс",
    )

    country: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Страна",
    )

    phone_number: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Телефон",
    )

    email: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="Электронная почта",
    )

    inn: Mapped[str] = Column(
        String,
        nullable=True,
        init=False,
        comment="ИНН",
    )

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="customer",
        lazy="immediate",
        init=False,
        foreign_keys="[Order.customer_id]",
        cascade="all, delete-orphan",
    )
