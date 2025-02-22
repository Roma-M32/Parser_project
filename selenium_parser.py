import time
import logging
import selenium.webdriver
import chromedriver_autoinstaller

# Устанавливаем Chrome WebDriver (если не установлен)
chromedriver_autoinstaller.install()

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_dynamic_content(url):
    """Парсинг страницы, которая загружается через JavaScript"""
    logging.info(f"🔍 Открываем сайт: {url}")

    # Запускаем браузер
    options = selenium.webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запуск без интерфейса (фон)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    driver = selenium.webdriver.Chrome(options=options)
    driver.get(url)

    # Ждём загрузки JavaScript-контента
    time.sleep(5)

    # Получаем HTML-код страницы
    page_source = driver.page_source
    driver.quit()  # Закрываем браузер

    return page_source

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/js/"  # Пример страницы с JS-контентом
    html = get_dynamic_content(url)
    print(html[:1000])  # Покажет первые 1000 символов страницы
