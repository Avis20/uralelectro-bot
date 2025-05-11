import random

from loguru import logger
from uuid import UUID
from bot.dto.order import OrderCreateDTO, OrderDTO
from bot.repositories.order import OrderRepository


class OrderService:

    @staticmethod
    async def get_orders_by_user_id(user_id: UUID) -> list[OrderDTO] | None:
        order_reader = OrderRepository()
        return await order_reader.get_order_list(user_id)

    @staticmethod
    async def generate_order_number() -> str:
        rand_str = "".join([chr(random.randint(65, 90)) for _ in range(3)])
        order_number = f"{rand_str}-{int(random.random() * 100000000)}"
        return order_number

    @staticmethod
    async def create_order(order_create_dto: OrderCreateDTO) -> OrderDTO | None:
        order_reader = OrderRepository()
        order_status_id = await order_reader.get_order_new_status_id()
        if order_status_id:
            order_create_dto.order_status_id = order_status_id
        logger.info(f"\n\norder_create_dto: {order_create_dto}")
        return await order_reader.create_order(order_create_dto)

    @staticmethod
    async def get_order_by_id(order_id: UUID) -> OrderDTO | None:
        order_reader = OrderRepository()
        return await order_reader.get_order_by_id(order_id)
