"""empty message

Revision ID: 183689e0e4ee
Revises: 
Create Date: 2022-02-23 11:00:46.058524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183689e0e4ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(length=10), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('operation', sa.String(length=64), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operations_operation'), 'operations', ['operation'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operations_operation'), table_name='operations')
    op.drop_table('operations')
    op.drop_table('users')
    # ### end Alembic commands ###