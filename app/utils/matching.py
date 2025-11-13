from typing import Optional, List, Dict
from sqlalchemy.orm import Session, joinedload

from app.db import models

PROFICIENCY_SCORE = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
}


def _proficiency_value(level: str | None) -> int:
    if not level:
        return 0
    return PROFICIENCY_SCORE.get(level.lower(), 0)


def generate_team_for_project(
    db: Session,
    project_id: int,
    team_size: int = 4,
) -> Optional[models.Team]:
    project = (
        db.query(models.Project)
        .options(
            joinedload(models.Project.skill_requirements),
            joinedload(models.Project.owner),
            )
        .filter(models.Project.id == project_id)
        .first()
    )
    if not project:
        return None
    if project.team:
        return project.team

    requirements = project.skill_requirements
    if not requirements:
        return None
    owner = project.owner
    owner_university = owner.university if owner else None
    users = (
        db.query(models.User)
        .options(joinedload(models.User.skills))
        .all()
    )

    candidates = [u for u in users if u.id != project.user_id and u.university == owner_university]
    scores: Dict[int, float] = {}

    for user in candidates:
        score = 0.0
        user_skills_by_name = {
            s.skill_name.lower(): s for s in user.skills
        }

        for req in requirements:
            req_name = req.skill_name.lower()
            if req_name not in user_skills_by_name:
                continue

            user_skill = user_skills_by_name[req_name]

            user_prof = _proficiency_value(user_skill.proficiency_level)
            min_prof = _proficiency_value(req.min_proficiency_level)
            if user_prof < min_prof:
                continue

            weight = req.weight or 1
            score += user_prof * weight

        scores[user.id] = score

    sorted_users = sorted(
        [u for u in candidates if scores.get(u.id, 0) > 0],
        key=lambda u: scores[u.id],
        reverse=True,
    )

    selected_users = sorted_users[:team_size]
    if not selected_users:
        return None
    team = models.Team(
        team_name=f"{project.project_name} Team",
        description=project.requirements or project.description,
        project_id=project.id,
        creator_id=project.user_id,
    )
    db.add(team)
    db.flush() 
    for user in selected_users:
        member = models.TeamMember(
            team_id=team.id,
            user_id=user.id,
            role="member",
            status="pending",
        )
        db.add(member)

    db.commit()
    db.refresh(team)
    return team