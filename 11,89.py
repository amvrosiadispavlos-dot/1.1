import random
august_precip = [random.randint(0, 15) for _ in range(31)]
rainy_days = [x for x in august_precip if x > 0]
avg = sum(rainy_days) / len(rainy_days) if rainy_days else 0
print(f"Среднее осадков в дождливые дни: {avg:.2f}")
