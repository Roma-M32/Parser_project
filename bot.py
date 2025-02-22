import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from database import SessionLocal, Article

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Настраиваем бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Включаем логирование
logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start_command(message: Message):
    """Приветствие и описание команд"""
    await message.answer(
        "👋 Привет! Я бот-парсер статей с Habr.\n\n"
        "Используй команду /articles, чтобы получить последние 5 статей."
    )

@dp.message(Command("articles"))
async def get_articles_command(message: Message):
    """Отправляет пользователю последние 5 статей из базы"""
    session = SessionLocal()
    articles = session.query(Article).order_by(Article.id.desc()).limit(5).all()
    session.close()

    if not articles:
        await message.answer("😕 В базе пока нет статей. Запусти парсер и попробуй снова.")
        return

    response_text = "📰 **Последние статьи:**\n\n"
    for article in articles:
        response_text += f"🔹 {article.title}\n"

    await message.answer(response_text, parse_mode="Markdown")

async def main():
    """Функция запуска бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())