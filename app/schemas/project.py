from pydantic import BaseModel

class ProjectBase(BaseModel):
    project_name: str
    description: str
    repository_url: str
    requirements: str | None = None
class ProjectSkillRequirementBase(BaseModel):
    skill_name: str
    min_proficiency_level: str | None = None
    weight: int | None = None

    
class ProjectCreate(ProjectBase):
    skill_requirements: list[ProjectSkillRequirementBase] = []


class ProjectSkillRequirementOut(ProjectSkillRequirementBase):
    id: int

    class Config:
        orm_mode = True
class ProjectOut(ProjectBase):
    id: int
    user_id: int | None = None
    last_commit_message: str | None = None
    last_commit_sha: str | None = None
    last_commit_url: str | None = None
    skill_requirements: list[ProjectSkillRequirementOut] = []
    class Config:
        orm_mode = True