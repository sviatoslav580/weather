import asyncio
from aiogram import Bot, Dispatcher
from handlers import handler
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
dp = Dispatcher()


# Запуск бота
async def main():
    bot = Bot(token="YOUR TOKEN, ВАШ ТОКЕН")

    dp.include_router(handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())