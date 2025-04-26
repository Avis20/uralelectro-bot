from uuid import UUID
from bot.dto.order import OrderCreateDTO, OrderDTO
from bot.repositories.order import OrderRepository


class OrderService:

    @staticmethod
    async def create_order(order_create_dto: OrderCreateDTO) -> OrderDTO | None:
        order_reader = OrderRepository()
        order_status_id = await order_reader.get_order_new_status_id()
        if order_status_id:
            print('\n\n')
            print(order_status_id)
            print('\n\n')
            order_create_dto.order_status_id = order_status_id
        return await order_reader.create_order(order_create_dto)

    @staticmethod
    async def get_order_by_id(order_id: UUID) -> OrderDTO | None:
        order_reader = OrderRepository()
        return await order_reader.get_order_by_id(order_id)
