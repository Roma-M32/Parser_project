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

## 🎯 TODO (Идеи для улучшения)
 Отправка статей в Telegram

 Автор: 
 Роман Мосин 
 https://github.com/Roma-M32