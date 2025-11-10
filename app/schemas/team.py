from pydantic import BaseModel


class TeamBase(BaseModel):
    team_name : str
    project_title : str
    description : str

class TeamCreate(TeamBase):
    creator_id : int

class TeamOut(TeamBase):
    id : int
    creator_id : int

    class Config:
        orm_mode = True