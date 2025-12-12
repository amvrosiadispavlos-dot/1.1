import random
sales = [random.randint(1000, 10000) for _ in range(31)]
s = 5000
days_above = sum(1 for x in sales if x > s)
print(f"Количество дней с продажами > {s}: {days_above}")
