from pydantic import BaseModel

class UserInterestBase(BaseModel):
    interest_name: str
    
class UserInterestCreate(UserInterestBase):
    user_id: int
    
class UserInterestOut(UserInterestBase):
    id: int
    user_id : int
    interest_name: str
    class Config:
        orm_mode = True

    