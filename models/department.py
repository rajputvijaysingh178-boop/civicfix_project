from sqlalchemy import Integer,String
from sqlalchemy.orm import declarative_base,Mapped,mapped_column
Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,Index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str]=mapped_column(String(100),nullable=False)
    contact_email: Mapped[str] = mapped_column(String(100),nullable=False)
    