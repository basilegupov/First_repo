def create_deck():
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = list()
    for suit in suits:
        for value in values:
            deck.append(f"{value}{suit}")
    return deck

from random import randrange

def shuffle_deck(deck):
    # new_deck = deck.copy()
    # for i in range(0, len(deck)):
    #     other_index = randrange(0, len(new_deck))
    #     new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
    # return new_deck
    
    for i in range(0, len(deck)):
        other_index = randrange(0, len(deck))
        deck[i], deck[other_index] = deck[other_index], deck[i]

    return deck
    

def deal(players, cards, deck):
    if players * cards > len(deck):
        return deck

    table = list()

    for _ in range(0, cards):
        for player in range(players):
            if player >= len(table):
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())
    return table

def main(players, cards):
    init_deck = create_deck()
    print(f"Open new deck: {init_deck}")

    deck = shuffle_deck(init_deck)
    print(f"Shuffle deck: {deck}")

    print(f"Invite {players} players to table")
    print(f"Give {cards} cards to each players")

    table = deal(players, cards, deck)

    for i in range(players):
        print(f"Player №{i+1} has cards: {table[i]}")

    print(f"Deck in the final: {deck}")


if __name__ == '__main__':
    main(4, 6)

# 12. І, нарешті, третій, останній етап. Використовуючи рішення із попередніх двох завдань, 
# напишіть функцію get_password, яка згенерує нам випадковий надійний пароль та поверне його. 
# Алгоритм простий — ми генеруємо пароль за допомогою функції get_random_password і, якщо він 
# проходить перевірку на надійність функцією is_valid_password, повертаємо його, якщо ні — 
# повторюємо ітерацію знову.
# 
# Примітка: Хорошою практикою буде обмежити кількість спроб (наприклад, до 100), щоб не 
# отримати нескінченний цикл.

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num

def get_password():
    count = 0
    while count<100:
        password=get_random_password()
        if is_valid_password(password):
            return password
        count +=1
    return None
    


# 13. Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. 
# Функція повинна просканувати директорію path та повернути кортеж із двох списків. 
# Перший — це список файлів усередині директорії, другий — список директорій.

# Приклад виводу функції:

# (['.gitignore', 'readme.md'],
#  ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 
#   'module-05', 'module-06', 'module-07',
#   'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])

from pathlib import Path

def parse_folder(path):
    
    return ([file.name for file in path.iterdir() if file.is_file()],
             [file.name for file in path.iterdir() if file.is_dir()])


print(parse_folder(Path('.')))


# 14. Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, 
# розділених пробілами. Наприклад, якщо скрипт був викликаний командою: python run.py first second, 
# то функція parse_args повинна повернути рядок наступного виду 'first second'.

import sys


def parse_args():
    result =""
    
    if len(sys.argv)>1:
        result += sys.argv[1]
        for count in range(len(sys.argv)):
            if count>1:
                result+=' '+sys.argv[count]
            
    return result

