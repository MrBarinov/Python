# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 3
# -> 1

import random
n = int(input("Введите ваше число: "))
a = [i for i in random.sample(range(100), n)]
x = int(input("Введите число которое встречается: "))
print(f"В массиве {a} ваше число {x} встречается {a.count(x)} раз" )


# from collections import Counter; n = Counter([x])
