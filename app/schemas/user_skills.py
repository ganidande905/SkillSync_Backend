from pydantic import BaseModel , EmailStr

class UserSkillBase(BaseModel):
    skill_name: str
    proficiency_level: str 

class UserSkillCreate(UserSkillBase):
    pass
class UserSkillOut(UserSkillBase):
    id: int
    user_id :int
    class Config:
        orm_mode = True
        
