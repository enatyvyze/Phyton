#Не смог додумать как решить эту задачу по условиям задания

our_list = []
a = int(input('Введите количество элементов вашего списка - '))
count = 0
while (count < a):
    our_list.append(input('Введите ваш элемент - '))
    count += 1
n = 1
#while
el = our_list[0]
el2 = our_list[1]
our_list.insert(1,el)
our_list.insert(0,el2)
print(our_list)

#print(el)
# while True:
# print(our_list)