from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass
class user(Base):
    __tablename__="users"
    
id:Mapped[UUID]=mapped_column(ForeignKey("auth.user.id",ondelete="CASCADE"),primary_key=True)
name:Mapped[str]=mapped_column(String(100),nullable=False)
email:Mapped[str]=mapped_column(String(100),unique=True,nullable=False)
role:Mapped[str]=mapped_column(String(100),nullable=False,default="residents")
department_id:Mapped[int | None]=mapped_column(ForeignKey("departments.id",nullable=True))
is_active:Mapped[bool]=mapped_column(Boolean,nullable=False,default=True)
created_At:Mapped[datetime]=mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now(),)

