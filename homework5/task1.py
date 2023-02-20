# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии. >

number_a = int(input('Введите число А: '))
number_b = int(input('Введите число В: '))


def degree(number_a, number_b):
    if number_b == 0:
        return 1
    return number_a * degree(number_a, number_b - 1)


print(degree(number_a, number_b))
