"""change password to password_hash

Revision ID: 16c3d114e797
Revises: 44d2b85f0b5e
Create Date: 2024-08-24 22:22:33.819453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16c3d114e797'
down_revision: Union[str, None] = '44d2b85f0b5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_services', sa.Column('hashed_password', sa.String(), nullable=True))
    op.drop_column('user_services', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_services', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user_services', 'hashed_password')
    # ### end Alembic commands ###