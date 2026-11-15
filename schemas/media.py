from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class MediaOut(BaseModel):
    id: int
    url: str
    kind: Literal["before", "after"]
    created_at: datetime