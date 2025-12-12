import random
qualification_score = 7000
scores = [random.randint(600, 900) for _ in range(10)]
total_score = sum(scores)
print(f"Баллы по видам: {scores}")
print(f"Общая сумма: {total_score}")
print(f"Порог: {qualification_score}")
print(f"Вышел в следующий этап: {total_score > qualification_score}")
