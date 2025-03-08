from aiogram.fsm.state import StatesGroup, State

class Survey(StatesGroup):
    GENDER = State()
    GRADE = State()
    SCHOOL = State()
    PROFILE = State()
    SUBJECTS = State()
    SCORES = State()
    UNIVERSITIES = State()
    SPECIALTIES = State()
    MILITARY = State()
    BSTU = State()
    CONFIRM = State()