from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shopping_cart_total():
    # Инициализация Firefox
    driver = webdriver.Firefox()

    try:
        # Шаг 1: Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Ожидание загрузки страницы
        wait = WebDriverWait(driver, 10)

        # Шаг 2: Авторизоваться как пользователь standard_user
        username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username_input.send_keys("standard_user")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Ожидание загрузки страницы товаров
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Шаг 3: Добавить в корзину товары
        # Sauce Labs Backpack
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()

        # Sauce Labs Bolt T-Shirt
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()

        # Sauce Labs Onesie
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()

        # Шаг 4: Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Ожидание загрузки корзины
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))

        # Шаг 5: Нажать Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Ожидание загрузки формы checkout
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        # Шаг 6: Заполнить форму своими данными
        first_name_input = driver.find_element(By.ID, "first-name")
        first_name_input.send_keys("Иван")

        last_name_input = driver.find_element(By.ID, "last-name")
        last_name_input.send_keys("Петров")

        postal_code_input = driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys("123456")

        # Шаг 7: Нажать кнопку Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Ожидание загрузки страницы с итоговой стоимостью
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))

        # Шаг 8: Прочитать итоговую стоимость (Total)
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text

        # Шаг 9: Проверить, что итоговая сумма равна $58.29
        assert total_text == "Total: $58.29", f"Ожидалась сумма 'Total: $58.29', но получили '{total_text}'"

    finally:
        # Шаг 10: Закрыть браузер
        driver.quit()