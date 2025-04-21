import pytest
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, drop_database

from app.settings import settings


@pytest.fixture(scope="module")
def alembic_config():
    return Config("alembic.ini")


@pytest.fixture(scope="module")
def single_use_database():
    """
    SQLAlchemy engine, for single use
    """
    db_url = f"{settings.pg_db_config.db_alembic_uri}"
    create_database(db_url)
    engine = create_engine(db_url, echo=True)
    try:
        yield engine
    finally:
        engine.dispose()
        drop_database(db_url)
