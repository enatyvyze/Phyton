print('Здравствуйте, давайте проанализируем финансы вашей компании!')
a = int(input('Введите сумму выручки компании - '))
b = int(input('Введите сумму издержки компании - '))
c = int(input('Введите количество сотрудников - '))
n = (a - b)
if n > 0:
    n1 = int((n/a)*100)
    n2 = int(n/c)
    print(f'Поздравляю, ваша компания работает с прибылью в {n} руб.')
    print(f'Рентабельность вашей выручки состовляет {n1} %')
    print(f'А прибыль на каждого сотрудника составляет - {n2} руб.')
else:
    print('Увы, вы работаете в убыток(')

