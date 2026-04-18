import sqlite3

#  Вибір співробітників компаній, у яких у 7 місяців була зарплата > 5000

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT c.company_name, e.employee, e.post, p.total
FROM companies c
    LEFT JOIN employees e ON e.company_id = c.id
    LEFT JOIN payments p ON p.employee_id = e.id
WHERE p.total > 5000
    AND  p.date_of BETWEEN  '2021-07-10' AND  '2021-07-20'
"""

print(execute_query(sql))

'''[('Smith-Sweeney', 'David Wallace', 'Art therapist', 8349), 
('Smith-Sweeney', 'Jason Griffin', 'Special effects artist', 6236),
 ('Smith-Sweeney', 'Jason Griffin', 'Special effects artist', 6201), 
 ('Smith-Sweeney', 'Jennifer Thomas', 'Investment banker, operational', 6295)...]'''



'''необхідно послідовно з'єднати таблиці між собою. Знайти всі записи, 
де виплати були більшими за 5000, і час виплат повинен бути між датами 
'2021-07-10' та '2021-07-20'.'''