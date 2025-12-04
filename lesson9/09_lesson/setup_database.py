# setup_database.py
# Этот скрипт сам создаст базу и выполнит миграцию

import subprocess
import sys
import os

def run_psql_command(command):
    """Выполнить команду psql"""
    try:
        # Устанавливаем пароль как переменную окружения
        env = os.environ.copy()
        env['PGPASSWORD'] = 'SQL1'
        
        result = subprocess.run(
            ['psql', '-U', 'postgres', '-c', command],
            env=env,
            capture_output=True,
            text=True,
            shell=True
        )
        
        if result.returncode == 0:
            print(f"✅ Успешно: {command}")
            return True
        else:
            print(f"❌ Ошибка: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ Команда psql не найдена. Установите PostgreSQL.")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    print("=" * 60)
    print("НАСТРОЙКА БАЗЫ ДАННЫХ POSTGRESQL")
    print("=" * 60)
    
    print(f"\n🔑 Используемый пароль: SQL1")
    print(f"👤 Пользователь: postgres")
    print(f"📁 База данных: mydatabase")
    print()
    
    # 1. Проверяем подключение к PostgreSQL
    print("1. Проверяем подключение к PostgreSQL...")
    if not run_psql_command("SELECT 1;"):
        print("\n💡 PostgreSQL не отвечает. Проверьте:")
        print("   • Установлен ли PostgreSQL")
        print("   • Запущена ли служба PostgreSQL")
        print("   • Правильный ли пароль")
        return
    
    # 2. Создаем базу данных
    print("\n2. Создаем базу данных 'mydatabase'...")
    run_psql_command("DROP DATABASE IF EXISTS mydatabase;")
    if run_psql_command("CREATE DATABASE mydatabase;"):
        print("   ✅ База 'mydatabase' создана")
    else:
        print("   ⚠️ Проблема при создании базы")
    
    # 3. Проверяем создание
    print("\n3. Проверяем создание базы...")
    run_psql_command("\\l mydatabase")
    
    print("\n" + "=" * 60)
    print("✅ НАСТРОЙКА ЗАВЕРШЕНА!")
    print("=" * 60)
    print("\n🎯 Теперь запустите миграцию:")
    print("   python migrate_ready.py")

if __name__ == "__main__":
    main()