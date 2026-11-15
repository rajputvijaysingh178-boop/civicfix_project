from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


CategoryName = Literal[
    "pothole",
    "garbage",
    "water_leak",
    "streetlight",
    "damaged_road",
    "other",
]


class CategoryCreate(BaseModel):
    name: CategoryName
    default_department_id: int | None = Field(default=None, gt=0)


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: CategoryName
    default_department_id: int | None = None
    
