from app.dto.order.base import OrderUpdateDTO
from app.uow.order_uow import IOrderUoW


class OrderService:
    def __init__(self, order_uow: IOrderUoW):
        self.order_uow = order_uow

    async def update_order(self, order_update_dto: OrderUpdateDTO):
        async with self.order_uow:
            order_status_id = None
            if order_update_dto.success:
                order_status_id = await self.order_uow.order_reader.get_order_status_by_name("В обработке")
            else:
                order_status_id = await self.order_uow.order_reader.get_order_status_by_name("Закрыт")
            order_update_dto.order_status_id = order_status_id
            await self.order_uow.order_repo.update_order_by_payment_id(order_update_dto)
