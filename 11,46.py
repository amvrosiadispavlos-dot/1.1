import random
resistors = [random.randint(1, 100) for _ in range(20)]
total_series = sum(resistors)
print(f"Сопротивления: {resistors}")
print(f"Общее сопротивление (последовательное): {total_series}")
