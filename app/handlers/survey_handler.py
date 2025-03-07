from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from services.states import Survey
from validation.validation import validate_answer
from database.crud import db
from keyboards.keyboards import *
from utils.texts import format_summary, SUCCESS_MESSAGE


survey_router = Router()

@survey_router.message(F.text == "ℹ️ Мой профиль")
async def view_profile(message: Message):
    user_data = db.get_user(message.from_user.id)
    if not user_data.get('gender'):
        await message.answer("❌ Вы еще не заполнили анкету!")
        return
    
    await message.answer(
        format_summary(user_data),
        reply_markup=edit_profile_kb()
    )

@survey_router.message(F.text == "🎓 Начать анкету")
async def start_survey(message: Message, state: FSMContext):
    await state.set_state(Survey.GENDER)
    await message.answer(
        "👤 *Шаг 1/10*\nВыберите ваш пол:",
        reply_markup=gender_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.GENDER, F.text.in_(["👨 Мужской", "👩 Женский"]))
async def process_gender(message: Message, state: FSMContext):
    db.save_answer(message.from_user.id, {"gender": message.text})
    await state.set_state(Survey.GRADE)
    await message.answer(
        "🎓 *Шаг 2/10*\nВыберите ваш класс:",
        reply_markup=grade_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.GRADE, F.text.in_(["10 класс", "11 класс"]))
async def process_grade(message: Message, state: FSMContext):
    db.save_answer(message.from_user.id, {"grade": message.text})
    await state.set_state(Survey.SCHOOL)
    await message.answer(
        "🏫 *Шаг 3/10*\nВведите полное название вашей школы:",
        reply_markup=back_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.SCHOOL)
async def process_school(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.GRADE)
        await message.answer(
            "🎓 Выберите ваш класс:",
            reply_markup=grade_kb()
        )
        return
    
    if len(message.text) < 2:
        await message.answer("❌ Название школы слишком короткое!")
        return
    
    db.save_answer(message.from_user.id, {"school": message.text})
    await state.set_state(Survey.PROFILE)
    await message.answer(
        "📊 *Шаг 4/10*\nВыберите профиль обучения:",
        reply_markup=profile_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.PROFILE)
async def process_profile(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.SCHOOL)
        await message.answer(
            "🏫 Введите название школы:",
            reply_markup=back_kb()
        )
        return
    
    db.save_answer(message.from_user.id, {"profile": message.text})
    await state.set_state(Survey.SUBJECTS)
    await message.answer(
        "📚 *Шаг 5/10*\nВведите предметы для ЕГЭ через запятую:",
        reply_markup=back_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.SUBJECTS)
async def process_subjects(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.PROFILE)
        await message.answer(
            "📊 Выберите профиль обучения:",
            reply_markup=profile_kb()
        )
        return
    
    db.save_answer(message.from_user.id, {"subjects": message.text})
    await state.set_state(Survey.SCORES)
    await message.answer(
        "🎯 *Шаг 6/10*\nПланируемый суммарный балл за 3 предмета:",
        reply_markup=back_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.SCORES)
async def process_scores(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.SUBJECTS)
        await message.answer(
            "📚 Введите предметы для ЕГЭ:",
            reply_markup=back_kb()
        )
        return
    
    try:
        score = int(message.text)
        if not 0 <= score <= 300:
            raise ValueError
        db.save_answer(message.from_user.id, {"scores": score})
        await state.set_state(Survey.UNIVERSITIES)
        await message.answer(
            "🏛 *Шаг 7/10*\nРассматриваемые вузы (через запятую):",
            reply_markup=back_kb(),
            parse_mode="Markdown"
        )
    except:
        await message.answer("❌ Введите число от 0 до 300!")

# Обработка вузов
@survey_router.message(Survey.UNIVERSITIES)
async def process_universities(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.SCORES)
        await message.answer(
            "🎯 Введите планируемый балл:",
            reply_markup=back_kb()
        )
        return
    
    db.save_answer(message.from_user.id, {"universities": message.text})
    await state.set_state(Survey.SPECIALTIES)
    await message.answer(
        "🎓 *Шаг 8/10*\nИнтересующие специальности:",
        reply_markup=back_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.SPECIALTIES)
async def process_specialties(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.UNIVERSITIES)
        await message.answer(
            "🏛 Введите рассматриваемые вузы:",
            reply_markup=back_kb()
        )
        return
    
    db.save_answer(message.from_user.id, {"specialties": message.text})
    await state.set_state(Survey.MILITARY)
    await message.answer(
        "🎖 *Шаг 9/10*\nХотите учиться на военной кафедре?",
        reply_markup=yes_no_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.MILITARY)
async def process_military(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.SPECIALTIES)
        await message.answer(
            "🎓 Введите специальности:",
            reply_markup=back_kb()
        )
        return
    
    db.save_answer(message.from_user.id, {"military_dep": message.text})
    await state.set_state(Survey.BSTU)
    await message.answer(
        "🏢 *Шаг 10/10*\nХотите учиться в БГТУ им. Шухова?",
        reply_markup=yes_no_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.BSTU)
async def process_bstu(message: Message, state: FSMContext):
    if message.text == "🔙 Назад":
        await state.set_state(Survey.MILITARY)
        await message.answer(
            "🎖 Хотите учиться на военной кафедре?",
            reply_markup=yes_no_kb()
        )
        return
    
    db.save_answer(message.from_user.id, {"bstu": message.text})
    await state.set_state(Survey.CONFIRM)
    user_data = db.get_user_data(message.from_user.id)
    await message.answer(
        f"✅ *Проверьте данные:*\n\n{format_summary(user_data)}",
        reply_markup=confirm_kb(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.CONFIRM, F.text == "✅ Подтвердить")
async def confirm_survey(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        SUCCESS_MESSAGE,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

@survey_router.message(Survey.CONFIRM, F.text == "✏️ Редактировать")
async def edit_survey(message: Message, state: FSMContext):
    await state.set_state(Survey.GENDER)
    await message.answer(
        "✏️ Начнем редактирование заново:",
        reply_markup=gender_kb()
    )