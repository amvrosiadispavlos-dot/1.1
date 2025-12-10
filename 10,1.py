import random

# а)
print("а) 8 случайных чисел [0, 1):")
for _ in range(8):
    print(random.random(), end=' ')
print()

# б)
k = int(input("Введите k: "))
print(f"б) {k} случайных чисел [0, 1):")
for _ in range(k):
    print(random.random(), end=' ')
print()

# в)
print("в) 15 случайных чисел [25, 26):")
for _ in range(15):
    print(random.uniform(25, 26), end=' ')
print()

# г)
print("г) 20 случайных чисел [0, 15):")
for _ in range(20):
    print(random.uniform(0, 15), end=' ')
print()

# д)
a = int(input("Введите a: "))
b = float(input("Введите b: "))
k = random.randint(1, a)
print(f"д) k = {k} чисел [0, {b}):")
for _ in range(k):
    print(random.uniform(0, b), end=' ')
print()

# е)
print("е) 10 случайных чисел [-40, 40):")
for _ in range(10):
    print(random.uniform(-40, 40), end=' ')
print()

# ж)
m = int(input("Введите m: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))
k = random.randint(1, m)
print(f"ж) k = {k} чисел [{a}, {b}):")
for _ in range(k):
    print(random.uniform(a, b), end=' ')
print()
