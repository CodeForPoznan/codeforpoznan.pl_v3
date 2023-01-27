"""empty message

Revision ID: ea7204474ffa
Revises: 
Create Date: 2018-11-25 18:45:30.629678

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ea7204474ffa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hacknight",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date", sa.String(length=20), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "participant",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=20), nullable=True),
        sa.Column("lastname", sa.String(length=20), nullable=True),
        sa.Column("email", sa.String(length=30), nullable=True),
        sa.Column("github", sa.String(length=200), nullable=True),
        sa.Column("phone", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=20), nullable=True),
        sa.Column("hashed_password", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    op.drop_table("participant")
    op.drop_table("hacknight")
    # ### end Alembic commands ###
