from sqlalchemy import String
from sqlalchemy.orm import Mapped

from app.models.base import Column, BaseModel
from app.models.mixins import BaseUUIDMixin


class UserItem(BaseModel, BaseUUIDMixin):

    __tablename__ = "items"
    __table_args__ = {"schema": "user"}

    name: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Название объекта",
    )

    alias: Mapped[str] = Column(
        String,
        nullable=False,
        init=False,
        comment="Алиас объекта",
    )
