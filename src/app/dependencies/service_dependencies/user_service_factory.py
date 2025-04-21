from typing import Annotated
from fastapi import Depends

from app.services.user.base import UserService
from app.dependencies import UserUoWDep


def create_user_service(user_uow: UserUoWDep):
    return UserService(user_uow)


UserServiceDep = Annotated[UserService, Depends(create_user_service)]
