from typing import Literal

from pydantic import BaseModel, Field


class DuplicateCheckRequest(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=10, max_length=5000)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    category_id: int | None = Field(default=None, gt=0)


class DuplicateCandidate(BaseModel):
    complaint_id: int
    title: str
    distance_m: float = Field(ge=0)
    similarity_score: float = Field(ge=0, le=1)
    status: str


class MergeRequest(BaseModel):
    master_complaint_id: int = Field(gt=0)