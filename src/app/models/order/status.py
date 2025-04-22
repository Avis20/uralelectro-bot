from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class OrderStatus(BaseModel, BaseUUIDMixin):

    __tablename__ = "status"
    __table_args__ = {"schema": "order"}

    def __str__(self) -> str:
        return f"{self.name}"

    name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Наименование статуса",
    )

    description: Mapped[str] = Column(
        Text,
        nullable=True,
        init=False,
        comment="Описание статуса",
    )
