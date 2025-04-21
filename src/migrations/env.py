import logging
from alembic import context
from sqlalchemy import engine_from_config, pool

from app.models.base import BaseModel
from app.settings import settings

logging.basicConfig()
logger = logging.getLogger('sqlalchemy')

logger.setLevel(settings.log_config.LOG_LEVEL)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = BaseModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
masked_url = None

if not (url := config.get_main_option("sqlalchemy.url")):
    url = settings.pg_db_config.db_alembic_uri
    masked_url = settings.pg_db_config.db_masked_alembic_uri


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    logger.debug(f"Attempting offline connection to: {masked_url}")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    logger.debug(f"Attempting online connection to: {masked_url}")

    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = url
    connectable = engine_from_config(
        configuration, prefix='sqlalchemy.', poolclass=pool.NullPool, connect_args={'prepare_threshold': None}
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=target_metadata.schema,
            include_schemas=True,
            compare_type=True,
        )

        with context.begin_transaction():
            context.execute('SET search_path TO public')
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
