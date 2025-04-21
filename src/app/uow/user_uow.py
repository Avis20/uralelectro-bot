from __future__ import annotations

from app.repositories.user.user_repo import IUserRepository, UserRepository
from app.repositories.user.user_reader import IUserReader, UserReader
from app.uow.base import SQLAlchemyUoW, UnitOfWorkABC


class IUserUoW(UnitOfWorkABC):
    user_repo: IUserRepository
    user_reader: IUserReader


class UserUoW(SQLAlchemyUoW, IUserUoW):
    async def __aenter__(self) -> UserUoW:
        await super().__aenter__()
        self.user_repo = UserRepository(self.master_session)
        self.user_reader = UserReader(self.slave_session)
        return self
