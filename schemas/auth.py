from pydantic import BaseModel,EmailStr, Field


class UserCreate(BaseModel):
    name : str = Field(min_length=1,max_length=100)
    email : EmailStr
    password:str =  Field(min_length=8,max_length=128)
    
    
class UserLogin(BaseModel):
    email: EmailStr
    password:str=  Field(min_length=8,max_length=128)
    
class Token(BaseModel):
    access_token:str 
    refresh_token:str | None=None
    token_type:str = "bearer"
    
    