# Найдите сумму цифр трехзначного числа.

# in
# 123

# out
# 6

num = int(input("Введите трехзначное число: "))
sum = 0

while num != 0:
    sum = num % 10 + sum
    num // 10
print(sum)
