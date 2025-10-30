from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройка FirefoxDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Переходим на страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Ждем немного для загрузки страницы
    time.sleep(2)

    # Находим поле username и вводим значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Введен username: tomsmith")

    # Находим поле password и вводим значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введен password: SuperSecretPassword!")

    # Ждем немного перед кликом
    time.sleep(1)

    # Находим и нажимаем кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Нажата кнопка Login")

    # Ждем загрузки следующей страницы
    time.sleep(2)

    # Находим зеленую плашку с сообщением об успехе
    success_message = driver.find_element(By.ID, "flash")

    # Получаем текст из зеленой плашки
    message_text = success_message.text
    print("\n" + "=" * 50)
    print("ТЕКСТ С ЗЕЛЕНОЙ ПЛАШКИ:")
    print(message_text)
    print("=" * 50)

    # Ждем немного чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрываем браузер методом quit()
    driver.quit()
    print("\nБраузер закрыт.")