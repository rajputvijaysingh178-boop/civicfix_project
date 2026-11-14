from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base
class HotspotSnapshot(Base):
    __tablename__ = "hotspot_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    cell_or_cluster_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    center_lat: Mapped[float] = mapped_column(Float, nullable=False)
    center_lng: Mapped[float] = mapped_column(Float, nullable=False)

    # Empty means this hotspot includes all complaint categories.
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
    )

    complaint_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    score: Mapped[float] = mapped_column(Float, nullable=False)

    computed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )