from uuid import UUID
from app.dto.user.base import UserCreateDTO, UserItemDTO, UserUpdateDTO
from app.exceptions.user import UserException
from app.schemas.request.user import UserCreateSchema, UserUpdateSchema
from app.uow.user_uow import IUserUoW


class UserService:
    def __init__(self, user_uow: IUserUoW):
        self.user_uow = user_uow

    async def create_user(self, user_request: UserCreateSchema) -> UserItemDTO:
        """
        Создание объекта

        Raises:
        """
        user_create_dto = UserCreateDTO(
            name=user_request.name,
            alias=user_request.alias,
        )
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.create_user(user_create_dto)
            if not user_dto:
                raise UserException.UserNotFoundException
            return user_dto

    async def get_user(self, user_id: UUID) -> UserItemDTO:
        """
        Получение объекта

        Raises:
        """
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.get_user_by_id(user_id=user_id)
            if not user_dto:
                raise UserException.UserNotFoundException
            return user_dto

    async def user_update(self, request_user: UserUpdateSchema, user_id: UUID) -> UserItemDTO:
        """
        Обновление объекта

        Raises:
            UserException.UserNotFoundException
        """
        user_update_dto = UserUpdateDTO(
            name=request_user.name,
            alias=request_user.alias,
        )
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.update_user(
                user_id=user_id,
                user_update_dto=user_update_dto,
            )
            if not user_dto:
                raise UserException.UserNotFoundException
            return user_dto

    async def delete_user(self, user_id: UUID) -> UserItemDTO:
        """
        Удаление объекта

        Raises:
            UserException.UserNotFoundException
        """
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.delete_user(user_id=user_id)
            if not user_dto:
                raise UserException.UserNotFoundException
            return user_dto
