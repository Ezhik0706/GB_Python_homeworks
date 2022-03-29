# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

#Реализована проверка на то, что введенное число является положительным.
while True:
    user_number = int(input('Please, enter integer number that more than 0: '))
    if user_number > 0:
        break
    else:
        print('Enter correct number: ')

max_digit = user_number % 10
while user_number > 0:
    user_number //= 10
    digit = user_number % 10
    if digit > max_digit:
        max_digit = digit
print('Max digit in number is: %d' %(max_digit))