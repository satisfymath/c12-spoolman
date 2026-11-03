"""add index on spool.filament_id.

Revision ID: 91068bd6832b
Revises: fe4970567bb3

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "91068bd6832b"
down_revision = "fe4970567bb3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add the index."""
    with op.batch_alter_table("spool", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_spool_filament_id"), ["filament_id"], unique=False)


def downgrade() -> None:
    """Remove the index."""
    with op.batch_alter_table("spool", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_spool_filament_id"))
