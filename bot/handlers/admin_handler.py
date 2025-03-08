from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from config.settings import CONFIG
from database.crud import db
import json

admin_router = Router()

@admin_router.message(Command("get_db_dump"))
async def get_db_dump(message: Message):
    if message.from_user.id != CONFIG.ADMIN_IDS:
        return await message.answer("⛔ Доступ запрещен")
    
    try:
        data = db.get_dump()
        
        with open("survey_dump.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        await message.answer_document(
            document=FSInputFile("survey_dump.json"),
            caption="Дамп базы данных"
        )
        
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

@admin_router.message(Command("clear_db"))
async def clear_db(message: Message):
    if message.from_user.id in CONFIG.ADMIN_IDS:
        db.users.delete_many({})
        await message.answer("База данных очищена!")