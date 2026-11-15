from pydantic import BaseModel,ConfigDict,EmailStr
from uuid import UUID
from typing import Literal
Role = Literal["resident", "officer", "admin"]

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id:UUID
    name:str
    email:EmailStr
    role:str
    department_id:int | None = None

    

class RoleUpdate(BaseModel):
    role: Role