import random
february = [random.randint(0, 15) for _ in range(28)]
avg_feb = sum(february) / len(february)
print(f"Среднедневное количество осадков в феврале: {avg_feb:.2f}")
