from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class ComplaintMedia(Base):
    __tablename__="complaint_media"
    __table_args__= ( 
            CheckConstraint(
                "kind IN ( 'before','after')",
                name="check_complaint-media_kind",
                
            ),)
    
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    complaint_id:Mapped[int]=mapped_column(ForeignKey("complaints.id",ondelete="CASCADE"),nullable=False,)
    storage_path:Mapped[str]=mapped_column(String(1000),nullable=False)
    content_hash: Mapped[str | None] = mapped_column(
    String(64),
    nullable=True,
    index=True,
)
    kind:Mapped[str]=mapped_column(String(100),nullable=False)
    uploaded_by:Mapped[UUID | None]=mapped_column(ForeignKey("auth.users.id"),nullable=True,)
    captured_lat: Mapped[float | None] = mapped_column(Float, nullable=True)
    captured_lng: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now())