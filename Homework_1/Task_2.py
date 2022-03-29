# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте
# форматирование строк.

user_time = int(input('Enter time in seconds: '))
quantity_hours = user_time // 3600
quantity_minutes = (user_time % 3600) // 60
quantity_seconds = user_time % 60
print(f"{quantity_hours:>02}:{quantity_minutes:>02}:{quantity_seconds:>02}")
