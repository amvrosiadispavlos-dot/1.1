import random
n = int(input("Введите n: "))
a = int(input("Введите a: "))
b = int(input("Введите b: "))
arr = [random.randint(a, b) for _ in range(n)]
print(arr)
