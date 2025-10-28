from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    print("Загружаем страницу...")

    # Дадим странице полностью загрузиться
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Найдем кнопку разными способами
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"Всего кнопок на странице: {len(buttons)}")

    for i, btn in enumerate(buttons):
        print(f"Кнопка {i}: текст='{btn.text}', id='{btn.get_attribute('id')}', класс='{btn.get_attribute('class')}'")

    # Нажмем на кнопку с id="ajaxButton"
    blue_button = driver.find_element(By.ID, "ajaxButton")
    print("Нажимаем на кнопку...")
    blue_button.click()

    # Подождем и проверим что появилось
    import time

    time.sleep(2)  # временно для отладки

    # Посмотрим всю страницу
    print("Текущий HTML страницы:")
    print(driver.page_source)

except Exception as e:
    print(f"Произошла ошибка: {e}")
    import traceback

    traceback.print_exc()

finally:
    driver.quit()
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait

    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/ajax")

        # Нажимаем кнопку
        button = driver.find_element(By.ID, "ajaxButton")
        button.click()

        # Ждем появления текста любым способом
        wait = WebDriverWait(driver, 15)


        def text_appeared(driver):
            elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Data loaded with AJAX get request.')]")
            return elements[0] if elements else False


        element = wait.until(text_appeared)
        print(element.text)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    finally:
        driver.quit()