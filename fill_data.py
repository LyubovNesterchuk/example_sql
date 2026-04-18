from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_COMPANIES = 3
NUMBER_EMPLOYESS = 30
NUMBER_POST = 5

def generate_fake_data(number_companies, number_employees, number_post) -> tuple:
    fake_companies = []# тут зберігатимемо компанії
    fake_employees = []# тут зберігатимемо співробітників
    fake_posts = []# тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()

# Створимо набір компаній у кількості number_companies
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

# Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

# Та number_post набір посад
    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts



companies, employees, posts = generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST)
print(companies) #['Mitchell-Richardson', 'Baird LLC', 'Smith Inc']
print(employees) #['Harold Pacheco', 'Melissa Brown', 'Jennifer Long', 'Lisa Leonard', 'Roy Richardson', 'Diana Dillon', 'Ryan Vang', 'Steven Frank', 'Melissa Preston', 'Jacob Robinson', 'Larry Brown', 'Travis Cole', 'Amber Graham', 'Christopher Gonzalez', 'Anthony Hoover', 'Michael Peterson', 'Roberta Dougherty', 'Shawn Gregory', 'Mariah Gardner', 'Thomas Guerrero', 'Debra Brown', 'Ryan Adams', 'Matthew Castillo', 'Rachel Fletcher', 'Melissa Payne', 'Angela Guerrero', 'Janet Richard', 'Tanya Young', 'Robert Dixon', 'Vincent Kennedy']
print(posts) #['Psychotherapist', 'Horticulturist, amenity', 'Ophthalmologist', 'Television/film/video producer', 'Research scientist (maths)']

'''дані випадкові і змінюватимуться при кожному виконанні функції.'''



'''Для виконання скрипту на множинне вставлення даних у таблицю нам знадобиться список 
кортежів, отже, необхідно підготувати такі дані для кожної з таблиць.'''

def prepare_data(companies, employees, posts) -> tuple:

    for_companies = []
    for company in companies:# Готуємо список кортежів назв компаній
        for_companies.append((company, ))

    for_employees = []# для таблиці employees
    for emp in employees:
        '''
        Для записів у таблицю співробітників нам потрібно додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число, збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    '''
    Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Діапазон зарплат генеруватимемо від 1000 до 10000 у.о.
    для кожного місяця та кожного співробітника.
    12 місяців × N співробітників
    '''
    for_payments = []
    for month in range(1, 12 + 1):# Виконуємо цикл за місяцями
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_EMPLOYESS + 1):# Виконуємо цикл за кількістю співробітників
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments

companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST))
print(companies)
print(employees)
print(posts)
'''
[('Small, Lee and Hoover',), ('Hernandez-Mercado',), ('Clark-Garcia',)]
[('Nicole Jones', 'Designer, ceramics/pottery', 2), ('Yolanda Mitchell', 'Theatre stage manager', 1), ('Robert Oliver', 'Theatre stage manager', 1), ('Mary Fernandez', 'Theatre stage manager', 3), ('Justin Richard', 'Occupational therapist', 3), ('Kevin Glover', 'Occupational therapist', 1), ('Jonathan Gonzalez Jr.', 'Occupational therapist', 1), ('Nathan Franklin', 'Personal assistant', 1), ('William Walsh', 'Theatre stage manager', 2), ('Scott Fowler', 'Designer, ceramics/pottery', 1), ('Cynthia Robinson', 'Administrator, local government', 3), ('Michael Cole', 'Personal assistant', 1), ('Linda Davis', 'Designer, ceramics/pottery', 1), ('Michael Gates', 'Administrator, local government', 3), ('Karen Williams DVM', 'Personal assistant', 3), ('Victor Watts', 'Administrator, local government', 2), ('Jacob Tucker', 'Theatre stage manager', 3), ('Miranda Lambert', 'Personal assistant', 1), ('Joyce Mason', 'Personal assistant', 2), ('Rachel Lopez', 'Personal assistant', 3), ('Jennifer Dennis', 'Theatre stage manager', 3), ('Patricia Guerrero', 'Administrator, local government', 2), ('Ashley Collins', 'Theatre stage manager', 3), ('Samantha Norris', 'Designer, ceramics/pottery', 2), ('Aaron Gomez', 'Personal assistant', 2), ('Dr. Matthew Schultz', 'Occupational therapist', 1), ('David Arellano', 'Personal assistant', 1), ('Matthew Austin', 'Theatre stage manager', 1), ('Carrie Pitts', 'Occupational therapist', 3), ('Melissa Mckenzie', 'Administrator, local government', 3)]
[(1, datetime.date(2021, 1, 18), 4847), (2, datetime.date(2021, 1, 18), 5553), (3, datetime.date(2021, 1, 18), 9511), ...]
'''


def insert_data_to_db(companies, employees, payments) -> None:
# Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, 
        помітимо знаком заповнювача (?) '''

        sql_to_companies = """INSERT INTO companies(company_name)
                               VALUES (?)"""

        '''Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипту, а другим - дані (список кортежів).'''

        cur.executemany(sql_to_companies, companies)

# Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_employees = """INSERT INTO employees(employee, post, company_id)
                               VALUES (?, ?, ?)"""

# Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_employees, employees)

# Останньою заповнюємо таблицю із зарплатами

        sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
                              VALUES (?, ?, ?)"""

# Вставляємо дані про зарплати

        cur.executemany(sql_to_payments, payments)

# Фіксуємо наші зміни в БД

        con.commit()

if __name__ == "__main__":
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST))
    insert_data_to_db(companies, employees, posts)


'''
Після виконання скрипту БД буде заповнена фейковими даними, з якими ми можемо вже працювати та створювати запити.
'''