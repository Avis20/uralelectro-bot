from typing import Annotated
from fastapi import Depends

from app.services.order.base import OrderService
from app.dependencies import OrderUoWDep


def create_order_service(order_uow: OrderUoWDep):
    return OrderService(order_uow)


OrderServiceDep = Annotated[OrderService, Depends(create_order_service)]
