import logging
import os
from aiogram import Bot, Dispatcher, executor, types
import aiosqlite

TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def init_db():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER
        )
        """)
        await db.commit()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("✅ Bot aktif! Ketik /daftar")

@dp.message_handler(commands=['daftar'])
async def daftar(message: types.Message):
    async with aiosqlite.connect("database.db") as db:
        await db.execute(
            "INSERT INTO users (telegram_id) VALUES (?)",
            (message.from_user.id,)
        )
        await db.commit()
    await message.answer("✅ Kamu berhasil daftar!")

if __name__ == "__main__":
    import asyncio
    asyncio.get_event_loop().run_until_complete(init_db())
    executor.start_polling(dp, skip_updates=True)
