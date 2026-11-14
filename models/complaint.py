from datetime import datetime
from uuid import UUID

from geoalchemy2 import Geometry
from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from database import Base
class Complaint(Base):
    __tablename__="complaints"
    
    id:Mapped[int]=mapped_column(primary_key=True,index=True,)
    user_id:Mapped[UUID]=mapped_column(ForeignKey("auth.users.id",ondelete="CASCADE"),nullable=False,)
    title:Mapped[str]=mapped_column(String(100),nullable=False,)
    description:Mapped[str]=mapped_column(Text,nullable=False,)
    category_id:Mapped[int]=mapped_column(ForeignKey("categories.id"),nullable=False)
    priority:Mapped[str]=mapped_column(String(100),nullable=False,default="submitted",)
    status:Mapped[str]=mapped_column(String(50),nullable=False,default="submitted",)
    latitude:Mapped[Float | None]=mapped_column(Float,nullable=False,)
    longitude:Mapped[Float | None]=mapped_column(Float,nullable=False,)
    location:Mapped[str | None]=mapped_column(Geometry("POINT",srid=4326,spatial_index=True),nullable=True,)
    address_text:Mapped[Text | None]=mapped_column(Text,nullable=True,)
    department_id:Mapped[int | None]=mapped_column(ForeignKey("departments.id"),nullable=True,)
    assigned_to:Mapped[UUID | None]=mapped_column(ForeignKey("auth.users.id"),nullable=True,)
    support_count: Mapped[int] = mapped_column(Integer,nullable=False,default=0,)
    ai_category: Mapped[str | None] = mapped_column(String(50), nullable=True)
    ai_priority: Mapped[str | None] = mapped_column(String(20), nullable=True)
    ai_confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column( DateTime(timezone=True),nullable=False,server_default=func.now(),)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now(),onupdate=func.now(),)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True),nullable=True,)