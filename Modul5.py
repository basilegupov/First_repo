# 6. Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію заборонених слів у повідомленні.
# 
# Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст заборонених 
# слів зі списку (параметр spam_words), і повертає результат перевірки: True, якщо є хоч одне 
# слово присутнє зі списку, та False, якщо в тексті стоп-слів не виявлено.
# 
# Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words, при 
# пошуку заборонених слів, регістру незалежна і весь текст має зводитися до нижнього регістру. Для 
# спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.
# 
# Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False. Він 
# відповідатиме за те, що функція шукатиме окреме слово чи ні. Слово вважати, що стоїть окремо, 
# якщо ліворуч від слова знаходиться символ пробілу або воно розташоване на початку тексту, а 
# праворуч від слова знаходиться пробіл або символ крапки.
# 
# Наприклад, у тексті ми шукаємо слово "лоток". То в слові "молоток" виклик та результат буде наступним:
# 
# print(is_spam_words("У діда в руках молоток.", ["лоток"]))  # True
# print(is_spam_words("У діда в руках молоток.", ["лоток"], True))  # False
# Тобто у другому випадку слово не окреме і є частиною іншого.
# 
# У цьому прикладі функція поверне True в обох випадках.
# 
# print(is_spam_words("У кота порожній лоток.", ["лоток"]))  # True
# print(is_spam_words("У кота порожній лоток.", ["лоток"], True))  # True

def is_spam_words(text, spam_words, space_around=False):
    result = False
    if space_around:
        text_new = text.replace('.', ' ').split()
        for s_word in spam_words:
            for t_word in text_new:
                if s_word.lower() == t_word.lower():
                    result = True
    else:
        for s_word in spam_words:
            if text.lower().find(s_word.lower()) >= 0:
                result = True
    return result

# 7. Ви вже навчилися працювати з рядками глибше і тепер у вас є повний набір інструментів для 
# обробки рядків за допомогою Python.
# 
# За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для 
# транслітерації. Створюйте словник TRANS поза функцією translate
# 
# Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.
# 
# Функція translate:
# 
# приймає на вхід рядок та повертає рядок;
# проводить транслітерацію кириличних символів на латиницю;
# Приклад виконання:
# 
# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
# Примітка: У задачі, при створенні словника TRANS, код TRANS[ord(c.upper())] = l.title() буде 
# вважатися неправильним, а TRANS[ord(c.upper())] = l.upper() — правильним. Це компроміс, тому 
# що в першому випадку ми враховуємо великі літери, а в другому — правильно, якщо ім'я буде все 
# великими літерами. Щоб не ускладнювати завдання, прийнято як у документах — все ім'я друкується великими.

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", 
               "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def translate(name):
    name = name.translate(TRANS)
    return name


# 8. У минулому модулі ми працювали із системою оцінок ECTS. Напишіть функцію formatted_grades, 
# яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:
# 
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# І повертає список відформатованих рядків, щоб під час виведення наступного коду:
# 
# for el in formatted_grades(students):
#     print(el)
# Виходила наступна таблиця:
# 
#    1|Nick      |  A  |  5
#    2|Olga      |  B  |  5
#    3|Mike      | FX  |  2
#    4|Anna      |  C  |  4
# перший стовпець — ширина 4 символи, вирівнювання по правому краю
# другий стовпець — ширина 10 символів, вирівнювання по лівому краю
# третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
# вертикальний символ | не входить у ширину стовпця


grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    result = []
    i = 1
    for student, grade in students.items():
        result.append(
            '{:>4}|{:<10}|{:^5}|{:^5}'
                .format(i,
                        student, 
                        grade, 
                        grades.get(grade)
                        )
                    )
        i +=1
    return result
        
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}    
for el in formatted_grades(students):
    print(el)



# 10. Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. Функція виконує пошук 
# зазначеного слова word у тексті text за допомогою функції search та повертає словник.
# 
# При виклику функції:
# 
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
# Результат має бути наступного виду при збігу:
# 
# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }
# де
# 
# result — результат пошуку True або False
# first_index — початкова позиція збігу
# last_index — кінцева позиція збігу
# search_string — частина рядка, в якому був збіг
# string — рядок, переданий у функцію
# Якщо збігів не виявлено:
# 
# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "python"))
# Результат:
# 
# {
#     'result': False,
#     'first_index': None,
#     'last_index': None,
#     'search_string': 'python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }

import re


