from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class StatusHistory(Base):
    __tablename__="status_history"
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    complaint_id:Mapped[int]=mapped_column(ForeignKey("complaints.id",ondelete="CASCADE"),nullable=False)
    old_status: Mapped[str | None] = mapped_column(String(30), nullable=True)
    new_status: Mapped[str] = mapped_column(String(30), nullable=False)
    changed_by:Mapped[UUID | None]=mapped_column(ForeignKey("auth.users.id"),nullable=True)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now(),)