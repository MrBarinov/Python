# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def stepen(a, b):
    if b == 1:
        return a
    else:
        return a * stepen(a, b - 1)
print(stepen(int(input("Введите число: ")), int(input("Введите его степень: "))))