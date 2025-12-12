import random
scores = [random.randint(5, 10) for _ in range(8)]
print(f"Оценки судей: {scores}")
sorted_scores = sorted(scores)
final_scores = sorted_scores[1:-1]  
final_score = sum(final_scores) / len(final_scores)
print(f"Удалены: {sorted_scores[0]} и {sorted_scores[-1]}")
print(f"Оставшиеся оценки: {final_scores}")
print(f"Итоговая оценка: {final_score:.2f}")
