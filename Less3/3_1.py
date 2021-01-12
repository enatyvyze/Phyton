def my_func(num1, num2):
    if num2 == 0:
        print('Делить на ноль нельзя!')
    else:
        return num1 / num2
res = my_func(int(input('Введите первое число - ')), int(input('Введите второе число - ')))
print(f'Результат - {res}')