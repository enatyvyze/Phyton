our_list = [9, 8, 5, 2, 2]
print(f'Рейтинг: {our_list}')
new = int(input('Введите новое число для рейтинга - '))
if new > 9:
    our_list.insert(1, new)
elif new <= 9:
    our_list.insert(2, new)
elif new <= 8:
    our_list.insert(3, new)
elif new <= 5:
    our_list.insert(6, new)
elif new <= 2:
    our_list.insert(6, new)
print(f'Рейтинг: {our_list}')
