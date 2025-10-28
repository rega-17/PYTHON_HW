from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Переходим на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Ожидаем загрузки поля ввода
    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "newButtonName"))
    )

    # Вводим текст SkyPro
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Находим и нажимаем синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()

    # Ждем изменения текста кнопки
    WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.ID, "updatingButton").text == "SkyPro"
    )

    # Получаем и выводим текст кнопки
    final_button_text = driver.find_element(By.ID, "updatingButton").text
    print(final_button_text)

finally:
    driver.quit()