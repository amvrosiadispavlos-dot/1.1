import random

# а)
print("а) 10 целых чисел [0, 10]:")
for _ in range(10):
    print(random.randint(0, 10), end=' ')
print()

# б)
k = int(input("Введите k: "))
a = int(input("Введите a: "))
print(f"б) {k} целых чисел [0, {a}]:")
for _ in range(k):
    print(random.randint(0, a), end=' ')
print()

# в)
print("в) 20 целых чисел [10, 20]:")
for _ in range(20):
    print(random.randint(10, 20), end=' ')
print()

# г)
k = int(input("Введите k: "))
a = int(input("Введите a: "))
print(f"г) {k} целых чисел [-10, {a}]:")
for _ in range(k):
    print(random.randint(-10, a), end=' ')
print()

# д)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
k = random.randint(1, 15)
print(f"д) k = {k} целых чисел [{a}, {b}]:")
for _ in range(k):
    print(random.randint(a, b), end=' ')
print()
