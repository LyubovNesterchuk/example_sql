import sqlite3

# Знаходження середньої зарплати за посадами

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT ROUND(AVG(p.total), 2), e.post
FROM payments as p
LEFT JOIN employees as e ON p.employee_id = e.id
GROUP BY e.post;
"""

print(execute_query(sql))


'''[(5295.17, 'Art therapist'), (5225.45, 'Energy engineer'), 
(5552.33, 'International aid/development worker'), 
(5536.16, 'Investment banker, operational'), (5800.54, 'Special effects artist')]'''


'''Ми робимо запит до таблиці payments, приєднуємо таблицю employees, щоб при цьому 
збігалися поля employee_id з таблиці payments та id з таблиці employees.
Середнє значення знаходимо за полем total таблиці payments та округляємо його 
до двох знаків після коми.
Виконали групування за полем post, щоб запит точно розумів процес обчислення 
середнього значення до кожної посади.'''