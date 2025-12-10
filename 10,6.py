import random

zeros = 0
ones = 0
print("50 чисел 0 или 1:")
for _ in range(50):
    num = random.randint(0, 1)
    print(num, end=' ')
    if num == 0:
        zeros += 1
    else:
        ones += 1

print(f"\nКоличество нулей: {zeros}")
print(f"Количество единиц: {ones}")
