"""test

Revision ID: 9f6d2b4d2d28
Revises:
Create Date: 2025-04-19_17-44

"""
from alembic import op
import sqlalchemy as sa
import re

from app.settings import settings

# revision identifiers, used by Alembic.
revision = '9f6d2b4d2d28'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    statement_part = ''
    with open(f"{settings.pg_db_config.SCHEMA_DUMP_DIR}/uralelectro-bot_up.sql") as file_:
        for statement in file_.read().split(";\n\n"):
            # иначе sqlalchemy будет думать, что там есть bind параметры
            statement = statement.replace(r'":', '"\\:')
            # у нас есть триггерные функции, которые попадают под шаблон split
            # поэтому надо из склеивать обратно
            statement_part = statement_part + statement + ";\n\n"
            if len(re.findall(r'\$body\$', statement_part.lower())) == 1:
                continue
            elif len(re.findall(r'\$body\$', statement_part.lower())) == 2:
                op.execute(statement_part)
                statement_part = ''
                continue

            op.execute(statement)
            statement_part = ''


def downgrade():
    with open(f"{settings.pg_db_config.SCHEMA_DUMP_DIR}/uralelectro-bot_down.sql") as file_:
        for statement in file_.read().split(";\n\n"):
            op.execute(statement)
