year = {'key1':'Зима', 'key2':'Весна', 'key3':'Лето', 'key4':'Осень'}
list_winter = (12, 1, 2)
list_spring = (3, 4, 5)
list_summer = (6, 7, 8)
list_autumn = (9, 10, 11)
month = int(input('Введите месяц, в виде числа - '))
if list_winter.count(month) > 0:
    print(year.get('key1'))
elif list_spring.count(month) > 0:
    print(year.get('key2'))
elif list_summer.count(month) > 0:
    print(year.get('key3'))
elif list_autumn.count(month) > 0:
    print(year.get('key4'))
else:
    print('Введённое число не совпадает с нумерацией месяцов')