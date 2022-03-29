# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_answer = input('Enter number:')
sum_number = int(user_answer) + int(2*user_answer) + int(3*user_answer)
print('Sum of numbers equals: %d' %(sum_number))