from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.db.db import get_db
from app.db import models
from app.schemas.team import TeamOut

router = APIRouter()


@router.get("/{team_id}", response_model=TeamOut)
def get_team(
    team_id: int,
    db: Session = Depends(get_db),
):
    team = (
        db.query(models.Team)
        .options(joinedload(models.Team.members))
        .filter(models.Team.id == team_id)
        .first()
    )
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team