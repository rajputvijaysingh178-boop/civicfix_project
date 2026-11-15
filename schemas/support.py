from pydantic import BaseModel, Field


class SupportResponse(BaseModel):
    complaint_id: int
    support_count: int = Field(ge=0)
    supported: bool