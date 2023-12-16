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
    
# 5. Ми маємо таку структуру файлу:
# 
# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
# Кожен запис складається з трьох частин і починається з нового рядка. Наприклад, для першого запису початок 60b90c1c13067a15887e1ae1 — це первинний ключ бази даних MongoDB. Він завжди містить 12 байтів або рівно 24 символи. Далі ми бачимо прізвисько кота Tayson та його вік 3. Всі частини запису розділені символом кома ,
# 
# Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:
# 
# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
# Параметри функції:
# 
# path - шлях до файлу
# Вимоги:
# 
# прочитайте вміст файлу за допомогою режиму "r".
# ми використовуємо менеджер контексту with
# поверніть із функції список котів із файлу у потрібному форматі

def get_cats_info(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split(',') for line in lines]
        for i in range(len(lines)):
            lines[i] = {"id":lines[i][0], "name": lines[i][1], "age": lines[i][2]}
    return lines


# 6. Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients, яка 
# приймала на вхід список з інгредієнтами рецепта.
# 
# Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт у файлі та 
# повертатиме знайдений рецепт у вигляді словника певної форми.
# 
# У вас є файл, який містить рецепти у вигляді:
# 
# 60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
# 60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
# 60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
# 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
# 60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
# Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.
# 
# Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника 
# для кожної страви що шукається. Створіть функцію get_recipe(path, search_id), яка повертатиме 
# словник для рецепта із зазначеним ідентифікатором MongoDB.
# 
# Де параметри функції:
# 
# path — шлях до файлу.
# search_id — первинний ключ MongoDB для пошуку рецепта
# Вимоги:
# 
# Використовуйте менеджер контексту with для читання з файлу
# Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
# Приклад: для файлу, вказаного вище, виклик функції у вигляді
# 
# get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
# Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:
# 
# {
#     "id": "60b90c3b13067a15887e1ae4",
#     "name": "Watermelon Cucumber Salad",
#     "ingredients": [
#         "1 large seedless watermelon",
#         "12 leaves fresh mint",
#         "1 cup crumbled feta cheese",
#     ],
# }

def get_recipe(path, search_id):
    with open(path, 'r') as file:
        rec=file.readline().strip().split(',')
        if rec[0]==search_id:
            return {
                "id":rec[0],
                "name":rec[1],
                "ingredients":[rec[i] for i in range(2,len(rec))]
            }


# 7. Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output 
# вміст текстового файлу source, очищений від цифр.
# 
# Вимоги:
# 
# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write

def sanitize_file(source, output):
    with open(source, 'r') as file_i:
        data = file_i.readlines()
        data = [line.replace('0', '').
                replace('1', '').
                replace('2', '').
                replace('3', '').
                replace('4', '').
                replace('5', '').
                replace('6', '').
                replace('7', '').
                replace('8', '').
                replace('9', '')
                 for line in data]
    print(data)
    with open(output, 'w') as file_o:
        for line in data:
            file_o.write(line)