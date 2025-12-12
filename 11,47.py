import random
resistors = [random.randint(1, 100) for _ in range(20)]
total_parallel = 1 / sum(1/r for r in resistors)
print(f"Сопротивления: {resistors}")
print(f"Общее сопротивление (параллельное): {total_parallel:.2f}")
