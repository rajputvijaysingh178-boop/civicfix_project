from sqlalchemy import Integer,String
from sqlalchemy.orm import declarative_base,Mapped,mapped_column
from database import Base

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str]=mapped_column(String(100),nullable=False)
    contact_email: Mapped[str] = mapped_column(String(100),nullable=False)
    