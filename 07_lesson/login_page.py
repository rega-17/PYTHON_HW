from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_button = (By.CLASS_NAME, "error-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Выполняет вход в систему и закрывает предупреждение"""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

        # Закрываем предупреждение о смене пароля, если оно появилось
        try:
            wait = WebDriverWait(self.driver, 5)
            error_button = wait.until(EC.element_to_be_clickable(self.error_button))
            error_button.click()
        except:
            # Если предупреждения нет, продолжаем работу
            pass