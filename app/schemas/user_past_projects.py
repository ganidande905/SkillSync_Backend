from pydantic import BaseModel
class UserPastProjectBase(BaseModel):
    project_title: str
    description: str
    technologies_used: str
class UserPastProjectCreate(UserPastProjectBase):
    pass

class UserPastProjectOut(UserPastProjectBase):
    id: int
    user_id : int
    class Config:
        orm_mode = True
        