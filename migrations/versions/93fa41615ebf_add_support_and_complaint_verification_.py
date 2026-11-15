"""add support and complaint verification fields

Revision ID: 93fa41615ebf
Revises: 67cbdff5055a
Create Date: 2026-11-14 19:02:48.159158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93fa41615ebf'
down_revision: Union[str, Sequence[str], None] = '67cbdff5055a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "complaint_supports",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("complaint_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["complaint_id"],
            ["complaints.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["auth.users.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "complaint_id",
            "user_id",
            name="uq_complaint_support_user",
        ),
    )
    op.create_index(
        op.f("ix_complaint_supports_id"),
        "complaint_supports",
        ["id"],
        unique=False,
    )

    op.add_column(
        "complaint_media",
        sa.Column("content_hash", sa.String(length=64), nullable=True),
    )
    op.create_index(
        op.f("ix_complaint_media_content_hash"),
        "complaint_media",
        ["content_hash"],
        unique=False,
    )

    op.add_column(
        "complaints",
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
    )
    op.create_check_constraint(
        "check_complaint_status",
        "complaints",
        "status IN ('submitted', 'assigned', 'in_progress', "
        "'resolved', 'verified', 'reopened', 'duplicate')",
    )

    op.create_index(
        "ix_complaints_category_id",
        "complaints",
        ["category_id"],
        unique=False,
    )
    op.create_index(
        "ix_complaints_created_at",
        "complaints",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        "ix_complaints_department_id",
        "complaints",
        ["department_id"],
        unique=False,
    )
    op.create_index(
        "ix_complaints_status",
        "complaints",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "check_complaint_status",
        "complaints",
        type_="check",
    )
    op.drop_index("ix_complaints_status", table_name="complaints")
    op.drop_index("ix_complaints_department_id", table_name="complaints")
    op.drop_index("ix_complaints_created_at", table_name="complaints")
    op.drop_index("ix_complaints_category_id", table_name="complaints")
    op.drop_column("complaints", "is_deleted")

    op.drop_index(
        op.f("ix_complaint_media_content_hash"),
        table_name="complaint_media",
    )
    op.drop_column("complaint_media", "content_hash")

    op.drop_index(
        op.f("ix_complaint_supports_id"),
        table_name="complaint_supports",
    )
    op.drop_table("complaint_supports")