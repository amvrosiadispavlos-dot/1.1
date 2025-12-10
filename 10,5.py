import random

print("30 чисел [0, 5], вывод только нечётных:")
for _ in range(30):
    num = random.randint(0, 5)
    if num % 2 != 0:
        print(num, end=' ')
print()
