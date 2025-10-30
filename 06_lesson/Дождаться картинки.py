from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Переходим на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем загрузки контейнера с картинками
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "image-container"))
    )

    # Ждем пока загрузятся минимум 4 картинки
    images = WebDriverWait(driver, 15).until(
        lambda driver: driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        if len(driver.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 4
        else False
    )

    # Получаем src третьей картинки (индекс 2)
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)

finally:
    driver.quit()