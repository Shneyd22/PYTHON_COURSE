# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input())
count_one = 0
count_zero = 0
for i in range(n):
    x = random.randint(0, 1)
    print(x)
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_zero > count_one:
    print(count_one)
else:
    print(count_zero)
