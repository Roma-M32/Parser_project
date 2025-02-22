# 📰 Habr Article Parser

Этот Python-скрипт парсит последние статьи с Habr и сохраняет их в `articles.json`.

## 🚀 Установка и запуск

1. **Клонируем репозиторий:**
   ```bash
   git clone https://github.com/ТВОЙ_GITHUB_USERNAME/habr_parser.git
   cd habr_parser

2. **Создаём виртуальное окружение и устанавливаем зависимости:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt

3. **Запускаем парсер:**
   ```bash
   python3 parser.py

## 📌 Пример данных

[
    {"title": "Как работает Python?"},
    {"title": "Лучшие практики Django"},
    {"title": "Парсим сайты с BeautifulSoup"}
]

## 🕵️‍♂️ Парсинг сложных сайтов (Selenium)

Этот парсер использует **Selenium** для обработки сайтов, которые загружают контент через **JavaScript**.

### 📌 Использование:

1. Установите зависимости:
   ```bash
   pip install selenium webdriver-manager chromedriver-autoinstaller

2. Запустите:
   ```bash
   python3 selenium_parser.py

## 🗄 Сохранение данных в PostgreSQL

Теперь парсер автоматически сохраняет статьи в базу данных **PostgreSQL** с помощью **SQLAlchemy**.

### 📌 Как настроить базу?
1. Установите PostgreSQL:
   ```bash
   sudo apt install postgresql  # Ubuntu/Linux
   brew install postgresql  # macOS

2. Создайте базу:
   ```sql
   CREATE DATABASE parser_db;
   CREATE USER parser_user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE parser_db TO parser_user;

3. Установите зависимости:
   ```bash
   pip install sqlalchemy psycopg2 dotenv

4. Создайте .env файл и добавьте:
   ```bash
   DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost/DATABASE

5. Запустите парсер:
   ```bash
   python3 parser.py

6. Данные будут сохраняться в PostgreSQL, а проверить их можно так:
   ```sql
   SELECT * FROM articles;

## 🤖 Интеграция с Telegram-ботом

Теперь парсер можно вызывать прямо из Telegram! Бот также может отправлять последние статьи.

### 📌 Как запустить бота?
1. Добавьте в `.env` токен бота:
 - BOT_TOKEN=ваш_телеграм_токен

2. Установите `aiogram` (если ещё не установлен):
   ```bash
   pip3 install aiogram

3. Запустите бота:
   ```bash
   python3 bot.py

4. Используйте команды:
 - /start
 - /articles

 ## Автор: 
 - Роман Мосин 
 - https://github.com/Roma-M32