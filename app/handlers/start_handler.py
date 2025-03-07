from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from services.states import SurveyStates
from keyboards.keyboards import start_survey_kb, gender_kb
from utils.texts import START_TEXT
from database.crud import db

start_router = Router()

@start_router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer(START_TEXT, reply_markup=start_survey_kb())

@start_router.callback_query(F.data == "start_survey")
async def start_survey(callback: CallbackQuery, state: FSMContext):
    await db.update_user(callback.from_user.id, {})
    await state.set_state(SurveyStates.gender)
    await callback.message.edit_text("Выберите ваш пол:", reply_markup=gender_kb())