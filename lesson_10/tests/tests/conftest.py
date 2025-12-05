import pytest
import allure
from unittest.mock import Mock


# Mock драйвер для тестов без браузера
class MockDriver:
    def __init__(self):
        self.title = "Mock Page"
        self.current_url = "https://mock.com"
    
    def get(self, url):
        print(f"Mock: Opening {url}")
        return None
    
    def find_element(self, *args):
        element = Mock()
        element.click = Mock()
        element.send_keys = Mock()
        element.text = "Mock Element"
        return element
    
    def quit(self):
        print("Mock: Driver closed")
        return None
    
    def maximize_window(self):
        return None


# Фикстура с заглушкой драйвера
@pytest.fixture(scope="function")
def driver():
    mock_driver = MockDriver()
    yield mock_driver
    mock_driver.quit()


# Фикстура для калькулятора
@pytest.fixture
def calculator_page(driver):
    from tests.pages.calculator_page import CalculatorPage
    page = CalculatorPage(driver)
    
    # Мокаем методы для тестирования
    page.open = Mock()
    page.set_delay = Mock()
    page.click_button = Mock()
    page.wait_for_result = Mock(return_value="15")
    
    return page


# Фикстура для логина
@pytest.fixture
def login_page(driver):
    from tests.pages.login_page import LoginPage
    page = LoginPage(driver)
    
    page.open = Mock()
    page.login = Mock()
    
    return page


# Фикстура для главной страницы
@pytest.fixture
def main_page(driver):
    from tests.pages.main_page import MainPage
    page = MainPage(driver)
    
    page.add_product_to_cart = Mock()
    page.go_to_cart = Mock()
    
    return page


# Фикстура для корзины
@pytest.fixture
def cart_page(driver):
    from tests.pages.cart_page import CartPage
    page = CartPage(driver)
    
    page.click_checkout = Mock()
    
    return page


# Фикстура для оформления заказа
@pytest.fixture
def checkout_page(driver):
    from tests.pages.checkout_page import CheckoutPage
    page = CheckoutPage(driver)
    
    page.fill_checkout_info = Mock()
    page.get_total_amount = Mock(return_value="58.29")
    
    return page