def find_word(text, word):
    res = {}
    found =  re.search(word, text)
    if found:
        res['result']=True
        res['first_index'] = found.start()
        res['last_index'] = found.end()
        res['search_string'] = found[0]
        res['string'] = text
    else:
        res['result']=False
        res['first_index'] = None
        res['last_index'] = None
        res['search_string'] = word
        res['string'] = text
        
    return res
            
            
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))            

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python")) 

# 11. Для закріплення матеріалу напишіть функцію find_all_words, яка шукає збіг слова в тексті. Функція повертає 
# список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого написання, тобто, наприклад, можливі 
# варіанти написання слова "Python" як pYthoN, pythOn, PYTHOn і т.і. головне, щоб зберігався порядок слів, регістр 
# не має значення.
# 
# Підказка: функції модуля re приймають ще ключовий параметр flags і ми можемо визначити нечутливість до регістру, 
# надавши йому значення re.IGNORECASE        

import re


def find_all_words(text, word):

    return re.findall(word, text, re.IGNORECASE)


print(find_all_words(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))            

print(find_all_words(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python")) 


# 12. У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті 
# повідомлення. Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів 
# на деякий шаблон. Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію 
# replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі 
# списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, 
# підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити 
# нечутливість до регістру стоп-слів.

import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word,'*'*len(word), text, flags= re.I)
    
    return text  


# 13. Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції 
# find_all_emails, яка буде в тексті (параметр text) знаходити всі email та повертати список 
# отриманих з тексту збігів.
# 
# З метою спрощення приймемо, що:
# 
# ми використовуємо для email, — англійський алфавіт
#  - префікс (все, що знаходиться до символу @) починається з латинської літери та може містити 
# будь-яке число або букву, включаючи нижнє підкреслення та символ точки. Має складатися мінімум 
# із двох символів
#  - суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, 
# та має дві частини, розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два 
# символи (все, що після точки)
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.
# 
# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок 
# регулярних виразів regex101.

import re


def find_all_emails(text):
    
    result = re.findall(r"([A-Za-z]{1}[-0-9A-z\.]{1,}@+([A-z]{1,}\.)+[A-z]{2,})", text)
    return result

print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o \
                      1Fool@iana.org first_last@iana.org \
                      first.middle.last@iana.or \
                      a@test.com abc111@test.com.net'))

# ^([A-z]{1}[-0-9A-z\.]{0,}[0-9A-z]{1})@([A-z]{1,}\.)+[-A-z]{2,}$

# 14. Завдання буде схоже на попереднє, але тепер у тексті ми шукатимемо номер телефону України 
# в міжнародному форматі, шаблон якого наступний: +380(67)777-7-777 або +380(67)777-77-77
# 
# Напишіть регулярний вираз для функції find_all_phones, яка буде в тексті (параметр text) знаходити 
# всі телефонні номери за вказаним шаблоном та повертати список отриманих з тексту збігів.

# З метою спрощення приймемо, що:

# використовуємо тільки цифри та символи +, (, ) та -
# телефонний номер починається із символу +
# шаблон телефону символ + потім три цифри 380, символ (, дві цифри, символ ), три цифри, символ -, 
# одна або дві цифри, символ -, дві чи три цифри
# Довжина шаблону телефонного номера завжди 17 символів
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів телефонних номерів.

# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних 
# виразів regex101.

import re


def find_all_phones(text):
    result = re.findall(r"\+380\([0-9]{2}\)[0-9]{3}[-0-9]{4}[0-9]{2}", text)
    return result

# 15. І останнє завдання на регулярні висловлювання — це пошук у тексті гіперпосилань.
# 
# Напишіть регулярний вираз для функції find_all_links, яка буде в тексті (параметр text) 
# знаходити всі лінки та повертати список отриманих з тексту збігів.
# 
# З метою спрощення приймемо, що:
# 
# Початок гіперпосилання може бути http:// або https://
# доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
# символи точок . не можуть зустрічатися поруч
# Фактично в навчальному прикладі ми шукатимемо прості url адреси:

# https://www.google.com
# https://www.facebook.com
# https://github.com
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів гіперпосилань.

# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок 
# регулярних виразів regex101.

import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"http[s]{0,1}:[\/]{2}(\w{1,}\.){1,}\w{1,}", text)
    
    for match in iterator:
        result.append(match.group())
    return result


print(find_all_links('The main search site in the world is https://www.google.com \
                     The main social network for people in the world is https://www.facebook.com \
                     But programmers have their own social network http://github.com \
                     There they share their code. some url to check https://www..facebook.com www.facebook.com '))
