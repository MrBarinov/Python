# 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

n = int(input("Введите ваше число, стекпени которых хотите получить: "))

k = n

while k < n:
    k *= 2
    print(k)