from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import update

from app.dto.order.base import OrderDTO, OrderUpdateDTO
from app.repositories.base import SQLAlchemyRepository
from app.repositories.order.order_reader import IOrderReader, OrderReader
from app.models.order.orders import Order


class IOrderRepository(IOrderReader, ABC):
    @abstractmethod
    async def update_order(self, order_id: UUID, order_update_dto: OrderUpdateDTO) -> OrderDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def update_order_by_payment_id(self, order_update_dto: OrderUpdateDTO) -> bool | None:
        raise NotImplementedError


class OrderRepository(IOrderRepository, OrderReader, SQLAlchemyRepository):

    async def update_order_by_payment_id(self, order_update_dto: OrderUpdateDTO) -> bool | None:
        stmt = (
            update(Order)
            .filter_by(payment_id=order_update_dto.payment_id)
            .values(payment_status=order_update_dto.status)
            .returning(Order)
        )
        result = await self._session.execute(stmt)
        if order := result.scalar():
            return True
            # return OrderDTO.model_to_dto(order)
        return None

    async def update_order(self, order_id: UUID, order_update_dto: OrderUpdateDTO) -> OrderDTO | None:
        order_dto = await self.get_order_by_id(order_id=order_id)
        if not order_dto:
            return None

        data = order_update_dto.as_dict(exclude_none=True)
        stmt = update(Order).filter_by(id=order_id).values(data).returning(Order)
        result = await self._session.execute(stmt)
        if order := result.scalar():
            return OrderDTO.model_to_dto(order)
        return None
