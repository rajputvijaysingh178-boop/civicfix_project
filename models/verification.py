from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class ResolutionVerification(Base):
    __tablename__ = "resolution_verifications"

    __table_args__ = (
        CheckConstraint(
            "method IN ('manual', 'ai')",
            name="check_verification_method",
        ),
        CheckConstraint(
            "verdict IN ('fixed', 'not_fixed', 'unclear')",
            name="check_verification_verdict",
        ),
        CheckConstraint(
            "confidence IS NULL OR (confidence >= 0 AND confidence <= 1)",
            name="check_verification_confidence",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    complaint_id: Mapped[int] = mapped_column(
        ForeignKey("complaints.id", ondelete="CASCADE"),
        nullable=False,
    )

    # Optional: manual verification might happen without an after photo.
    after_media_id: Mapped[int | None] = mapped_column(
        ForeignKey("complaint_media.id", ondelete="SET NULL"),
        nullable=True,
    )

    method: Mapped[str] = mapped_column(String(10), nullable=False)
    verdict: Mapped[str] = mapped_column(String(10), nullable=False)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    citizen_response: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )