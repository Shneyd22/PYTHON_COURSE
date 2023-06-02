# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

import random

n = int(input('Введите кол-во элементов массива '))
x = int(input('Задайте число '))
a = []
for i in range(0, n):
    a.append(random.randint(1, 10))
print(*a)
print(x)
min = 10
near_num = 0
for i in range(0, n):
    if (a[i] > x) and ((a[i] - x) < min):
        min = a[i] - x
        near_num = a[i]
    elif (a[i] < x) and ((x - a[i]) < min):
        min = x - a[i]
        near_num = a[i]
print(f"Ближайшее к {x} число в массиве: {near_num}")
