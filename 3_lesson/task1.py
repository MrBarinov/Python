# num = {k: v ** 3 for k, v in zip("ASDFGHJK", range(1, 11))}
	
# print(num)

# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
print(len(set(list_nums)))