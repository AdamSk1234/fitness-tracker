"""goals fields

Revision ID: 7685d26dca1d
Revises: 15385552523b
Create Date: 2025-08-11 19:53:03.417418

"""
from alembic import op
import sqlalchemy as sa


revision = '7685d26dca1d'
down_revision = '15385552523b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('goal', sa.Column('metric', sa.String(length=20), nullable=False, server_default='duration'))
    op.alter_column('goal', 'metric', server_default=None)
    op.add_column('goal', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.add_column('goal', sa.Column('end_date', sa.DateTime(), nullable=True))
    op.add_column('goal', sa.Column('exercise_type_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_goal_ex_type', 'goal', 'exercise_type', ['exercise_type_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_goal_ex_type', 'goal', type_='foreignkey')
    op.drop_column('goal', 'exercise_type_id')
    op.drop_column('goal', 'end_date')
    op.drop_column('goal', 'start_date')
    op.drop_column('goal', 'metric')