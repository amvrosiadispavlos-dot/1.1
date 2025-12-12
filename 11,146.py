import random
results = [round(random.uniform(9.50, 12.00), 2) for _ in range(23)]
sorted_results = sorted(results)
best_four = sorted_results[:4]
indices = [results.index(time) + 1 for time in best_four]
print(f"Лучшие результаты: {best_four}")
print(f"Индексы спортсменов: {indices}")
print(f"Сумма времени: {sum(best_four):.2f}")
