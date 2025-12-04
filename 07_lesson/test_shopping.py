from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shopping_flow():
    driver = webdriver.Chrome()

    try:
        # Создаем объекты страниц
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Шаг 1: Открыть сайт и авторизоваться
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Шаг 2: Добавить товары в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product in products_to_add:
            main_page.add_product_to_cart(product)

        # Шаг 3: Перейти в корзину и нажать Checkout
        main_page.go_to_cart()
        cart_page.click_checkout()

        # Шаг 4: Заполнить форму оформления заказа
        checkout_page.fill_checkout_info("Иван", "Петров", "123456")

        # Шаг 5: Проверить итоговую стоимость
        total_amount = checkout_page.get_total_amount()
        assert total_amount == "58.29", f"Ожидалась сумма 58.29, но получена {total_amount}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_flow()