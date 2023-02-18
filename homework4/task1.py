# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

lenght_1 = int(input('Введите количество элементов первого множества: '))
list_1 = []

for i in range(lenght_1):
    numbers_1 = int(input('Введите элементы первого множества: '))
    list_1.append(numbers_1)


lenght_2 = int(input('Введите количество элементов второго множества: '))
list_2 = []

for i in range(lenght_2):
    numbers_2 = int(input('Введите элементы второго множества: '))
    list_2.append(numbers_2)


# print(list_1)
# print('------')
# print(list_2)

res_list_1 = set(list_1)
res_list_2 = set(list_2)

result_set = res_list_1.intersection(res_list_2)

print(sorted(result_set))