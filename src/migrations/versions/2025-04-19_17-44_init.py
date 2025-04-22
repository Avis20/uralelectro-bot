"""add-schema

Revision ID: 74f152bfe7df
Revises: 9f6d2b4d2d28
Create Date: 2024-11-21 15:18:10.439316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f152bfe7df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"");
    op.execute("CREATE SCHEMA \"user\"")
    op.execute("CREATE SCHEMA \"inventory\"")
    op.execute("CREATE SCHEMA \"supplier\"")
    op.execute("CREATE SCHEMA \"customer\"")
    op.execute("CREATE SCHEMA \"employee\"")
    op.execute("CREATE SCHEMA \"order\"")


def downgrade():
    op.execute("DROP SCHEMA \"user\"")
    op.execute("DROP SCHEMA \"inventory\"")
    op.execute("DROP SCHEMA \"supplier\"")
    op.execute("DROP SCHEMA \"customer\"")
    op.execute("DROP SCHEMA \"employee\"")
    op.execute("DROP SCHEMA \"order\"")
