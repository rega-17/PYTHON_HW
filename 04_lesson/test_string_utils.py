import pytest
from string_utils import StringUtils

# Инициализация утилиты
string_utils = StringUtils()

# Тесты для функции trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("   python", "python"),
    ("test", "test"),  # строка без пробелов
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),  # пустая строка
    ("   ", ""),  # строка только с пробелами
    ("skypro   ", "skypro   "),  # пробелы в конце (не должны удаляться)
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для функции contains()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("Hello World", " ", True),  # пробел как символ
    ("123abc", "2", True),  # цифра как символ
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),  # пустая строка
    ("   ", "a", False),  # строка с пробелами
    ("SkyPro", "", False),  # пустой символ для поиска
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# Тесты для функции delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),  # удаление пробела
    ("04 апреля 2023", "апреля ", "04 2023"),  # строка с пробелами и датой
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # символ отсутствует
    ("", "a", ""),  # пустая строка
    ("   ", " ", ""),  # удаление всех пробелов
    ("Test", "", "Test"),  # пустой символ для удаления
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected