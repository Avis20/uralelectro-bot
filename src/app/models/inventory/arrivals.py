# Поступления

from datetime import date
import uuid
from sqlalchemy import Date
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel, RestrictForeignKey
from app.models.inventory.warehouses import Warehouse
from app.models.mixins import BaseUUIDMixin
from app.models.supplier.suppliers import Supplier


class Arrival(BaseModel, BaseUUIDMixin):

    __tablename__ = "arrivals"
    __table_args__ = {"schema": "inventory"}

    def __str__(self) -> str:
        return f"{self.supplier.company_name}: {self.warehouse} - {self.arrival_date}"

    supplier_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Supplier.id, name="suppliers_supplier_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор поставщика",
    )

    warehouse_id: Mapped[uuid.UUID] = Column(
        RestrictForeignKey(Warehouse.id, name="inventory_warehouse_id_fkey"),
        nullable=False,
        init=False,
        comment="Идентификатор склада",
    )

    arrival_date: Mapped[date] = Column(
        Date,
        nullable=False,
        init=False,
        comment="Дата поступления",
    )

    supplier: Mapped["Supplier"] = relationship(
        "Supplier",
        back_populates="arrivals",
        init=False,
        lazy="immediate",
        foreign_keys=[supplier_id],
    )

    warehouse: Mapped["Warehouse"] = relationship(
        "Warehouse",
        back_populates="arrivals",
        init=False,
        lazy="immediate",
        foreign_keys=[warehouse_id],
    )

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="arrival",
        init=False,
        lazy="immediate",
        foreign_keys="[Product.arrival_id]",
    )
