# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input('Введите число: '))
b = int(input('Введите степень: '))


def deg_calc(x, y):
    result = 0
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        result = x * deg_calc(x, y - 1)
        return result


print(deg_calc(a, b))
