import random
candy_prices = [random.randint(100, 500) for _ in range(30)]
min_price = min(candy_prices)
# a)
first_index = candy_prices.index(min_price)
# б)
last_index = len(candy_prices) - 1 - candy_prices[::-1].index(min_price)
print(f"Самая низкая цена: {min_price}")
print(f"a) Первый самый дешевый вид: {first_index+1}")
print(f"б) Последний самый дешевый вид: {last_index+1}")
