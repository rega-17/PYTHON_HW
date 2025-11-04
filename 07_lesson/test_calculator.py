from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator_with_delay():
    driver = webdriver.Chrome()  # Можно заменить на webdriver.Firefox() или webdriver.Edge()

    try:
        calculator_page = CalculatorPage(driver)

        calculator_page.open()
        calculator_page.set_delay(45)

        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

        result = calculator_page.wait_for_result("15", timeout=50)
        assert result == "15", f"Ожидался результат 15, но получен {result}"

        print("Тест пройден успешно! Результат: 15")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator_with_delay()