import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import config
from handlers import start_handler


async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(start_handler.start_router)

    
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())