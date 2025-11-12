from pydantic import BaseModel, EmailStr

class UserInterestBase(BaseModel):
    interest_name: str
class UserInterestCreate(UserInterestBase):
   pass
    
class UserInterestOut(UserInterestBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

    