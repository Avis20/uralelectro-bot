from typing import Annotated
from fastapi import Depends

from app.dependencies import MasterSessionMakerDep, SlaveSessionMakerDep
from app.uow.order_uow import IOrderUoW, OrderUoW


def create_order_uow(
    master_session_maker: MasterSessionMakerDep,
    slave_session_maker: SlaveSessionMakerDep,
):
    return OrderUoW(master_session_maker, slave_session_maker)


OrderUoWDep = Annotated[IOrderUoW, Depends(create_order_uow)]
