"""upgrade anime db

Revision ID: c7656c265cf5
Revises: 6eb713ee0248
Create Date: 2024-04-30 14:42:22.294285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7656c265cf5'
down_revision: Union[str, None] = '6eb713ee0248'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('anime', 'genre',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('anime', 'genre',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
