# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict.

# across list
while True:
    user_month = int(input('Please enter number of month (1-12): '))
    if user_month >= 1 and user_month <= 12:
        break
    else:
        print('Enter correct number of month')
season_list = [[1,'зима'], [2,'зима'], [3,'весна'], [4,'весна'], [5,'весна'], [6,'лето'], [7,'лето'], [8,'лето'],
               [9,'осень'], [10,'осень'], [11,'осень'], [12,'зима']]
for el in season_list:
    if user_month in el:
        print(el[1])
        break

# across dictionary
while True:
    user_month = int(input('Please enter number of month (1-12): '))
    if user_month >= 1 and user_month <= 12:
        break
    else:
        print('Enter correct number of month')
month_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for keys, values in month_dict.items():
    for i in values:
        if i == user_month:
            print(f'The time of year is - {keys}')
            break