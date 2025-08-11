"""uniq exercisetype per user

Revision ID: 15385552523b
Revises: de9cf00db031
Create Date: 2025-08-11 15:17:00
"""
from alembic import op
import sqlalchemy as sa

revision = "15385552523b"
down_revision = "de9cf00db031"
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    if bind.dialect.name == "sqlite":
        bind.execute(sa.text("PRAGMA foreign_keys=OFF"))

    op.create_table(
        "exercise_type_new",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.UniqueConstraint("user_id", "name", name="uq_exercise_type_user_name"),
    )

    op.execute("""
        INSERT INTO exercise_type_new (id, user_id, name)
        SELECT id, user_id, name FROM exercise_type
    """)

    # Podmiana tabel
    op.drop_table("exercise_type")
    op.rename_table("exercise_type_new", "exercise_type")

    if bind.dialect.name == "sqlite":
        bind.execute(sa.text("PRAGMA foreign_keys=ON"))


def downgrade():
    bind = op.get_bind()
    if bind.dialect.name == "sqlite":
        bind.execute(sa.text("PRAGMA foreign_keys=OFF"))

    op.create_table(
        "exercise_type_old",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.UniqueConstraint("name", name="uq_exercise_type_name"),
    )

    op.execute("""
        INSERT INTO exercise_type_old (id, user_id, name)
        SELECT id, user_id, name FROM exercise_type
    """)

    op.drop_table("exercise_type")
    op.rename_table("exercise_type_old", "exercise_type")

    if bind.dialect.name == "sqlite":
        bind.execute(sa.text("PRAGMA foreign_keys=ON"))
