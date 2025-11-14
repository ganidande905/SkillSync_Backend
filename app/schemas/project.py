# app/schemas/project.py
from typing import List, Optional
from pydantic import BaseModel
from typing_extensions import Literal

ProficiencyLevel = Literal["beginner", "intermediate", "advanced"]


class ProjectSkillRequirementBase(BaseModel):
    skill_name: str
    min_proficiency_level: ProficiencyLevel
    weight: Optional[int] = None


class ProjectSkillRequirementCreate(ProjectSkillRequirementBase):
    pass


class ProjectSkillRequirementOut(ProjectSkillRequirementBase):
    id: int
    project_id: int


class ProjectBase(BaseModel):
    project_name: str
    description: str
    repository_url: str
    requirements: str


class ProjectCreate(ProjectBase):
    skill_requirements: List[ProjectSkillRequirementCreate]


class ProjectOut(ProjectBase):
    id: int
    user_id: int
    last_commit_message: Optional[str] = None
    last_commit_sha: Optional[str] = None
    last_commit_url: Optional[str] = None
    skill_requirements: List[ProjectSkillRequirementOut]

    class Config:
        from_attributes = True