import random

m = random.randint(1, 20)
n = random.randint(1, 20)
print(f"m = {m}, n = {n}")

a = int(input("Введите a: "))
b = int(input("Введите b: "))

print(f"{n} целых чисел [{a}, {b}]:")
for _ in range(n):
    print(random.randint(a, b), end=' ')
print()

print(f"{m} вещественных чисел [0, {n}]:")
for _ in range(m):
    print(random.uniform(0, n), end=' ')
print()
