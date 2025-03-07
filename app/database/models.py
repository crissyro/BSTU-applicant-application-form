from pydantic import BaseModel

class UserResponse(BaseModel):
    gender: str | None = None
    grade: str | None = None
    school: str | None = None
    profile: str | None = None
    subjects: str | None = None
    scores: str | None = None
    universities: str | None = None
    specialties: str | None = None
    military_dep: str | None = None
    bstu: str | None = None