"""add-schema

Revision ID: 74f152bfe7df
Revises: 9f6d2b4d2d28
Create Date: 2024-11-21 15:18:10.439316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f152bfe7df'
down_revision = '9f6d2b4d2d28'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA \"user\"")


def downgrade():
    op.execute("DROP SCHEMA \"user\"")
