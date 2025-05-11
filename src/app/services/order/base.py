from app.dto.order.base import OrderUpdateDTO
from app.uow.order_uow import IOrderUoW


class OrderService:
    def __init__(self, order_uow: IOrderUoW):
        self.order_uow = order_uow

    async def update_order(self, order_update_dto: OrderUpdateDTO):
        async with self.order_uow:
            await self.order_uow.order_repo.update_order_by_payment_id(order_update_dto)
