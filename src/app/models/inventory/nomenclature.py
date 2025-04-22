# Номенклатура

import uuid
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel, RestrictForeignKey
from app.models.mixins import BaseUUIDMixin
from app.models.inventory.arrivals import Arrival
from app.models.inventory.categories import Category
from app.models.inventory.warehouses import Warehouse


class Nomenclature(BaseModel, BaseUUIDMixin):

    __tablename__ = "nomenclature"
    __table_args__ = {"schema": "inventory"}

    def __str__(self) -> str:
        return f"{self.name}"

    category_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Category.id, name="inventory_category_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор категории",
    )

    warehouse_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Warehouse.id, name="inventory_warehouse_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор склада",
    )

    arrival_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Arrival.id, name="inventory_arrival_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор поступления",
    )

    name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Наименование товара",
    )

    unit_of_measure: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Единица измерения товара",
    )

    article_number: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Артикул товара",
    )

    price: Mapped[float] = Column(
        Numeric(10, 2),
        nullable=False,
        init=False,
        comment="Цена товара",
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="nomenclatures",
        lazy="immediate",
        init=False,
        foreign_keys=[category_id],
    )

    warehouse: Mapped["Warehouse"] = relationship(
        "Warehouse",
        back_populates="nomenclatures",
        lazy="immediate",
        init=False,
        foreign_keys=[warehouse_id],
    )

    arrival: Mapped["Arrival"] = relationship(
        "Arrival",
        back_populates="nomenclatures",
        lazy="immediate",
        init=False,
        foreign_keys=[arrival_id],
    )

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="nomenclature",
        lazy="immediate",
        init=False,
        foreign_keys="[Order.nomenclature_id]",
        cascade="all, delete-orphan",
    )
