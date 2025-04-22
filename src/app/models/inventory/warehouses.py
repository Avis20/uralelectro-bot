# Склады

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, relationship, selectinload

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class Warehouse(BaseModel, BaseUUIDMixin):

    __tablename__ = "warehouses"
    __table_args__ = {"schema": "inventory"}

    def __str__(self) -> str:
        return f"{self.name}"

    name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Название склада",
    )

    address: Mapped[str] = Column(
        Text,
        nullable=False,
        init=False,
        comment="Адрес склада",
    )

    arrivals: Mapped[list["Arrival"]] = relationship(
        "Arrival",
        back_populates="warehouse",
        lazy="immediate",
        init=False,
        foreign_keys="[Arrival.warehouse_id]",
    )

    nomenclatures: Mapped[list["Nomenclature"]] = relationship(
        "Nomenclature",
        back_populates="warehouse",
        lazy="immediate",
        init=False,
        foreign_keys="[Nomenclature.warehouse_id]",
    )
