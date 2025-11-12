from pydantic import BaseModel, EmailStr

class UserInterestBase(BaseModel):
    interest_name: str
    user_email: EmailStr
class UserInterestCreate(UserInterestBase):
    user_id: int
    
class UserInterestOut(UserInterestBase):
    id: int
    class Config:
        orm_mode = True

    