import random
results = [random.randint(120, 300) for _ in range(25)] 
winner_time = min(results)
print(f"Результат победителя: {winner_time} секунд")
