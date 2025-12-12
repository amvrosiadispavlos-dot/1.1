import random
prices = [random.randint(100, 1000) for _ in range(60)]
min_price = min(prices)
count = prices.count(min_price)
print(f"Количество самых дешевых книг (цена {min_price}): {count}")
