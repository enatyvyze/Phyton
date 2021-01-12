stroka = str(input('Введите несколько слов через пробел - '))
our_list = list(stroka.split())
count = 0
while count < len(our_list):
    number = count + 1
    if len(our_list[count]) <= 10:
        strochechka = str(our_list[count])
        print(f'{number} {strochechka}')
        count += 1
    else:
        strochechka = str(our_list[count])
        print(f'{number} {strochechka}'[:12])
        count += 1
