from typing import Literal

from pydantic import BaseModel, Field


class ResolveRequest(BaseModel):
    note: str | None = Field(default=None, max_length=1000)


class VerificationOut(BaseModel):
    verdict: Literal["fixed", "not_fixed", "unclear"]
    confidence: float | None = Field(default=None, ge=0, le=1)
    reason: str | None = None
    needs_citizen_confirmation: bool


class CitizenConfirm(BaseModel):
    confirmed: bool
    comment: str | None = Field(default=None, max_length=1000)