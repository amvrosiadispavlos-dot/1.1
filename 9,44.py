weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = int(input("Введите вес v (в граммах): "))
count = 0
from itertools import combinations
for r in range(1, len(weights)+1):
    for combo in combinations(weights, r):
        if sum(combo) == v:
            count += 1
print(f"Количество способов: {count}")
