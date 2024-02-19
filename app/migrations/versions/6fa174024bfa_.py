"""empty message

Revision ID: 6fa174024bfa
Revises: 1ab889a7930b
Create Date: 2024-02-19 15:02:21.522450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fa174024bfa'
down_revision: Union[str, None] = '1ab889a7930b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
