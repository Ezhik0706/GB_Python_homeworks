# Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с
# новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10
# букв в слове.

user_string = input('Enter some words across space: ')
user_string = user_string.split(' ')
num_str = 0
for el in user_string:
    num_str += 1
    print(f'{num_str} {el[:11]}')
