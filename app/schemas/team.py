from pydantic import BaseModel
from typing import List


class TeamMemberOut(BaseModel):
    id: int
    user_id: int
    role: str
    status: str  

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    team_name: str
    description: str


class TeamOut(TeamBase):
    id: int
    project_id: int
    creator_id: int | None = None
    members: List[TeamMemberOut] = []

    class Config:
        orm_mode = True