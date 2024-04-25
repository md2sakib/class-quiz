# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

"""added google_oauth

Revision ID: 0c081a52ab8a
Revises: 6dc09ad6f6ef
Create Date: 2022-06-11 14:55:03.312529

"""

from alembic import op
import sqlalchemy as sa
import ormar

# revision identifiers, used by Alembic.
revision = "0c081a52ab8a"
down_revision = "6dc09ad6f6ef"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE userauthtypes AS ENUM ('LOCAL', 'GOOGLE');")
    op.create_unique_constraint(None, "quiz", ["id"])
    op.add_column(
        "users",
        sa.Column("auth_type", sa.Enum("LOCAL", "GOOGLE", name="userauthtypes"), nullable=True, server_default="LOCAL"),
    )
    op.add_column("users", sa.Column("google_uid", sa.String(length=255), nullable=True))
    op.alter_column("users", "password", existing_type=sa.VARCHAR(length=100), nullable=True)
    op.drop_constraint("users_password_key", "users", type_="unique")
    op.create_unique_constraint(None, "users", ["google_uid"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_google_uid_key", "users", type_="unique")
    op.create_unique_constraint("users_password_key", "users", ["password"])
    op.alter_column("users", "password", existing_type=sa.VARCHAR(length=100), nullable=False)
    op.drop_column("users", "google_uid")
    op.drop_column("users", "auth_type")
    op.drop_constraint("quiz_id_key", "quiz", type_="unique")
    op.execute("DROP TYPE IF EXISTS userauthtypes;")
    # ### end Alembic commands ###
