"""Add url column to feedback, and modify id column

Revision ID: bedd04471e8e
Revises: 16c3d114e797
Create Date: 2024-08-25 05:34:25.775031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bedd04471e8e'
down_revision: Union[str, None] = '16c3d114e797'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('feedback', 'url')
    # ### end Alembic commands ###
