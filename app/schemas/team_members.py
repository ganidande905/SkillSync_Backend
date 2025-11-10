from pydantic import BaseModel

class TeamMemberBase(BaseModel):
    team_id: int
    user_id: int
    role: str
    
class TeamMemberCreate(TeamMemberBase):
    pass
class TeamMemberOut(TeamMemberBase):
    id: int
    class Config:
        orm_mode = True