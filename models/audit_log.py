from datetime import datetime
from uuid import UUID
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class AuditLog(Base):
    __tablename__="audit_log"
    
    id:Mapped[int]=mapped_column(primary_key=True,index=True)
    user_id:Mapped[UUID | None]=mapped_column(ForeignKey("auth.users.id",ondelete="SET NULL"),nullable=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    entity: Mapped[str] = mapped_column(String(100), nullable=False)
    entity_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
