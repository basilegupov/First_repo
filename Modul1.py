side_one, side_two, side_three = 5, 7, 10
print(side_one, side_two, side_three)

side_one = side_two = side_three = 5
print(side_one, side_two, side_three)


side_one, side_two, side_three = 5, 7, 10

print(side_one, side_two, side_three, sep=',', end='\t')

side_one, side_two, side_three = 3, 4, 1
print(side_one, side_two, side_three, sep='\t:\t')



name = 'Alice'
age = 30

message = f'My name is {name}. I am {age/2} years old'
print(message)

message = 'Test 2, My name is {}. I am {} years old'.format(name, age)
print(message)

message = 'Test 3, My name is %s. I am %d years old' % (name, age)
print(message)

message = 'Test 4, My name is ' + name + ' I am ' + str(age) + ' years old'
print(message)



print("\N{slightly smiling face}") # Використання escape sequence \N{} з назвою символу
print("\u263A")  # Смайлик у шістнадцятковому форматі
print("\U0001F600")  # Смайлик у шістнадцятковому форматі з великою літерою "U"


# Ітерпретатор розуміє значення \n і розуміє, що строку потрібно перенести в наступний рядок
# У випадках подвійного слешу "\\" в стандартону випадку слеші заміняються на одинарні

string = 'Hi\nHello'
print(string)

path = "C:\\Users\\Username\\Documents"
print(path) # C:\Users\Username\Documents


# Ітерпретатор зчитує "r" перед строкою і розуміє, що слеші потрібно ігнорувати
# Тобто для строки відкидається стандартне форматування і залишається її вхідне відображення

raw_string = r'Hi\nHello'
print(raw_string) #Hi\nHello

raw_path = r"C:\\Users\\Username\\Documents"
print(raw_path) # C:\\Users\\Username\\Documents


age = 25
weight = 25.0
room = '25'
# Перевірка типу даних
print(type(age), type(weight), type(room))


