"""Initial migration.

Revision ID: 5861dcba496d
Revises: 
Create Date: 2023-05-05 12:59:47.542312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5861dcba496d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=36), server_default='', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###
