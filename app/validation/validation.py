from pydantic import BaseModel, ValidationError, validator

class SurveyValidator(BaseModel):
    gender: str
    grade: str
    school: str
    profile: str
    subjects: str
    scores: str
    universities: str
    specialties: str
    military_dep: str
    bstu: str

    @validator('school')
    def validate_school(cls, value: int):
        if len(value) < 15 or len(value) > 100:
            raise ValueError('Название школы должно быть от 2 до 100 символов')
        return value

    @validator('scores')
    def validate_scores(cls, v):
        if not v.isdigit():
            raise ValueError('Баллы должны быть числом')
        if int(v) < 0 or int(v) > 300:
            raise ValueError('Баллы должны быть в диапазоне 0-300')
        return v

def validate_answer(step: str, value: str):
    try:
        if step == 'scores':
            SurveyValidator.validate_scores(None, value)
        elif step == 'school':
            SurveyValidator.validate_school(None, value)
        return True, None
    except ValidationError as e:
        return False, e.errors()[0]['msg']