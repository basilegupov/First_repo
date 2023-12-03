# 1. Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою 
# по кожному розробнику компанії.
# 
# Приклад файлу:
# 
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.
# 
# Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.
# 
# Вимоги до завдання:
# 
# функція total_salary повертає значення типу float
# для читання файлу функція total_salary використовує лише метод readline
# ми поки що не використовуємо менеджер контексту with

def total_salary(path):
    result = 0.0
    file = open(path,'r')
    while True:
        line = file.readline()
        if not line:
            break
        ln = line.split(",")
        result += float(ln[1])
    file.close()
    return result
    
# 2. У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
# 
# ['Robert Stivenson,28', 'Alex Denver,30']
# Це список рядків із прізвищем та віком співробітника, розділеними комами.
# 
# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника 
# починалася з нового рядка.
# 
# Функція запису в файл write_employees_to_file(employee_list, path), де:
# 
# path – шлях до файлу.
# employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Вимоги:
# 
# запишіть вміст employee_list у файл, використовуючи режим "w".
# ми поки що не використовуємо менеджер контексту with
# кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19

def write_employees_to_file(employee_list, path):
    file = open(path,'w')
    for depart in employee_list:
        for employ in depart:
            file.write(employ+'\n')
    file.close()
    return
    