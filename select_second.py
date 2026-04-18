import sqlite3

# Вибірка: кількість співробітників за компаніями

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT COUNT(*), c.company_name
FROM employees e
LEFT JOIN companies c ON e.company_id = c.id
GROUP BY c.id;
"""

print(execute_query(sql))

'''[(10, 'Reeves-Weaver'), (13, 'Green, Lowery and Arellano'), 
(7, 'Hines, Johnson and Cook')]'''



'''Тут використовуємо функцію COUNT для підрахунку кількості рядків, 
головне — це з'єднати таблиці companies та employees за ключами id та company_id, 
а потім виконати групування за полем id або company_name таблиці companies. 
У нашому випадку ми виконали групування за полем id.'''