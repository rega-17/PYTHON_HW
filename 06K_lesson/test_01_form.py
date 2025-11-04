from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    # Инициализация Edge
    driver = webdriver.Edge()

    try:
        # Шаг 1: Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 15)

        # Шаг 2: Заполнение формы
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
        first_name.clear()
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.NAME, "last-name")
        last_name.clear()
        last_name.send_keys("Петров")

        address = driver.find_element(By.NAME, "address")
        address.clear()
        address.send_keys("Ленина, 55-3")

        email = driver.find_element(By.NAME, "e-mail")
        email.clear()
        email.send_keys("test@skypro.com")

        phone = driver.find_element(By.NAME, "phone")
        phone.clear()
        phone.send_keys("+7985899998787")

        # Zip code - оставляем пустым
        zip_code = driver.find_element(By.NAME, "zip-code")
        zip_code.clear()

        city = driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("Москва")

        country = driver.find_element(By.NAME, "country")
        country.clear()
        country.send_keys("Россия")

        job_position = driver.find_element(By.NAME, "job-position")
        job_position.clear()
        job_position.send_keys("QA")

        company = driver.find_element(By.NAME, "company")
        company.clear()
        company.send_keys("SkyPro")

        # Шаг 3: Нажать кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Ожидание применения стилей валидации
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.is-invalid")))

        # Шаг 4: Проверка, что поле Zip code подсвечено красным
        zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
        zip_code_classes = zip_code_field.get_attribute("class")
        assert "is-invalid" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"

        # Шаг 5: Проверка, что остальные поля подсвечены зеленым
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]

        for field_id in fields_to_check:
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field_classes = field.get_attribute("class")
            assert "is-valid" in field_classes, f"Поле {field_id} должно быть подсвечено зеленым"

    finally:
        driver.quit()