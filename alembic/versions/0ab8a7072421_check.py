"""check

Revision ID: 0ab8a7072421
Revises: a37a14601532
Create Date: 2025-11-15 10:53:48.147093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ab8a7072421'
down_revision: Union[str, Sequence[str], None] = 'a37a14601532'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
