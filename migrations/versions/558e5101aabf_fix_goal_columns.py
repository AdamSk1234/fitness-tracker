"""fix goal columns

Revision ID: 558e5101aabf
Revises: 7685d26dca1d
Create Date: 2025-08-11 21:18:56.566927
"""
from alembic import op
import sqlalchemy as sa

revision = "558e5101aabf"
down_revision = "7685d26dca1d"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("goal", schema=None) as batch:
        batch.add_column(sa.Column("metric", sa.String(length=20), nullable=True))
        batch.add_column(sa.Column("start_date", sa.DateTime(), nullable=True))
        batch.add_column(sa.Column("end_date", sa.DateTime(), nullable=True))
        batch.add_column(sa.Column("exercise_type_id", sa.Integer(), nullable=True))
        batch.create_index("ix_goal_metric", ["metric"])
        batch.create_index("ix_goal_exercise_type_id", ["exercise_type_id"])

    op.execute("UPDATE goal SET metric='duration' WHERE metric IS NULL")

    with op.batch_alter_table("goal", schema=None) as batch:
        batch.alter_column(
            "metric",
            existing_type=sa.String(length=20),
            nullable=False,
        )




def downgrade():
    with op.batch_alter_table("goal", schema=None) as batch:
        batch.drop_index("ix_goal_exercise_type_id")
        batch.drop_index("ix_goal_metric")
        batch.drop_column("exercise_type_id")
        batch.drop_column("end_date")
        batch.drop_column("start_date")
        batch.drop_column("metric")
