from __future__ import annotations

from app.repositories.order.order_repo import IOrderRepository, OrderRepository
from app.repositories.order.order_reader import IOrderReader, OrderReader
from app.uow.base import SQLAlchemyUoW, UnitOfWorkABC


class IOrderUoW(UnitOfWorkABC):
    order_repo: IOrderRepository
    order_reader: IOrderReader


class OrderUoW(SQLAlchemyUoW, IOrderUoW):
    async def __aenter__(self) -> OrderUoW:
        await super().__aenter__()
        self.order_repo = OrderRepository(self.master_session)
        self.order_reader = OrderReader(self.slave_session)
        return self
