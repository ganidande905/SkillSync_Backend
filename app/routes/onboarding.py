from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas.user_past_projects import UserPastProjectCreate, UserPastProjectOut
from app.db import crud

router = APIRouter()

@router.post("/pastprojects", response_model=UserPastProjectOut)
def create_past_project(
    project: UserPastProjectCreate,
    db: Session = Depends(get_db),
):
    db_project = crud.add_past_projects(db, project.user_email,project)
    if not db_project:
        raise HTTPException(status_code=400, detail="Error adding past project (user not found?)")
    return db_project