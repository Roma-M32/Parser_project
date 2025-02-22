import requests
import logging
import json
from bs4 import BeautifulSoup
import schedule
import time

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# URL для парсинга
URL = "https://habr.com/ru/articles/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_articles():
    """Функция парсит статьи с Habr и сохраняет в JSON"""
    try:
        logging.info("🔍 Отправляем запрос на сайт...")
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Проверяем ошибки

        soup = BeautifulSoup(response.text, "lxml")
        articles = soup.find_all("h2")

        if not articles:
            logging.warning("⚠ Заголовки статей не найдены! Возможно, структура сайта изменилась.")
            return []

        data = [{"title": article.text.strip()} for article in articles[:5]]
        logging.info(f"✅ Найдено {len(data)} статей.")

        # Сохраняем в JSON
        with open("articles.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        logging.info("📁 Данные сохранены в articles.json")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Ошибка при запросе: {e}")
        return []

def run_parser():
    print("🔄 Запуск парсера...")
    get_articles()  # Вызываем функцию парсинга

# Запускаем парсер каждые 10 минут
schedule.every(10).minutes.do(run_parser)

print("✅ Парсер теперь работает по расписанию!")

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверяем задачи каждую минуту


if __name__ == "__main__":
    get_articles()
