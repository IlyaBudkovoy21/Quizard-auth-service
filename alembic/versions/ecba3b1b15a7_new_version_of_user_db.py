"""New version of User db

Revision ID: ecba3b1b15a7
Revises: a072a4aa0741
Create Date: 2025-07-31 10:16:18.024902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecba3b1b15a7'
down_revision: Union[str, Sequence[str], None] = 'a072a4aa0741'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
