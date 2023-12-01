# 1.У Харкові відкривають у бомбосховищі школу для молодших школярів. 
# Треба  обладнати три кімнати партами. Парта  - на дві людини. 
# Програмі подається на вхід три числа (трьома input)  - кількість учнів в кожному класі. 
# Програма має порахувати необхідну кількість парт загалом.
# 20 21 22  -> 32
# 26 20 16 -> 31
# 25 21 23 -> 36
# 17 19 18 -> 28

# def desks(*klass):
#     result=0
#     for kl in klass:
#         result += (kl-1)//2+1 
#     return result


# print(desks(20,21,22,11))
# print(desks(26,20,16))
# print(desks(25,21,23))
# print(desks(17,19,18))

# З початку доби пройшло n хвилин. Програма приймає це число input-ом.
# Який час буде показувати електроне табло годинника ?
# Програма має вивести два числа - години (від 0 до 23), та хвилини (від 0 до 59).
# 150 -> 2 30
# 1441 -> 0 1
# 444 -> 7 24
# 180 -> 3 0
# 1439 -> 23 59
# 1400 -> 0 0

# def current_time(minuts):
#     minuts = minuts % 1440
#     h = minuts // 60
#     m = minuts % 60
#     return h, m


# print(current_time(150))
# print(current_time(1441))
# print(current_time(444))
# print(current_time(180))
# print(current_time(1439))
# print(current_time(1440))

# Качка плаває в прямокутному пруду розміром n на m метрів.
# Це розумна, бойова українська качка.
# Вона знає, що під час тревоги треба якнайшвидше дістатись берега і сховатись у кущах.
# Коли залунала сирена вона одразу визначила, що до найдовшої сторони пруда їй плисти x метрів,
# а до короткої сторони пруда - y  метрів.
# Визначте її найкоротший шлях до берега.
# Для цієї задачі викорустуйте функції max, min.
# 23 52 8 43 -> 8
# 18 90 3 63 -> 3
# 73 63 56 8 -> 7

# def min_dist(n, m, x, y):
#     if n < m:
#         return min(n-x, m-y, x, y)
#     else:
#         return min(m-x, n-y, x, y)


# print(min_dist(23, 52, 8, 43))
# print(min_dist(18, 90, 3, 63))
# print(min_dist(73, 63, 56, 8))

# У Джо Палуки товсті пальці, тому він завжди натискає клавішу "Caps Lock", коли насправді має намір натиснути клавішу "a". 
# (Коли Джо намагається ввести якусь акцентовану версію "a", яка потребує більше натискань клавіш для створення акцентів,
# він більш обережний у присутності таких рафінованих символів ([Shift] + [a]) і буде натискати клавіші правильно).
# Обчисліть і виведіть результат введення Джо заданого тексту. Клавіша "Caps Lock" впливає лише на клавіші з літерами 
# від "a" до "z", і не впливає на інші клавіші або символи. вважається, що клавіша "Caps Lock" спочатку вимкнена.
# Для клавіатури Джо, клавіша Caps Lock завжди є великою літерою. Це означає, що якщо клавіша Caps Lock увімкнена,
# а Джо натискає Shift + b - він отримає "B" (у верхньому регістрі).
# Вхідні дані: Рядок (str). Введений текст.
# Виводиться на екран: Рядок (str). Виводиться текст після введення.
# Приклади:
# "Why are you asking me that?" --> "Why RE YOU sking me thT?"
# "Always wanted to visit Zambia." --> "AlwYS Wnted to visit ZMBI."
# "Aloha from Hawaii" -->  "Aloh FROM HwII"

def bad_input_a(string_a):
    string_b = string_a.split('a')
    st=''
    for i in range(len(string_b)):
        if i%2:
            st += string_b[i].upper()
        else:
            st += string_b[i]
    return st

print(bad_input_a("Why are you asking me that?"))
print(bad_input_a("Always wanted to visit Zambia."))
print(bad_input_a("Aloha from Hawaii"))


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def decode(message):
    de_morse=''
    words=message.split('   ')
    for i in range(len(words)):
        words[i]=words[i].split(' ')
    #print(words)
    i = 0
    for word in words:
        for ch in word:
            # print(list(MORSE_CODE_DICT.keys()))
            # print(list(MORSE_CODE_DICT.values()).index(ch))
            de_morse += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(ch)].lower()
        # if not i:
        #     de_morse=de_morse.title()
        i += 1
        de_morse=de_morse.capitalize()
        if i < len(words):
            de_morse += ' '
        
    return de_morse

def encrypt(message):
    cipher = ''
    for letter in range(len(message)):
        if message[letter] != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[message[letter].upper()] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '*2
 
    return cipher.strip()




grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    global grades
    result = []
    i = 0
    for student in students:
        result.append(
            '{:>4}|{:<10}|{:^5}|{:^5}'
                .format(i+1,
                        student, 
                        students.get(student), 
                        grades.get(students.get(student))
                        )
                    )
        i +=1
    return result


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}    
for el in formatted_grades(students):
    print(el)


def seasons(mo):
    SEASON = ['ЗИМА','ВЕСНА','ЛЕТО','ОСЕНЬ']
    return SEASON[(mo//3+4)%4]

for i in range(1,25):
    print(i, seasons(i))

def main():
    print(f"Decode text:{decode('... --- -- .   - . -..- -')}.")
    print(f"Decode text:{decode('..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----')}.")
    print(f"Encript string:{encrypt('It is a simple test')}|")
    print(decode(encrypt('It is a simple test')))

if __name__ == '__main__':
    main()
# всі стовпці мають ширину 10 символів
# у заголовків таблиці вирівнювання по центру
# перший стовпець десяткових чисел — вирівнювання по лівому краю
# другий стовпець шістнадцяткових чисел — вирівнювання по центру
# третій стовпець двійкових чисел — вирівнювання з правого краю
# вертикальний символ | не входить у ширину стовпця


def formatted_numbers():
    result=['|{:^10}|{:^10}|{:^10}|'.format('decimal','hex','binary')]
    for i in range(16):
        result.append('|{:<10d}|{:^10x}|{:>10b}|'.format( i, i, i))
    return result
    
    
for el in formatted_numbers():
    print(el) 


def eratosthenes(num):
    
    A = list(range(2,num+1))
    for i in A:
        if i != 0:
            for j in range(2*i,num+1,i):
                A[j-2] = 0
                print(i,j, A)
    for i in range(len(A)):
        if 0 not in A:
            break
        A.pop(A.index(0))

    return num in A, A

print(eratosthenes(127))