from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime
from uuid import UUID
from typing import Literal
from schemas.media import MediaOut

class ComplaintCreate(BaseModel):
    title:str =  Field(min_length=5, max_length=100)
    description:str = Field(min_length=5, max_length=100)
    category_id: int | None = Field(default=None, gt=0)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    address_text: str | None = Field(default=None, max_length=500)
    
    
class ComplaintOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    category_id: int
    priority: str
    status: str

    latitude: float
    longitude: float
    address_text: str | None = None

    department_id: int | None = None
    assigned_to: UUID | None = None
    support_count: int

    created_at: datetime
    updated_at: datetime
    resolved_at: datetime | None = None
    media: list[MediaOut] = Field(default_factory=list)
    
class ComplaintListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    category_id: int
    priority: str
    status: str
    created_at: datetime
    distance_m: float | None = None
    
    
    
class ComplaintFilter(BaseModel):
    status: Literal[
        "submitted",
        "assigned",
        "in_progress",
        "resolved",
        "verified",
        "reopened",
        "duplicate",
    ] | None = None

    category_id: int | None = Field(default=None, gt=0)
    priority: str | None = None
    department_id: int | None = Field(default=None, gt=0)

    date_from: datetime | None = None
    date_to: datetime | None = None

    min_latitude: float | None = Field(default=None, ge=-90, le=90)
    max_latitude: float | None = Field(default=None, ge=-90, le=90)
    min_longitude: float | None = Field(default=None, ge=-180, le=180)
    max_longitude: float | None = Field(default=None, ge=-180, le=180)

    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)
    
class StatusUpdate(BaseModel):
    new_status: Literal[
        "submitted",
        "assigned",
        "in_progress",
        "resolved",
        "verified",
        "reopened",
        "duplicate",
    ]
    note: str | None = Field(default=None, max_length=1000)
    
class AssignRequest(BaseModel):
    officer_id: UUID