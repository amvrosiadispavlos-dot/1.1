import random

print("50 чисел [0, 5], вывод только 0 и 1:")
for _ in range(50):
    num = random.randint(0, 5)
    if num == 0 or num == 1:
        print(num, end=' ')
print()
