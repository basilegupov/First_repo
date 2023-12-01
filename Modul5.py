



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