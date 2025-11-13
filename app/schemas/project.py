from pydantic import BaseModel

class ProjectBase(BaseModel):
    project_name: str
    description: str
    repository_url: str

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    user_id: int
    last_commit_message: str | None = None
    last_commit_sha: str | None = None
    last_commit_url: str | None = None

    class Config:
        orm_mode = True