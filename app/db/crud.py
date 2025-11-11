from typing import Optional
from sqlalchemy.orm import Session
from app.db import models
from datetime import datetime, date
from sqlalchemy import func
from app.utils.hashing import Hash
from app.schemas.user_details import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user_in: UserCreate):
    hashed_password = Hash.hash(user_in.password) 
    db_user = models.User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user