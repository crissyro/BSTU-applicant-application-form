from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.keyboards import main_menu
from aiogram.fsm.context import FSMContext
from utils.texts import START_TEXT

start_router = Router()

@start_router.message(Command("start"))
@start_router.message(F.text.in_(["🏠 В главное меню", "🚫 Отмена"]))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
         START_TEXT,
         reply_markup=main_menu(),
         parse_mode="Markdown"
    )
    await message.answer(
        "🏠 Вы в главном меню:",
        reply_markup=main_menu()
    )
