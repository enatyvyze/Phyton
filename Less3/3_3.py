def my_func(a,b,c):
    if (a + b) >= (a + c):
        sum = int(a + b)
    else:
        sum = int(a + c)
    if (b + c) >= sum:
        sum = int(b + c)
    return sum
res = my_func(int(input('Введите первое число - ')),
              int(input('Введите второе число - ')),
              int(input('Введите третье число - ')))
print(f'Сумма двух самых больших чисел = {res}')
