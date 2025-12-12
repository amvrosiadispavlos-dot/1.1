import random
prices = [random.randint(5000, 50000) for _ in range(50)]
max_price = max(prices)
print(f"Стоимость самого дорогого автомобиля: {max_price}")
