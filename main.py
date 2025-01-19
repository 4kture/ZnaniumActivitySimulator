from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import time
from config import settings

USERNAME = settings['login']
PASSWORD = settings['password']
BOOK_URL = settings['book_url']


def create_driver():
    print("Создание драйвера...")
    service = Service(binary_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=options)
    print("Драйвер создан.")
    return driver


def login_to_znanium(driver):
    print("Попытка войти в систему...")
    driver.get("https://znanium.ru/site/login")
    time.sleep(3)

    username_field = driver.find_element(By.ID, "loginform-username")
    username_field.send_keys(USERNAME)

    password_field = driver.find_element(By.ID, "loginform-password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    time.sleep(5)
    print("Вход выполнен успешно.")


def open_book_and_wait(driver):
    print(f"Открытие книги: {BOOK_URL}")
    driver.get(BOOK_URL)
    time.sleep(60)
    print("Книга открыта. Ожидание завершено.")


def close_session(driver):
    print("Закрытие сессии...")
    driver.delete_all_cookies()
    driver.close()
    driver.quit()
    print("Сессия закрыта.")


def main():
    try:
        while True:
            print("Запуск нового цикла...")
            driver = create_driver()
            login_to_znanium(driver)
            open_book_and_wait(driver)
            close_session(driver)
            print("Цикл завершен. Ожидание 60    минут...")
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Скрипт остановлен пользователем.")


if __name__ == "__main__":
    main()
