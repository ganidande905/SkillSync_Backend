from pydantic import BaseModel

class ProjectBase(BaseModel):
    project_name: str
    description: str
    repository_url: str
    progress: int
class ProjectCreate(ProjectBase):
    owner_id: int
    
class ProjectOut(ProjectBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True