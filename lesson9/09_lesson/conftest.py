# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base

# Строка подключения для тестов
TEST_DATABASE_URL = "postgresql://postgres:SQL1@localhost:5432/mydatabase"

@pytest.fixture(scope="function")
def db_session():
    """Создать сессию БД для каждого теста"""
    # Создаем движок
    engine = create_engine(
        TEST_DATABASE_URL,
        poolclass=StaticPool,
        echo=False
    )
    
    # Создаем таблицы (если не существуют)
    Base.metadata.create_all(engine)
    
    # Создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Отдаем сессию тесту
    yield session
    
    # После теста - очистка
    session.rollback()
    
    # Удаляем данные из всех таблиц
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    
    session.commit()
    session.close()

@pytest.fixture
def test_user_data():
    """Тестовые данные для пользователя"""
    return {
        "username": "test_user",
        "email": "test@example.com",
        "password": "test123"
    }

@pytest.fixture
def test_student_data():
    """Тестовые данные для студента"""
    return {
        "name": "Тестовый Студент",
        "email": "student@test.com",
        "phone": "+79990001122"
    }

@pytest.fixture
def test_teacher_data():
    """Тестовые данные для преподавателя"""
    return {
        "name": "Тестовый Преподаватель",
        "email": "teacher@test.com",
        "department": "Информатика"
    }