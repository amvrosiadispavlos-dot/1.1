import random
january_precip = [random.randint(0, 20) for _ in range(31)]
avg_precip = sum(january_precip) / 31
days_above = [i+1 for i, p in enumerate(january_precip) if p > avg_precip]
print(f"Среднедневное количество осадков: {avg_precip:.2f}")
print(f"Дней с осадками выше среднего: {len(days_above)}")
print(f"Даты: {days_above}")
