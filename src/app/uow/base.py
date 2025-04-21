from abc import ABC, abstractmethod
from types import TracebackType
from typing import Optional, Type

from app.connectors.pg_database import MasterSessionMaker, SlaveSessionMaker


class UnitOfWorkABC(ABC):
    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class SQLAlchemyUoW(UnitOfWorkABC):
    def __init__(
        self,
        master_session_factory: MasterSessionMaker,
        slave_session_factory: SlaveSessionMaker,
    ):
        self.master_session_factory = master_session_factory
        self.slave_session_factory = slave_session_factory

    async def __aenter__(self):
        self.slave_session = self.slave_session_factory()
        self.master_session = self.master_session_factory()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        if exc_value:
            await self.rollback()
        else:
            await self.commit()
        await self.slave_session.close()
        await self.master_session.close()

    async def commit(self):
        await self.master_session.commit()

    async def rollback(self):
        await self.master_session.rollback()
