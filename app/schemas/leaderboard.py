from pydantic import BaseModel

class LeaderboardUser(BaseModel):
    id: int
    name: str
    email: str
    score: int

    class Config:
        orm_mode = True