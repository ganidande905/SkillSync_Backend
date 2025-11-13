"""add is_onboarded to users

Revision ID: 46d9ba67e567
Revises: 174f1f460c5a
Create Date: 2025-11-14 04:53:29.833349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46d9ba67e567'
down_revision: Union[str, Sequence[str], None] = '174f1f460c5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
