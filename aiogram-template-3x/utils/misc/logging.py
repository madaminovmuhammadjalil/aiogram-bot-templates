import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from data import config
import asyncio

# Logging sozlamalari
logging.basicConfig(
    format='%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
    # level=logging.DEBUG,  # kerak bo‘lsa darajani o‘zgartiring
)

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # Sizning handlerlar va startup funksiyalaringizni ulash
    # dp.include_router(...)

    logging.info("🤖 Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
