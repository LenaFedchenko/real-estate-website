"""expand user password column

Revision ID: 2f4a8c1d9b7e
Revises: 1eedd5dbd0a6
Create Date: 2026-04-28 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f4a8c1d9b7e'
down_revision = '1eedd5dbd0a6'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'password',
            existing_type=sa.String(length=35),
            type_=sa.String(length=255),
            existing_nullable=False,
        )


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'password',
            existing_type=sa.String(length=255),
            type_=sa.String(length=35),
            existing_nullable=False,
        )
