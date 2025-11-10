import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data import config
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(bot: Bot, dp: Dispatcher):
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(bot)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(bot)


async def main():
    # Bot va dispatcher obyektlarini yaratamiz
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # ✅ Shu tarzda ishlaydi
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Routerni handlerlardan ulash
    dp.include_routers(
        handlers.users.start.router,
        handlers.users.help.router,
        handlers.users.echo.router,
    )

    # Startup funksiyasini chaqirish
    await on_startup(bot, dp)

    print("🤖 Bot ishga tushdi!")
    await dp.start_polling(bot)  # Botni ishga tushiramiz


if __name__ == "__main__":
    asyncio.run(main())
