"""Add default and nullable parameters

Revision ID: 6345f0224491
Revises: a51a48ad09a8
Create Date: 2024-09-01 23:38:59.594545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6345f0224491'
down_revision: Union[str, None] = 'a51a48ad09a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feedback', 'author',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('feedback', 'text',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('feedback', 'url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('order', 'customer_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('order', 'customer_number',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('order', 'customer_email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('project', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('project', 'image_path',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('project', 'image_path',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('project', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('order', 'customer_email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('order', 'customer_number',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('order', 'customer_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('feedback', 'url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('feedback', 'text',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('feedback', 'author',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###
