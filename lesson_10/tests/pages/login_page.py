from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """Page Object для страницы авторизации"""
    
    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы логина
        
        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_button = (By.CLASS_NAME, "error-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации
        
        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Выполнить вход с логином '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему и закрывает предупреждение
        
        Args:
            username (str): Имя пользователя
            password (str): Пароль
            
        Returns:
            None
        """
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