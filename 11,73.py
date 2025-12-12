import random
heights = [random.randint(150, 190) for _ in range(22)]
r = 170
count = sum(1 for h in heights if h <= r)
print(f"Количество учеников с ростом ≤ {r}: {count}")
