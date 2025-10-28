from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Шаг 1: Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Шаг 2: Нажимаем на синюю кнопку
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    blue_button.click()

    # Шаг 3: Получаем текст из зеленой плашки
    # Ждем появления элемента с текстом AJAX
    green_badge = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    badge_text = green_badge.text

    # Шаг 4: Выводим текст в консоль
    print(badge_text)

finally:
    # Закрываем браузер
    driver.quit()