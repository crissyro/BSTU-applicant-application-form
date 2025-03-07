import asyncio
import logging
from aiogram import Dispatcher
from config.config import Config

async def main():
    logging.basicConfig(level=logging.INFO)
    
    dp = Dispatcher(Config.bot, storage=Config.storage)

    # TODO: make handlers
    # Example:
    # dp.register_message_handler(start_handler, commands=['start'])
    # dp.register_message_handler(help_handler, commands=['help'])
    # dp.register_message_handler(echo_handler, regexp='^/echo (.+)$')
    # dp.register_callback_query_handler(callback_handler)
    # ...

    try:
        await dp.start_polling()
    except Exception as e:
        logging.error(f'Error occurred while polling the bot: {e}')
    