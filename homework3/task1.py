# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

list_length = int(input('Введите длину списка: '))
number = int(input('Введите искомое число: '))
list = []

for i in range(list_length):
    list.append(random.randint(1, 100))
print(list)

nearest_value = list[0]
for i in range(len(list)):
    if list[i] == number:
        count_number = + 1
        print(f'Искомое число {number} встречается {count_number} раз')
    else:
        if abs(list[i] - number) < abs(nearest_value - number):
            nearest_value = list[i]
print(f'Максимально близкое значение к {number} = {nearest_value}')
