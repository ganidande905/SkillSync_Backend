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

@router.get("/users/lookup")
def lookup_user_id(email: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.id}

@router.post("/{user_id}/complete")
def complete_onboarding(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_onboarded = True
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"detail": "Onboarding completed", "is_onboarded": user.is_onboarded}