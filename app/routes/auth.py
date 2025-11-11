from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas.user_details import UserCreate, UserLogin, UserOut
from app.utils.hashing import Hash
from app.db import models
from app.db import crud
router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db, user)


@router.post("/login", response_model=UserOut)

def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.verify_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user