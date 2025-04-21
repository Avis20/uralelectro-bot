from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import insert, delete, update

from app.dto.user.base import UserCreateDTO, UserItemDTO, UserUpdateDTO
from app.repositories.base import SQLAlchemyRepository
from app.repositories.user.user_reader import IUserReader, UserReader
from app.models.user.items import UserItem


class IUserRepository(IUserReader, ABC):
    @abstractmethod
    async def create_user(self, user_create_dto: UserCreateDTO) -> UserItemDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def update_user(self, user_id: UUID, user_update_dto: UserUpdateDTO) -> UserItemDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def delete_user(self, user_id: UUID) -> UserItemDTO | None:
        raise NotImplementedError


class UserRepository(IUserRepository, UserReader, SQLAlchemyRepository):
    async def create_user(self, user_create_dto: UserCreateDTO) -> UserItemDTO | None:
        stmt = insert(UserItem).values(user_create_dto.as_dict()).returning(UserItem)
        result = await self._session.execute(stmt)
        if user := result.scalar():
            return UserItemDTO.model_to_dto(user)
        return None

    async def update_user(self, user_id: UUID, user_update_dto: UserUpdateDTO) -> UserItemDTO | None:
        user_dto = await self.get_user_by_id(user_id=user_id)
        if not user_dto:
            return None

        data = user_update_dto.as_dict(exclude_none=True)
        stmt = update(UserItem).filter_by(id=user_id).values(data).returning(UserItem)
        result = await self._session.execute(stmt)
        if user := result.scalar():
            return UserItemDTO.model_to_dto(user)
        return None

    async def delete_user(self, user_id: UUID) -> UserItemDTO | None:
        user_dto = await self.get_user_by_id(user_id=user_id)
        if not user_dto:
            return None

        stmt = delete(UserItem).filter_by(id=user_id)
        await self._session.execute(stmt)
        return user_dto
