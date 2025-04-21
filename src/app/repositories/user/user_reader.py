from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import select

from app.dto.user.base import UserItemDTO
from app.repositories.base import SQLAlchemyRepository
from app.models.user.items import UserItem


class IUserReader(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: UUID) -> UserItemDTO | None:
        raise NotImplementedError


class UserReader(SQLAlchemyRepository, IUserReader):
    async def get_user_by_id(self, user_id: UUID) -> UserItemDTO | None:
        stmt = select(UserItem).filter_by(id=user_id)
        result = await self._session.execute(stmt)
        if user_db := result.scalar():
            user = UserItemDTO.model_to_dto(user_db)
            return user
        return None
