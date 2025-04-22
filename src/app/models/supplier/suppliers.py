# Поставщики

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, relationship, selectinload

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class Supplier(BaseModel, BaseUUIDMixin):

    __tablename__ = "suppliers"
    __table_args__ = {"schema": "supplier"}

    def __str__(self) -> str:
        return f"{self.company_name}"

    company_name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Наименование компании",
    )

    contact_person: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Контактное лицо",
    )

    address: Mapped[str] = Column(
        Text,
        nullable=False,
        init=False,
        comment="Адрес",
    )

    city: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Город",
    )

    region: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Регион",
    )

    postal_code: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Почтовый индекс",
    )

    phone_number: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Телефон",
    )

    email: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Электронная почта",
    )

    arrivals: Mapped[list["Arrival"]] = relationship(
        "Arrival",
        back_populates="supplier",
        lazy="immediate",
        init=False,
        foreign_keys="[Arrival.supplier_id]"
    )
