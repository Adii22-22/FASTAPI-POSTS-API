"""add content column to posts table

Revision ID: 8a4fd84ffbde
Revises: a620fbf873cc
Create Date: 2025-10-20 20:38:35.774218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a4fd84ffbde'
down_revision: Union[str, Sequence[str], None] = 'a620fbf873cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(),nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
