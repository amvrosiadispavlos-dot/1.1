import random
grades = [random.randint(2, 5) for _ in range(22)]
counts = {2:0, 3:0, 4:0, 5:0}
for g in grades:
    counts[g] += 1
for grade, count in counts.items():
    print(f"{grade}: {count}")
