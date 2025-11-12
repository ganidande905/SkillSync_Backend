from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.db import engine, Base
from app.db.models import User, UserInterest, UserPastProject, UserSkill, Project, Team, TeamMember
from app.routes import auth , onboarding
app = FastAPI(title = "SkillSync API")


@app.on_event("startup")
def on_startup():
    print("Registered tables:", Base.metadata.tables.keys())
    print("Onboarding router: ", onboarding.router)
    Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


app.include_router(auth.router , prefix="/auth", tags=["Authentication"])
app.include_router(onboarding.router , prefix="/onboarding", tags=["Onboarding"])
@app.get("/")
def read_root():
    return {"message": "Welcome to SkillSync API!"}
