



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
