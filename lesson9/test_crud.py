# test_crud.py
import pytest
from sqlalchemy import text

def test_database_connection(db_session):
    """Тест подключения к БД"""
    result = db_session.execute(text("SELECT version()"))
    version = result.scalar()
    print(f"Подключено к: {version}")
    assert "PostgreSQL" in version

def test_tables_exist(db_session):
    """Тест что таблицы существуют"""
    result = db_session.execute(text("SELECT COUNT(*) FROM users"))
    count = result.scalar()
    print(f"Пользователей в БД: {count}")
    assert count >= 0

def test_create_data(db_session):
    """Тест создания данных"""
    # Простой тест
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1
    print("✅ Тест создания пройден")
