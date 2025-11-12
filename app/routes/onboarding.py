from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import models
from app.db import crud
from app.schemas.user_past_projects import (
    UserPastProjectCreate,
    UserPastProjectOut,
)
from app.schemas.user_skills import (
    UserSkillCreate,
    UserSkillOut,
)

router = APIRouter()

# Past Projects
@router.post("/{user_id}/past-projects", response_model=UserPastProjectOut)
def create_past_project(
    user_id: int,
    project: UserPastProjectCreate,
    db: Session = Depends(get_db),
):
    db_project = crud.add_past_project(db, user_id, project)
    if not db_project:
        raise HTTPException(status_code=404, detail="User not found")
    return db_project


@router.get("/{user_id}/past-projects", response_model=List[UserPastProjectOut])
def list_past_projects(
    user_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(models.UserPastProject)
        .filter(models.UserPastProject.user_id == user_id)
        .all()
    )


# Skills
@router.post("/{user_id}/skills", response_model=UserSkillOut)
def create_user_skill(
    user_id: int,
    skill: UserSkillCreate,   # <-- request model must be Create, not Out
    db: Session = Depends(get_db),
):
    db_skill = crud.add_user_skill(db, user_id, skill)
    if not db_skill:
        raise HTTPException(status_code=404, detail="User not found")
    return db_skill

@router.get("/{user_id}/skills", response_model=List[UserSkillOut])
def list_user_skills(
    user_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(models.UserSkill)
        .filter(models.UserSkill.user_id == user_id)
        .all()
    )