from pydantic import BaseModel


class TeamBase(BaseModel):
    team_name : str
    project_title : str
    description : str

class TeamCreate(TeamBase):
    project_id:int

class TeamOut(TeamBase):
    id : int
    project_id: int
    creator_id : int | None = None

    class Config:
        orm_mode = True