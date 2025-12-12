import random
results = [random.choice([1, 2, 3]) for _ in range(20)]
wins = sum(1 for x in results if x == 3)
draws = sum(1 for x in results if x == 1)
losses = sum(1 for x in results if x == 2)
print(f"Выигрышей: {wins}")
print(f"Ничьих: {draws}")
print(f"Проигрышей: {losses}")
