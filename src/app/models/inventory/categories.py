from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, relationship

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class Category(BaseModel, BaseUUIDMixin):

    __tablename__ = "categories"
    __table_args__ = {"schema": "inventory"}

    def __str__(self) -> str:
        return f"{self.name}"

    name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Наименование категории",
    )

    description: Mapped[str] = Column(
        Text,
        nullable=True,
        init=False,
        comment="Описание категории",
    )

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
        lazy="immediate",
        init=False,
        foreign_keys="[Product.category_id]"
    )
