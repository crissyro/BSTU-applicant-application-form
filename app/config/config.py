import os
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

class Config:
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    storage = MemoryStorage()