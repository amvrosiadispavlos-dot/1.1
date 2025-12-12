import random
prices = [random.randint(100, 10000) for _ in range(12)]
total_cost = sum(prices)
print(f"Стоимость предметов: {prices}")
print(f"Общая стоимость: {total_cost}")
