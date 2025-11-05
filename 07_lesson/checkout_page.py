from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Заполняет информацию для оформления заказа"""
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self):
        """Получает итоговую сумму с ожиданием элемента"""
        wait = WebDriverWait(self.driver, 10)

        # Ждем появления элемента с итоговой суммой
        total_element = wait.until(
            EC.presence_of_element_located(self.total_label)
        )
        total_text = total_element.text

        # Извлекаем числовое значение
        return total_text.split("$")[-1] if "$" in total_text else total_text