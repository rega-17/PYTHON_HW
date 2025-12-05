# tests/test_suites/test_calculator.py
import allure


@allure.feature("Калькулятор")
@allure.story("Мок-тест")
@allure.title("Тест калькулятора без фикстур")
def test_calculator_simple():
    """Простой тест без фикстур"""
    with allure.step("Проверка логики калькулятора"):
        assert 7 + 8 == 15
    
    with allure.step("Проверка результата"):
        result = 15
        assert result == 15


@allure.feature("Калькулятор")
@allure.story("Дополнительные проверки")
@allure.title("Проверка математики")
def test_calculator_math():
    with allure.step("Сложение"):
        assert 1 + 1 == 2
    
    with allure.step("Умножение"):
        assert 3 * 3 == 9
    
    with allure.step("Комбинированные операции"):
        assert (2 + 3) * 4 == 20