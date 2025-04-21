from typing import Annotated
from fastapi import Depends

from app.dependencies import MasterSessionMakerDep, SlaveSessionMakerDep
from app.uow.user_uow import IUserUoW, UserUoW


def create_user_uow(
    master_session_maker: MasterSessionMakerDep,
    slave_session_maker: SlaveSessionMakerDep,
):
    return UserUoW(master_session_maker, slave_session_maker)


UserUoWDep = Annotated[IUserUoW, Depends(create_user_uow)]
