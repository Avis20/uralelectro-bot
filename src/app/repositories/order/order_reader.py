from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import select

from app.dto.order.base import OrderDTO
from app.repositories.base import SQLAlchemyRepository
from app.models.order.orders import Order


class IOrderReader(ABC):
    @abstractmethod
    async def get_order_by_id(self, order_id: UUID) -> OrderDTO | None:
        raise NotImplementedError


class OrderReader(SQLAlchemyRepository, IOrderReader):
    async def get_order_by_id(self, order_id: UUID) -> OrderDTO | None:
        stmt = select(Order).filter_by(id=order_id)
        result = await self._session.execute(stmt)
        if order_db := result.scalar():
            order = OrderDTO.model_to_dto(order_db)
            return order
        return None
