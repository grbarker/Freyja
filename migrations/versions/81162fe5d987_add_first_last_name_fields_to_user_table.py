"""Add first/last name fields to user table.

Revision ID: 81162fe5d987
Revises: 4e8beae024e9
Create Date: 2018-11-28 22:14:00.933976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81162fe5d987'
down_revision = '4e8beae024e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=False)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    # ### end Alembic commands ###
