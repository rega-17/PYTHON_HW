# database.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

# МОДЕЛИ НА ОСНОВЕ ВАШИХ ТАБЛИЦ:

class User(Base):
    """Модель пользователя (таблица users)"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    created_at = Column(DateTime)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

class Student(Base):
    """Модель студента (таблица student)"""
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    # Добавьте остальные поля на основе вашей таблицы
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

class Teacher(Base):
    """Модель преподавателя (таблица teacher)"""
    __tablename__ = 'teacher'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    department = Column(String(100))
    
    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}')>"

class Subject(Base):
    """Модель предмета (таблица subject)"""
    __tablename__ = 'subject'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(500))
    
    def __repr__(self):
        return f"<Subject(id={self.id}, name='{self.name}')>"

class GroupStudent(Base):
    """Модель группы студентов (таблица group_student)"""
    __tablename__ = 'group_student'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    group_id = Column(Integer)
    # Добавьте остальные поля
    
    student = relationship("Student")
    
    def __repr__(self):
        return f"<GroupStudent(id={self.id}, student_id={self.student_id})>"

# ФУНКЦИИ ДЛЯ РАБОТЫ С БАЗОЙ:
def get_engine():
    """Создать подключение к PostgreSQL"""
    return create_engine(
        "postgresql://postgres:SQL1@localhost:5432/mydatabase",
        echo=False  # поставьте True для отладки SQL запросов
    )

def get_session():
    """Получить сессию для работы с БД"""
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def create_tables():
    """Создать таблицы в БД (если не существуют)"""
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("✅ Таблицы созданы/проверены")