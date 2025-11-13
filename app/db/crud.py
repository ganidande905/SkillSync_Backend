from typing import Optional
from fastapi import HTTPException
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

def get_user_by_id(db: Session, user_id: int) -> models.User:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

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

def create_project(
    db: Session,
    user_id: int,
    project_in: ProjectCreate,
) -> Optional[models.Project]:
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    project = models.Project(
        user_id=user_id,
        project_name=project_in.project_name,
        description=project_in.description,
        repository_url=project_in.repository_url,
        requirements=project_in.requirements,
    )

    db.add(project)
    db.flush()  # get project.id without committing yet
    for req in project_in.skill_requirements or []:
        db_req = models.ProjectSkillRequirement(
            project_id=project.id,
            skill_name=req.skill_name,
            min_proficiency_level=req.min_proficiency_level,
            weight=req.weight,
        )
        db.add(db_req)

    db.commit()
    db.refresh(project)
    return project

def get_team_member(db: Session, team_id: int, user_id: int):
    return (
        db.query(models.TeamMember)
        .filter(
            models.TeamMember.team_id == team_id,
            models.TeamMember.user_id == user_id
        )
        .first()
    )

def update_team_member_status(db: Session, team_id: int, user_id: int, status: str):
    member = get_team_member(db, team_id, user_id)
    if not member:
        return None
    member.status = status
    db.commit()
    db.refresh(member)
    return member

def get_team(db: Session, team_id: int):
    return (
        db.query(models.Team)
        .filter(models.Team.id == team_id)
        .first()
    )