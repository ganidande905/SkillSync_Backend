from pydantic import BaseModel , EmailStr

class UserSkillBase(BaseModel):
    skill_name: str
    
class UserSkillCreate(UserSkillBase):
    user_id : int
    proficiency_level: str 

class UserSkillOut(UserSkillBase):
    id: int
    user_id: int
    proficiency_level: str
    class Config:
        orm_mode = True
        
