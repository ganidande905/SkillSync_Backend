from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import exc
from app.db import models
from app.schemas.project import ProjectCreate
from app.schemas.user_interests import UserInterestCreate
from app.utils.hashing import Hash
from app.schemas.user_details import UserCreate, UserLogin
from app.schemas.user_past_projects import UserPastProjectCreate
from app.schemas.user_skills import UserSkillCreate

# Lookups 

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

# Users
def create_user(db: Session, user_in: UserCreate) -> models.User:
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise ValueError("Email already registered")

    hashed_password = Hash.hash(user_in.password)
    db_user = models.User(
        name=user_in.name,
        email=user_in.email,
        university=user_in.university,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_user(db: Session, user_in: UserLogin) -> Optional[models.User]:
    db_user = get_user_by_email(db, user_in.email)
    if not db_user:
        return None
    if not Hash.verify(user_in.password, db_user.hashed_password):
        return None
    return db_user

# Projects
def add_past_project(db: Session, user_id: int, past_project_in: UserPastProjectCreate) -> Optional[models.UserPastProject]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    past_project = models.UserPastProject(
        user_id=user_id,
        project_title=past_project_in.project_title,
        description=past_project_in.description,
        technologies_used=past_project_in.technologies_used,
    )
    db.add(past_project)
    db.commit()
    db.refresh(past_project)
    return past_project
# Skills
def add_user_skill(db: Session, user_id: int, skill_in: UserSkillCreate) -> Optional[models.UserSkill]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    user_skill = models.UserSkill(
        user_id=user_id,
        skill_name=skill_in.skill_name,
        proficiency_level=skill_in.proficiency_level,
    )
    db.add(user_skill)
    db.commit()
    db.refresh(user_skill)
    return user_skill

# Interests
def add_user_interest(db:Session, user_id:int, interest_in: UserInterestCreate) -> Optional[models.UserInterest]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    user_interest = models.UserInterest(
        user_id=user_id,
        interest_name=interest_in.interest_name,
    )
    db.add(user_interest)
    db.commit()
    db.refresh(user_interest)
    return user_interest

# projects
def add_project(db: Session, user_id: int, project_in: ProjectCreate ) -> Optional[models.Project]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    
    user_project = models.Project(
        user_id=user_id,
        project_name=project_in.project_name,
        description=project_in.description,
        repository_url=project_in.repository_url,
        
    )
    db.add(user_project)
    db.commit()
    db.refresh(user_project)
    return user_project
