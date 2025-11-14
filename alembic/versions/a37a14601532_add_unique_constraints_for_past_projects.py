"""add unique constraints for  past_projects

Revision ID: a37a14601532
Revises: 46d9ba67e567
Create Date: 2025-11-14 06:48:33.180886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a37a14601532'
down_revision: Union[str, Sequence[str], None] = '46d9ba67e567'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
