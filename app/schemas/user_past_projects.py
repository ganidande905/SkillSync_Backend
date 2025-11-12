from pydantic import BaseModel , EmailStr

class UserPastProjectBase(BaseModel):
    project_title: str
    description: str
    technologies_used: str
    user_email: EmailStr
class UserPastProjectCreate(UserPastProjectBase):
    pass

class UserPastProjectOut(UserPastProjectBase):
    id: int

    class Config:
        orm_mode = True
        