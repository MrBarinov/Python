# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# Пример:
# 5 -> 1 0 1 1 0
# 2

n = int(input("Введите колличество монеток: "))
reshka = gerb = 0

for i in range(n):
    count = int(input("Введите колличество (решка - 0; орел - 1): "))
    if count < 1:
        reshka += 1
    else:
        gerb += 1
if gerb < reshka: 
    print(f"{gerb} монеты, надо перевернуть")
else:
    print(f"{reshka} монеты, надо перевернуть")