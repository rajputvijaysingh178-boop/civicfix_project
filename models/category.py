from sqlalchemy import ForeignKey, Integer,String , CheckConstraint
from sqlalchemy.orm import declarative_base,Mapped,mapped_column
from database import Base
class Category(Base):
    __tablename__ = "categories"

    __table_args__ = (
        CheckConstraint(
            "name IN ('pothole', 'garbage', 'water_leak', "
            "'streetlight', 'damaged_road', 'other')",
            name="check_category_name",
        ),
    )


    id:Mapped[int]=mapped_column( Integer,primary_key=True,index=True)
    name:Mapped[str]=mapped_column(String(200),unique=True,nullable=False)
    default_department_id: Mapped[int | None] = mapped_column(ForeignKey("departments.id"),nullable=True)

