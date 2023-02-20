# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

number_a = int(input('Введите число А: '))
number_b = int(input('Введите число В: '))


def sum_numbers(number_a, number_b):
    if number_b == 0:
        return number_a
    return sum_numbers(number_a + 1, number_b - 1)


print(sum_numbers(number_a, number_b))
