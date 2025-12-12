import random
candy_prices = [random.randint(100, 500) for _ in range(20)]
min_price = min(candy_prices)
print(f"Цена самых дешевых конфет: {min_price}")
