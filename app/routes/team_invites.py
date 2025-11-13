from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.db import models
from app.schemas.team import TeamMemberOut
from app.schemas.team_members import TeamInviteResponse

router = APIRouter(prefix="/team-invites", tags=["Team Invites"])

@router.get("/{user_id}", response_model=List[TeamMemberOut])
def get_user_team_invites(
    user_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(models.TeamMember)
        .filter(
            models.TeamMember.user_id == user_id,
            models.TeamMember.statusin_(["pending","accepted"])
        )
        .all()
    )


@router.post("/{team_id}/respond")
def respond_to_team_invite(
    team_id: int,
    body: TeamInviteResponse,
    user_id: int,
    db: Session = Depends(get_db),
):
    if body.status not in {"accepted", "rejected"}:
        raise HTTPException(status_code=400, detail="Invalid status")

    member = (
        db.query(models.TeamMember)
        .filter(
            models.TeamMember.team_id == team_id,
            models.TeamMember.user_id == user_id,
        )
        .first()
    )

    if not member:
        raise HTTPException(status_code=404, detail="Team membership not found")

    if member.status != "pending":
        raise HTTPException(
            status_code=400,
            detail=f"Invitation already {member.status}",
        )

    member.status = body.status
    db.commit()
    db.refresh(member)

    return {"detail": body.status}