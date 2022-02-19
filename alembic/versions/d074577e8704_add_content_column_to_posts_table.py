"""add content column to posts table

Revision ID: d074577e8704
Revises: 11bc7c6306dc
Create Date: 2022-02-18 11:16:03.282131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd074577e8704'
down_revision = '11bc7c6306dc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
