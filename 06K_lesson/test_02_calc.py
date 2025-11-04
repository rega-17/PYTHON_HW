from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    # Инициализация Chrome
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 50)  # Увеличено до 50 секунд для учета задержки

        # Шаг 2: Ввести значение 45 в поле delay
        delay_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Шаг 3: Нажать на кнопки 7 + 8 =
        # Кнопка 7
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        # Кнопка +
        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        # Кнопка 8
        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

        # Кнопка =
        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()

        # Шаг 4: Проверить, что в окне отобразится результат 15 через 45 секунд
        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")

        # Ожидаем появления результата 15 с учетом задержки 45 секунд
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        # Проверяем результат
        result_text = result_element.text
        assert result_text == "15", f"Ожидался результат '15', но получили '{result_text}'"

    finally:
        driver.quit()