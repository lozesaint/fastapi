"""create posts table

Revision ID: 11bc7c6306dc
Revises: 
Create Date: 2022-02-18 09:09:52.039193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11bc7c6306dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False,))
    pass


def downgrade():
    op.drop_table('posts')
    pass
