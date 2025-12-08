n = int(input("Введите количество судей: "))
scores = list(map(float, input("Введите оценки судей через пробел: ").split()[:n]))
if n <= 2:
    print("Недостаточно оценок для расчёта")
else:
    max_score = max(scores)
    min_score = min(scores)
    scores.remove(max_score)
    scores.remove(min_score)
    average_score = sum(scores) / len(scores)
    print(f"Зачётная оценка спортсмена: {average_score:.2f}")
