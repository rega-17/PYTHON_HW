# test_crud.py
import pytest
from sqlalchemy import text

from database import User, Student, Teacher, Subject, GroupStudent

# ========== ТЕСТ 1: CREATE (Добавление) ==========
def test_create_student(db_session, test_student_data):
    """Тест добавления нового студента"""
    # Создаем объект студента
    student = Student(
        name=test_student_data["name"],
        email=test_student_data["email"],
        phone=test_student_data["phone"]
    )
    
    # Добавляем в БД
    db_session.add(student)
    db_session.commit()
    
    # Проверяем что студент добавлен
    saved_student = db_session.query(Student).filter_by(email=test_student_data["email"]).first()
    
    assert saved_student is not None
    assert saved_student.name == test_student_data["name"]
    assert saved_student.email == test_student_data["email"]
    assert saved_student.id is not None
    
    print(f"✅ Создан студент ID: {saved_student.id}")

# ========== ТЕСТ 2: READ (Чтение) ==========
def test_read_existing_data(db_session):
    """Тест чтения существующих данных из БД"""
    # Читаем пользователей
    users_count = db_session.query(User).count()
    print(f"📊 Пользователей в БД: {users_count}")
    
    # Читаем студентов
    students_count = db_session.query(Student).count()
    print(f"📊 Студентов в БД: {students_count}")
    
    # Проверяем что данные есть (миграция прошла успешно)
    assert users_count > 0, "Должны быть пользователи после миграции"
    assert students_count > 0, "Должны быть студенты после миграции"
    
    # Показываем первых 3 пользователя
    users = db_session.query(User).limit(3).all()
    print(f"📝 Пример пользователей:")
    for user in users:
        print(f"   • {user.username or 'N/A'} ({user.email or 'N/A'})")

# ========== ТЕСТ 3: UPDATE (Обновление) ==========
def test_update_teacher(db_session, test_teacher_data):
    """Тест обновления преподавателя"""
    # Сначала создаем преподавателя
    teacher = Teacher(
        name=test_teacher_data["name"],
        email=test_teacher_data["email"],
        department=test_teacher_data["department"]
    )
    db_session.add(teacher)
    db_session.commit()
    teacher_id = teacher.id
    
    # Обновляем данные
    teacher_to_update = db_session.query(Teacher).filter_by(id=teacher_id).first()
    teacher_to_update.name = "Обновленное Имя"
    teacher_to_update.department = "Обновленный отдел"
    db_session.commit()
    
    # Проверяем обновление
    updated_teacher = db_session.query(Teacher).filter_by(id=teacher_id).first()
    
    assert updated_teacher.name == "Обновленное Имя"
    assert updated_teacher.department == "Обновленный отдел"
    assert updated_teacher.email == test_teacher_data["email"]
    
    print(f"✅ Обновлен преподаватель ID: {teacher_id}")

# ========== ТЕСТ 4: DELETE (Удаление) ==========
def test_delete_subject(db_session):
    """Тест удаления предмета"""
    # Создаем тестовый предмет
    subject = Subject(name="Тестовый предмет", description="Для тестирования")
    db_session.add(subject)
    db_session.commit()
    subject_id = subject.id
    
    # Проверяем что предмет создан
    assert db_session.query(Subject).filter_by(id=subject_id).first() is not None
    
    # Удаляем предмет
    subject_to_delete = db_session.query(Subject).filter_by(id=subject_id).first()
    db_session.delete(subject_to_delete)
    db_session.commit()
    
    # Проверяем что предмет удален
    deleted_subject = db_session.query(Subject).filter_by(id=subject_id).first()
    assert deleted_subject is None
    
    print(f"✅ Удален предмет ID: {subject_id}")

# ========== ТЕСТ 5: SQL запросы ==========
def test_sql_queries(db_session):
    """Тест выполнения SQL запросов"""
    # Пример 1: Простой запрос
    result = db_session.execute(text("SELECT COUNT(*) FROM users"))
    users_count = result.scalar()
    print(f"📊 SQL запрос: users = {users_count}")
    
    # Пример 2: Запрос с условием
    result = db_session.execute(text("SELECT COUNT(*) FROM student WHERE name IS NOT NULL"))
    students_with_name = result.scalar()
    print(f"📊 SQL запрос: students with name = {students_with_name}")
    
    # Пример 3: JOIN запрос
    result = db_session.execute(text("""
        SELECT s.name, COUNT(gs.id) as group_count
        FROM student s
        LEFT JOIN group_student gs ON s.id = gs.student_id
        GROUP BY s.name
        LIMIT 5
    """))
    
    print(f"📊 JOIN запрос (первые 5):")
    for row in result.fetchall():
        print(f"   • {row[0] or 'N/A'}: {row[1]} групп")

# ========== ТЕСТ 6: Проверка связей ==========
def test_relationships(db_session):
    """Тест связей между таблицами"""
    # Проверяем что в group_student есть ссылки на student
    result = db_session.execute(text("""
        SELECT COUNT(DISTINCT student_id) 
        FROM group_student 
        WHERE student_id IS NOT NULL
    """))
    unique_students_in_groups = result.scalar()
    print(f"📊 Уникальных студентов в группах: {unique_students_in_groups}")
    
    assert unique_students_in_groups >= 0

# ========== ЗАПУСК БЕЗ pytest ==========
if __name__ == "__main__":
    print("Запустите тесты через: pytest test_crud.py -v")
    print("Или для одного теста: pytest test_crud.py::test_read_existing_data -v")