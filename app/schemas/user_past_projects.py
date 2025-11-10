from pydantic import BaseModel , EmailStr

class UserPastProjectBase(BaseModel):
    project_title: str
    description: str
    technologies_used: str

class UserPastProject(UserPastProjectBase):
    user_id: int


class UserPastProjectOut(UserPastProjectBase):
    id: int
    user_id: int
    project_title: str
    description: str
    technologies_used: str

    class Config:
        orm_mode = True
        