from pydantic import BaseModel , EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name : str
    university: str | None = None
    
class UserCreate(UserBase):
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
class UserOut(UserBase):
    id : int
    is_onboarded : bool
    
    class Config:
        orm_mode = True