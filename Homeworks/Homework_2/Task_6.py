# Реализовать структуру данных «Товары». Она должна
# представлять собой список кортежей. Каждый кортеж
# хранит информацию об отдельном товаре. В кортеже
# должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру
# нужно сформировать программно, т.е. запрашивать
# все данные у пользователя.

index = 1
total_list = []
ready_structure = [(index, {'название': '', 'цена': '', 'количество': '', 'ед': ''})]
dict_structure = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics_structure = {'название': [], 'цена': [], 'количество': [], 'ед': []}
num = 1
while True:
    for key, value in dict_structure.items():
        if key == 'название':
            value = input('Введите название товара: ')
            dict_structure[key] = value
            analytics_structure[key].append(value)
        elif key == 'цена':
            value = input('Введите цену товара: ')
            dict_structure[key] = value
            analytics_structure[key].append(value)
        elif key == 'количество':
            value = input('Введите количество товара: ')
            dict_structure[key] = value
            analytics_structure[key].append(value)
        elif key == 'ед':
            value = input('Введите единицу измерения товара: ')
            dict_structure[key] = value
            analytics_structure[key].append(value)
    total_list.append((index, dict_structure))
    index +=1
    print(f'Структура товаров: {total_list}\nАналитика: {analytics_structure}')
    message = input('Для добавления нового товара нажмите Enter, для выхода из программы нажмите q!')
    if message.lower() == 'q':
        break