# 📊 SQL Project (example_sql)

Проєкт для створення та заповнення бази даних SQLite з використанням Python та Poetry.

---

## ⚙️ Технології

- Python 3.11+
- Poetry (управління залежностями)
- SQLite
- Faker (генерація тестових даних)

---

## 🚀 1. Налаштування середовища

Створення та запуск проєкту через Poetry:

```bash
poetry init
poetry shell
poetry install --no-root
poetry env info
```    

---

## 🗄️ 2. Створення SQL структури

Файл:

salary.sql

📌 Призначення:

створення таблиць у базі даних
опис структури БД мовою SQL

---

## 🏗️ 3. Створення бази даних

Файл:

create_db.py

📌 Функціонал:

підключення до SQLite
виконання SQL скриптів
створення таблиць

💡 SQLite створює файл БД автоматично при першому підключенні.

---

## 📦 4. Наповнення бази даних

Файл:

fill_data.py

📌 Використовується:

```bash
pip install faker
poetry add faker
```

📌 Призначення:

генерація фейкових даних для заповнення таблиць:
компанії
співробітники
зарплати

---

## 🔍 5. Виконання SQL запитів

Файл:

select_first.py
select_second.py
select_third.py

📌 Призначення:

SELECT запити
JOIN таблиць
аналітика даних
перевірка результатів

---

## 📁 Структура проєкту
 
example_sql/
│
├── salary.sql
├── create_db.py
├── fill_data.py
├── pyproject.toml
├── poetry.lock
├── select_first.py
├── select_second.py
├── select_third.pyco
└── README.md