from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.checkout_button_css = (By.CSS_SELECTOR, "[data-test='checkout']")
        self.checkout_button_class = (By.CLASS_NAME, "checkout_button")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            checkout_btn = wait.until(EC.element_to_be_clickable(self.checkout_button))
            checkout_btn.click()
        except:
            try:
                checkout_btn = wait.until(EC.element_to_be_clickable(self.checkout_button_css))
                checkout_btn.click()
            except:
                checkout_btn = wait.until(EC.element_to_be_clickable(self.checkout_button_class))
                checkout_btn.click()