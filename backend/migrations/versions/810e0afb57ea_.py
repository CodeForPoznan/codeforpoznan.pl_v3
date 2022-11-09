"""empty message

Revision ID: 810e0afb57ea
Revises: 22771e69d10c
Create Date: 2022-01-19 19:59:08.027108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "810e0afb57ea"
down_revision = "22771e69d10c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "techstack",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("technology", sa.String(length=50), nullable=False),
        sa.Column("label", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("technology"),
    )
    op.create_table(
        "team_techstack",
        sa.Column("team_id", sa.Integer(), nullable=True),
        sa.Column("techstack_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["team_id"],
            ["team.id"],
        ),
        sa.ForeignKeyConstraint(
            ["techstack_id"],
            ["techstack.id"],
        ),
    )
    op.create_table(
        "user_skill",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("techstack_id", sa.Integer(), nullable=False),
        sa.Column("skill_level", sa.Integer(), nullable=True),
        sa.Column("is_learning_goal", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["techstack_id"],
            ["techstack.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "techstack_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_skill")
    op.drop_table("team_techstack")
    op.drop_table("techstack")
    # ### end Alembic commands ###
