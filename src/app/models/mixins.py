import uuid
from datetime import datetime, timezone

from sqlalchemy import func, TIMESTAMP, Boolean, Integer
from sqlalchemy.sql import expression
from sqlalchemy.orm import Mapped, MappedAsDataclass
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Column


class IdIntegerMixin(MappedAsDataclass):
    __abstract__ = True

    id: Mapped[int] = Column(
        Integer,
        init=False,
        nullable=False,
        primary_key=True,
        comment="ID",
    )


class IdUUIDMixin(MappedAsDataclass):
    __abstract__ = True

    id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        nullable=False,
        primary_key=True,
        comment="ID",
    )


class TsCreateMixin(MappedAsDataclass):
    __abstract__ = True

    ts_create: Mapped[datetime] = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        comment="Дата и время создания записи",
    )


class TsModifyMixin(MappedAsDataclass):
    __abstract__ = True

    ts_modify: Mapped[datetime] = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        comment="Дата и время обновления",
    )


class IsDeletedMixin(MappedAsDataclass):
    __abstract__ = True

    is_deleted: Mapped[bool] = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default=expression.false(),
        comment="Флаг, что запись удалена",
    )


class TriggerOffMixin(MappedAsDataclass):
    __abstract__ = True

    _trigger_off: Mapped[bool] = Column(
        Boolean,
        nullable=True,
        default=None,
        server_default=expression.null(),
    )


class BaseIntegerMixin(IdIntegerMixin, TsCreateMixin, TsModifyMixin, IsDeletedMixin, TriggerOffMixin):
    __abstract__ = True


class BaseUUIDMixin(IdUUIDMixin, TsCreateMixin, TsModifyMixin, IsDeletedMixin, TriggerOffMixin):
    __abstract__ = True
