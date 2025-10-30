from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/dynamicid")

    time.sleep(2)


    blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")

    blue_button.click()

    time.sleep(2)

    print("Успешно! Клик по синей кнопке с динамическим ID выполнен.")

finally:
    # Закрываем браузер
    driver.quit()