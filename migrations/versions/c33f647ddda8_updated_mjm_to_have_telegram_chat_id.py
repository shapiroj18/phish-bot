"""updated mjm to have telegram chat id

Revision ID: c33f647ddda8
Revises: 140c8f7246ce
Create Date: 2021-02-09 16:17:48.756611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c33f647ddda8"
down_revision = "140c8f7246ce"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("mjm_alerts", "phone_number")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "mjm_alerts",
        sa.Column(
            "phone_number", sa.VARCHAR(length=60), autoincrement=False, nullable=True
        ),
    )
    # ### end Alembic commands ###
