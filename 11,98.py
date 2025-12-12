import random
prices = [random.randint(100, 1000) for _ in range(20)]
avg_price = sum(prices) / len(prices)
count = sum(1 for p in prices if p < avg_price)
print(f"Средняя стоимость: {avg_price:.2f}")
print(f"Видов товара дешевле среднего: {count}")
