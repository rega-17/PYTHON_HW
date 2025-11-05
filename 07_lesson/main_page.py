from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_to_cart(self, product_name):
        """Добавляет товар в корзину по имени"""
        button_id = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        add_button = (By.ID, button_id)

        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(add_button))
        button.click()

    def go_to_cart(self):
        """Переходит в корзину"""
        wait = WebDriverWait(self.driver, 10)

        cart_icon = wait.until(EC.element_to_be_clickable(self.cart_icon))
        wait.until(EC.presence_of_element_located(self.cart_badge))
        cart_icon.click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))