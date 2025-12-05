import allure
import pytest


@allure.feature("Базовые тесты")
@allure.story("Проверка Allure разметки")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка математических операций")
@allure.description("Простой тест для проверки работы Allure отчетов")
def test_addition():
    """Тест сложения"""
    with allure.step("Шаг 1: Проверить сложение простых чисел"):
        result = 1 + 1
        with allure.step(f"Результат: 1 + 1 = {result}"):
            assert result == 2
    
    with allure.step("Шаг 2: Проверить сложение отрицательных чисел"):
        result = -5 + 10
        with allure.step(f"Результат: -5 + 10 = {result}"):
            assert result == 5


@allure.feature("Базовые тесты")
@allure.story("Работа со строками")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Проверка строковых операций")
@allure.description("Тестирование операций со строками")
def test_string_operations():
    """Тест строковых операций"""
    text = "Hello World"
    
    with allure.step(f"Проверить строку: '{text}'"):
        with allure.step("Проверить наличие подстроки 'Hello'"):
            assert "Hello" in text
        
        with allure.step("Проверить длину строки"):
            assert len(text) == 11
        
        with allure.step("Проверить преобразование в верхний регистр"):
            upper_text = text.upper()
            assert upper_text == "HELLO WORLD"


@allure.feature("Базовые тесты")
@allure.story("Проверка структур данных")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Проверка списков и словарей")
@allure.description("Тестирование операций со списками и словарями")
def test_data_structures():
    """Тест структур данных"""
    with allure.step("Работа со списками"):
        numbers = [1, 2, 3, 4, 5]
        
        with allure.step(f"Проверить список: {numbers}"):
            with allure.step("Проверить длину списка"):
                assert len(numbers) == 5
            
            with allure.step("Проверить наличие элемента 3"):
                assert 3 in numbers
            
            with allure.step("Проверить сумму элементов"):
                total = sum(numbers)
                assert total == 15