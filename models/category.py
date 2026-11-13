from sqlalchemy import ForeignKey, Integer,String
from sqlalchemy.orm import declarative_base,Mapped,mapped_column
Base=declarative_base()

id:Mapped[int]=mapped_column(Integer,PrimaryKey=True,Index=True)
name:Mapped[str]=mapped_column(String(200),unique=True,nullable=False)
default_department_id: Mapped[int | None] = mapped_column(ForeignKey("departments.id"),nullable=True)

