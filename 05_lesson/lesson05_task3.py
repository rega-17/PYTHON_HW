from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр браузера Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Ждем немного для загрузки страницы
    time.sleep(2)

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим в поле текст "Sky"
    input_field.send_keys("Sky")

    # Ждем немного чтобы увидеть результат
    time.sleep(1)

    # Очищаем поле
    input_field.clear()

    # Ждем немного после очистки
    time.sleep(1)

    # Вводим в поле текст "Pro"
    input_field.send_keys("Pro")

    # Ждем немного чтобы увидеть результат
    time.sleep(2)

    print("Успешно! Текст 'Sky' введен, поле очищено, текст 'Pro' введен.")

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт.")