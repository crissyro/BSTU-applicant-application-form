from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🎓 Начать опрос")
    builder.button(text="ℹ️ Мой профиль")
    return builder.as_markup(resize_keyboard=True)

def gender_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="👨 Мужской")
    builder.button(text="👩 Женский")
    builder.button(text="🔙 Назад")
    builder.button(text="🚫 Отмена")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def back_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🔙 Назад")
    return builder.as_markup(resize_keyboard=True)

def profile_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="💼 Соц-экономический")
    builder.button(text="🧮 Физмат")
    builder.button(text="🧪 Биохим")
    builder.button(text="📚 Гуманитарный")
    builder.button(text="💻 Инфотех")
    builder.button(text="🔙 Назад")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def yes_no_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="✅ Да")
    builder.button(text="❌ Нет")
    builder.button(text="🔙 Назад")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def confirm_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="✅ Подтвердить")
    builder.button(text="✏️ Редактировать")
    return builder.as_markup(resize_keyboard=True)

def edit_profile_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="✏️ Перезаполнить анкету")
    builder.button(text="🏠 В главное меню")
    return builder.as_markup(resize_keyboard=True)

def grade_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="10 класс", callback_data="answer:grade:10")
    builder.button(text="11 класс", callback_data="answer:grade:11")
    builder.button(text="🔙 Назад", callback_data="nav_back")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)