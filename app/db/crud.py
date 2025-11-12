from typing import Optional
from sqlalchemy.orm import Session
from app.db import models
from datetime import datetime, date
from sqlalchemy import func
from app.utils.hashing import Hash
from app.schemas.user_details import UserCreate, UserLogin




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



def verify_user(db:Session, user_in:UserLogin):
    db_user = get_user_by_email(db, user_in.email)
    if not db_user:
        return None
    if not Hash.verify(user_in.password, db_user.hashed_password):
        return None
    return db_user



def add_past_projects(db:Session,user_email:str,user_in: models.UserPastProject):
    db_user = get_user_by_email(db, user_email)
    if not db_user:
        return None
    past_project= models.UserPastProject(
        project_title=user_in.project_title,
        description=user_in.description,
        technologies_used=user_in.technologies_used,
        user_email =user_email
        
    )
    db.add(past_project)
    db.commit()
    db.refresh(past_project)
    return past_project