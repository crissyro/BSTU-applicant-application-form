from aiogram.utils.keyboard import InlineKeyboardBuilder

def start_survey_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="▶️ Начать опрос", callback_data="start_survey")
    return builder.as_markup()

def gender_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="♂️ Мужской", callback_data="answer:gender:male")
    builder.button(text="♀️ Женский", callback_data="answer:gender:female")
    builder.button(text="🔙 Назад", callback_data="nav_back")
    builder.adjust(2)
    return builder.as_markup()