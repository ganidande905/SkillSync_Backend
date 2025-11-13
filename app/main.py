from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.db import engine, Base
from app.routes import auth, onboarding, projects, team, team_invites, team_matching , leaderboard

app = FastAPI(title="SkillSync API")


@app.on_event("startup")
def on_startup():
    print("Registered tables:", Base.metadata.tables.keys())
    print("Onboarding router: ", onboarding.router)
    Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(onboarding.router, prefix="/onboarding", tags=["Onboarding"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(leaderboard.router, prefix="/leaderboard", tags=["Leaderboard"])
app.include_router(team.router, prefix="/teams", tags=["Teams"])
app.include_router(team_matching.router, prefix="/projects", tags=["Team Matching"])
app.include_router(team_invites.router, prefix="/teams", tags=["Team Invites"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SkillSync API!"}