
# В некоторой школе решили набрать три новых 
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может 
# сидеть два учащихся. Известно количество учащихся 
# в каждом из трех классов. Выведите наименьшее число 
# парт, которое нужно приобрести для них.

a = int(input("Введите первый класс: "))
b = int(input("Введите второй класс: "))
c = int(input("Введите третий класс: "))

print(-(-(a + b + c) // 2 // 3))