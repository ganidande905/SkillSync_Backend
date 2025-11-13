from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.crud import calculate_user_score
from app.db.db import get_db
from app.db import models
from app.schemas.leaderboard import LeaderboardUser



router = APIRouter()

@router.get("/", response_model=list[LeaderboardUser])
async def get_leaderboard(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    rankings = []

    for user in users:
        score = await calculate_user_score(db, user)
        rankings.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "score": score,
        })

    rankings.sort(key=lambda x: x["score"], reverse=True)
    return rankings