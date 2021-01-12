
def my_func(x ,y):
    if x < 0:
        print('X Должен быть положительным')
    elif y > 0:
        print('Y Должен быть отрицательным')
    else:
        return x ** y
res = my_func(float(input('Введите действительное положительное число x - ')),
        int(input('Введите целое отрицательное число y - ')))
print(f'Реузльтат - {res}')