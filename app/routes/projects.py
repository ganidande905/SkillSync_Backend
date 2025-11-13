from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import models
from app.db import crud
from app.schemas.project import (
    ProjectOut,
    ProjectCreate
)

router = APIRouter()

@router.post("/{user_id}/project", response_model=ProjectOut)
def create_project(
    user_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db),
):
    db_project = crud.add_project(db, user_id, project)
    if not db_project:
        raise HTTPException(status_code=404, detail="User not found")
    return db_project
@router.get("/{user_id}/projects", response_model=List[ProjectOut])
def list_user_projects(
    user_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(models.Project)
        .filter(models.Project.user_id == user_id)
        .all()
    )