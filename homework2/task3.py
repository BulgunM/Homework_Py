# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите натуральное число: '))

for i in range(0, number, 1):
    degree = 2 ** i
    if degree > number:
        break
    print(degree)