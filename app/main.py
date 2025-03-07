import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.settings import CONFIG
from handlers import (
    start_handler, admin_handler, 
    survey_handler
)

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=CONFIG.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(start_handler.start_router)
    dp.include_router(survey_handler.survey_router)
    dp.include_router(admin_handler.admin_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())