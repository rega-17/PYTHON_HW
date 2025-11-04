from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 15)

        # Заполнение формы через цикл
        fields_filling = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_name, value in fields_filling.items():
            field = wait.until(EC.presence_of_element_located((By.NAME, field_name)))
            field.clear()
            field.send_keys(value)

        # Zip code оставляем пустым
        driver.find_element(By.NAME, "zip-code").clear()

        # Нажимаем кнопку
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", submit_button)

        # Ждем появления класса alert-danger у zip-code
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
        )

        # Проверяем все поля
        assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

        for field_name in fields_filling.keys():
            assert "alert-success" in driver.find_element(By.ID, field_name).get_attribute("class")

    finally:
        driver.quit()