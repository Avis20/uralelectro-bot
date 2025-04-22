from pydantic_settings import BaseSettings


class PgDriverConfig(BaseSettings):
    prepare_threshold: int | None = None  # If it is set to None, prepared statements are disabled on the connection.


# Настройки PostgreSQL
class PgDbConfig(BaseSettings):
    DB_ECHO_LOG: bool = False
    SCHEMA_DUMP_DIR: str = "/opt/sql/schema"

    PG_DRIVER_CONFIG: PgDriverConfig = PgDriverConfig()

    PG_DB_DRIVER: str = "psycopg"

    PG_MASTER_HOST: str = 'localhost'
    PG_MASTER_PORT: int = 6432
    PG_MASTER_DB: str = 'project_uralelectro-bot'
    PG_MASTER_USER: str = 'project_uralelectro-bot'
    PG_MASTER_PASSWORD: str = 'project_uralelectro-bot'
    PG_MASTER_MIN_POOL_SIZE: int = 2
    PG_MASTER_MAX_POOL_SIZE: int = 20

    PG_SLAVE_HOST: str = 'localhost'
    PG_SLAVE_PORT: int = 6432
    PG_SLAVE_DB: str = 'project_uralelectro-bot'
    PG_SLAVE_USER: str = 'project_uralelectro-bot'
    PG_SLAVE_PASSWORD: str = 'project_uralelectro-bot'
    PG_SLAVE_MIN_POOL_SIZE: int = 2
    PG_SLAVE_MAX_POOL_SIZE: int = 200

    PG_ALEMBIC_HOST: str = 'localhost'
    PG_ALEMBIC_PORT: int = 6432
    PG_ALEMBIC_DB: str = 'project_uralelectro-bot'
    PG_ALEMBIC_USER: str = 'project_uralelectro-bot'
    PG_ALEMBIC_PASSWORD: str = 'project_uralelectro-bot'
    PG_ALEMBIC_MIN_POOL_SIZE: int = 1
    PG_ALEMBIC_MAX_POOL_SIZE: int = 2

    @property
    def db_master_uri(self) -> str:
        return (
            f"postgresql+{self.PG_DB_DRIVER}://{self.PG_MASTER_USER}:"
            f"{self.PG_MASTER_PASSWORD}@{self.PG_MASTER_HOST}:{self.PG_MASTER_PORT}/"
            f"{self.PG_MASTER_DB}"
        )

    @property
    def db_slave_uri(self) -> str:
        return (
            f"postgresql+{self.PG_DB_DRIVER}://{self.PG_SLAVE_USER}:"
            f"{self.PG_SLAVE_PASSWORD}@{self.PG_SLAVE_HOST}:{self.PG_SLAVE_PORT}/"
            f"{self.PG_SLAVE_DB}"
        )

    @property
    def db_alembic_uri(self) -> str:
        return (
            f"postgresql+{self.PG_DB_DRIVER}://{self.PG_ALEMBIC_USER}:"
            f"{self.PG_ALEMBIC_PASSWORD}@{self.PG_ALEMBIC_HOST}:{self.PG_ALEMBIC_PORT}/"
            f"{self.PG_ALEMBIC_DB}"
        )

    @property
    def db_masked_alembic_uri(self) -> str:
        return (
            f"postgresql+{self.PG_DB_DRIVER}://{self.PG_ALEMBIC_USER}:"
            f"******@{self.PG_ALEMBIC_HOST}:{self.PG_ALEMBIC_PORT}/"
            f"{self.PG_ALEMBIC_DB}"
        )


class ApiConfig(BaseSettings):
    SHOW_DOCS: bool = False
    API_ROOT: str = ''
    BACK_SCHEMA: str = 'http'
    BACK_HOST: str = '0.0.0.0'
    BACK_PORT: int = 8080
    UVICORN_WORKERS_COUNT: int = 1
    UVICORN_LOG_LEVEL: str = 'info'
    UVICORN_RELOAD: bool = True
    REQUEST_ID_LOG_LENGTH: int = 10


class AdminConfig(BaseSettings):
    ADMIN_SECRET: str = 'secret'


class Settings(BaseSettings):
    DEBUG: bool = False
    ENABLE_LOG_REQUESTS: bool = False

    api_config: ApiConfig = ApiConfig()
    pg_db_config: PgDbConfig = PgDbConfig()
    admin_config: AdminConfig = AdminConfig()


settings = Settings()
