# Найдите сумму цифр трехзначного числа.

# in
# 123

# out
# 6

num = int(input("Введите число: "))
sum = 0

while num != 0:
    sum = num % 10 + sum
    num = num // 10
print(sum)
