import random
results = [random.choice([0, 1, 3]) for _ in range(20)]
wins = sum(1 for x in results if x == 3)
draws = sum(1 for x in results if x == 1)
print(f"Результаты: {results}")
print(f"Выигрышей: {wins}")
print(f"Ничьих: {draws}")
