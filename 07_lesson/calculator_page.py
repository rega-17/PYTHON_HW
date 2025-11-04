from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            "1": (By.XPATH, "//span[text()='1']"),
            "2": (By.XPATH, "//span[text()='2']"),
            "3": (By.XPATH, "//span[text()='3']"),
            "4": (By.XPATH, "//span[text()='4']"),
            "5": (By.XPATH, "//span[text()='5']"),
            "6": (By.XPATH, "//span[text()='6']"),
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "9": (By.XPATH, "//span[text()='9']"),
            "0": (By.XPATH, "//span[text()='0']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "-": (By.XPATH, "//span[text()='-']"),
            "*": (By.XPATH, "//span[text()='×']"),
            "/": (By.XPATH, "//span[text()='÷']"),
            "=": (By.XPATH, "//span[text()='=']"),
            "C": (By.XPATH, "//span[text()='C']")
        }

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_button(self, button):
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()

    def wait_for_result(self, expected_result, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.result_display, expected_result)
        )
        return self.driver.find_element(*self.result_display).text