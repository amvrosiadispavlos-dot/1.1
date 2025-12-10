n = 8 
m = 5  
scores = [[0] * m for _ in range(n)]
print("Введите баллы каждого спортсмена по 5 видам спорта (через пробел):")
for i in range(n):
    row = list(map(int, input(f"Спортсмен {i+1}: ").split()))
    if len(row) != m:
        print(f"Нужно {m} чисел. Повторите.")
        row = list(map(int, input(f"Спортсмен {i+1}: ").split()))
    scores[i] = row
max_score = max(max(row) for row in scores)
total_per_athlete = [sum(row) for row in scores]
winner_score = max(total_per_athlete)
print(f"\nа) Максимальная оценка в таблице: {max_score}")
print(f"б) Баллы победителя: {winner_score}")
