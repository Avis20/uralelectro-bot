from abc import ABC, abstractmethod
import orjson
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import Settings


def orjson_dumps(v, *args, **kwargs):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, *args, **kwargs).decode()


class MasterSessionMaker(ABC):
    @abstractmethod
    def __call__(self):
        raise NotImplementedError


class SlaveSessionMaker(ABC):
    @abstractmethod
    def __call__(self):
        raise NotImplementedError


class SQLAlchemyDatabaseConnector:
    def __init__(self, settings: Settings):
        master_engine = create_async_engine(
            settings.pg_db_config.db_master_uri,
            json_serializer=orjson_dumps,
            json_deserializer=orjson.loads,
            connect_args={'prepare_threshold': None},
            echo=settings.pg_db_config.DB_ECHO_LOG,
        )
        slave_engine = create_async_engine(
            settings.pg_db_config.db_slave_uri,
            json_serializer=orjson_dumps,
            json_deserializer=orjson.loads,
            connect_args={'prepare_threshold': None},
            echo=settings.pg_db_config.DB_ECHO_LOG,
        )
        self._master_session_maker = async_sessionmaker(master_engine)
        self._slave_session_maker = async_sessionmaker(slave_engine)

    def get_master_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return self._master_session_maker

    def get_slave_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return self._slave_session_maker
