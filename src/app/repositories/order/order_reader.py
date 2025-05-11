from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import select

from app.dto.order.base import OrderDTO
from app.models.order.status import OrderStatus
from app.repositories.base import SQLAlchemyRepository
from app.models.order.orders import Order


class IOrderReader(ABC):
    @abstractmethod
    async def get_order_by_id(self, order_id: UUID) -> OrderDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def get_order_status_by_name(self, name: str) -> UUID | None:
        raise NotImplementedError


class OrderReader(SQLAlchemyRepository, IOrderReader):
    async def get_order_by_id(self, order_id: UUID) -> OrderDTO | None:
        stmt = select(Order).filter_by(id=order_id)
        result = await self._session.execute(stmt)
        if order_db := result.scalar():
            order = OrderDTO.model_to_dto(order_db)
            return order
        return None

    async def get_order_status_by_name(self, name: str) -> UUID | None:
        stmt = select(OrderStatus).filter_by(name=name)
        result = await self._session.execute(stmt)
        if order_status := result.scalar():
            return order_status.id
        return None
