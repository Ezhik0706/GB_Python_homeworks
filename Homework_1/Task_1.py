# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные,
# выведите на экран.

variable_1 = -10
variable_2 = 38.5
variable_3 = 'Integration system'
variable_4 = False
print('Variable 1:', variable_1, type(variable_1))
print('Variable 2:', variable_2, type(variable_2))
print('Variable 3:', variable_3, type(variable_3))
print('Variable 4:', variable_4, type(variable_4), '\n')

user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))
lucky_number = user_age*3//10
print("Dear, %s! Your lucky number is %d" %(user_name, lucky_number))
