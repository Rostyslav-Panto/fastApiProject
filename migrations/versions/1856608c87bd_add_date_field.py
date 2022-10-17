"""Add Date field

Revision ID: 1856608c87bd
Revises: eeffefd88321
Create Date: 2022-10-17 05:14:07.377901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1856608c87bd'
down_revision = 'eeffefd88321'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('csv_meta', sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('csv_meta', 'date')
    # ### end Alembic commands ###
