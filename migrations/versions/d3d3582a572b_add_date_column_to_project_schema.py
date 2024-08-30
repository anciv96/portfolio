"""Add date column to Project schema

Revision ID: d3d3582a572b
Revises: d1690d800357
Create Date: 2024-08-27 21:04:24.193903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3d3582a572b'
down_revision: Union[str, None] = 'd1690d800357'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('created_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'created_on')
    # ### end Alembic commands ###