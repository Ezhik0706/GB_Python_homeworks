# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер
# дня, на который общий результат спортсмена составить
# не менее b километров. Программа должна принимать
# значения параметров a и b и выводить одно натуральное
# число — номер дня.

a = int(input('Please, enter daily result of running: '))
b = int(input('Please enter the needed result: '))
day_number = 1
while a <= b:
    a *= 1.1
    day_number += 1
print('Day of needed result is %d' %(day_number))