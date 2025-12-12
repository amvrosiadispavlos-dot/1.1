import random
prices = [random.randint(100, 10000) for _ in range(30)]
sorted_prices = sorted(prices, reverse=True)
top_two = sorted_prices[:2]
print(f"Стоимость двух самых дорогих товаров: {top_two}")
