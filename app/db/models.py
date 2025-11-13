from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    university = Column(String(200), nullable=True)
    
    interests = relationship("UserInterest", back_populates="user", cascade="all, delete-orphan")
    past_projects = relationship("UserPastProject", back_populates="user", cascade="all, delete-orphan")
    skills = relationship("UserSkill", back_populates="user", cascade="all, delete-orphan")
    projects = relationship("Project", back_populates="owner", cascade="all, delete-orphan", foreign_keys="Project.user_id")
    teams_created = relationship("Team", back_populates="creator", cascade="all, delete-orphan", foreign_keys="Team.creator_id")
    team_memberships = relationship("TeamMember", back_populates="user", cascade="all, delete-orphan")


class UserInterest(Base):
    __tablename__ = "user_interests"
    __table_args__ = (
        UniqueConstraint("user_id", "interest_name", name="uq_user_interest_user_interest_name"),
    )
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interest_name = Column(String(150), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="interests")


class UserPastProject(Base):
    __tablename__ = "user_past_projects"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    technologies_used = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="past_projects")


class UserSkill(Base):
    __tablename__ = "user_skills"
    __table_args__ = (
        UniqueConstraint("user_id", "skill_name", name="uq_user_skill_user_skill_name"),
    )

    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    skill_name = Column(String(150), nullable=False)
    proficiency_level = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="skills")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    project_name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    repository_url = Column(String(300), nullable=False)
    progress = Column(Text, nullable=True)
    requirements = Column(Text, nullable=True) 
    last_commit_message = Column(Text, nullable=True)
    last_commit_sha = Column(String(64), nullable=True)
    last_commit_url = Column(String(500), nullable=True)
    skill_requirements = relationship(
        "ProjectSkillRequirement",
        back_populates="project",
        cascade="all, delete-orphan",
    )
    owner = relationship("User", back_populates="projects")
    team = relationship("Team", back_populates="project", uselist=False)

class ProjectSkillRequirement(Base):
    __tablename__ = "project_skill_requirements"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)

    skill_name = Column(String(150), nullable=False)
    min_proficiency_level = Column(String(50), nullable=True) 
    weight = Column(Integer, nullable=True) 

    project = relationship("Project", back_populates="skill_requirements")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    team_name = Column(String(150), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    description = Column(Text, nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    creator = relationship("User", back_populates="teams_created")
    project = relationship("Project", back_populates="team")
    members = relationship("TeamMember", back_populates="team", cascade="all, delete-orphan")


class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    role = Column(String(100), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    team = relationship("Team", back_populates="members")
    status = Column(String(20), nullable=False, default="pending") 
    user = relationship("User", back_populates="team_memberships")