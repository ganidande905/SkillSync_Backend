from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import models
from app.schemas.team import TeamOut
from app.utils.matching import generate_team_for_project


router = APIRouter()


@router.post("/{project_id}/generate-team", response_model=TeamOut)
def generate_team(
    project_id: int,
    db: Session = Depends(get_db),
):
    team = generate_team_for_project(db, project_id=project_id)
    if not team:
        raise HTTPException(
            status_code=400,
            detail="Cannot generate team (project not found, no requirements, or no suitable users).",
        )
    return team