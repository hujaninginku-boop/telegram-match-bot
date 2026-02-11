import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
import aiosqlite

TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def init_db():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            name TEXT,
            age INTEGER,
            gender TEXT,
            city TEXT,
            looking_for TEXT
        )
        """)
        await db.commit()

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Halo! Ketik /daftar untuk mulai.")

@dp.message(commands=["daftar"])
async def daftar(message: types.Message):
    await message.answer("Masukkan nama kamu:")

@dp.message()
async def save_user(message: types.Message):
    await message.answer("Terima kasih! (Versi dasar aktif)")

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
