lst = [1, 2, 3, 4, 5]
lst = [100] + lst
print(f"Результат: {lst}")

lst = [1, 2, 3, 4, 5]
num = 99
lst = [num] + lst
print(f"Результат: {lst}")

lst = [1, 2, 3, 4, 5]
num = 99
index = 2
lst = lst[:index] + [num] + lst[index:]
print(f"Результат: {lst}")
