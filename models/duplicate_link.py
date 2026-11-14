from sqlalchemy import (
    CheckConstraint,
    Float,
    ForeignKey,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class DuplicateLink(Base):
    __tablename__ = "duplicate_links"

    __table_args__ = (
        CheckConstraint(
            "method IN ('rule', 'ai')",
            name="check_duplicate_link_method",
        ),
        CheckConstraint(
            "state IN ('suggested', 'confirmed', 'rejected')",
            name="check_duplicate_link_state",
        ),
        CheckConstraint(
            "complaint_id <> master_complaint_id",
            name="check_duplicate_link_not_self",
        ),
        CheckConstraint(
            "similarity_score >= 0 AND similarity_score <= 1",
            name="check_duplicate_link_score",
        ),
        UniqueConstraint(
            "complaint_id",
            "master_complaint_id",
            name="unique_duplicate_link_pair",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    complaint_id: Mapped[int] = mapped_column(
        ForeignKey("complaints.id", ondelete="CASCADE"),
        nullable=False,
    )

    master_complaint_id: Mapped[int] = mapped_column(
        ForeignKey("complaints.id", ondelete="CASCADE"),
        nullable=False,
    )
    similarity_score: Mapped[float] = mapped_column(Float, nullable=False)
    method: Mapped[str] = mapped_column(String(10), nullable=False)
    state: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="suggested",
    )