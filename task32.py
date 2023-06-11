
# Задача 32: Определить индексы элементов массива(списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('Кол-во элементов массива: '))
minim = int(input('Мин.: '))
maxim = int(input('Макс.: '))
arr = [random.randint(0, 10) for i in range(n)]
print(arr)
for i in range(len(arr)):
    if minim <= arr[i] <= maxim:
        print(i)
