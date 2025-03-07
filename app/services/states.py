from aiogram.fsm.state import StatesGroup, State

class SurveyStates(StatesGroup):
    gender = State()
    grade = State()
    school = State()
    profile = State()
    subjects = State()
    scores = State()
    universities = State()
    specialties = State()
    military_dep = State()
    bstu = State()
    confirm = State()