n = 15  
m = 3  
results_table = [[0] * m for _ in range(n)]
print("Введите баллы каждого спортсмена по трём программам (через пробел):")
for i in range(n):
    programs_scores = list(map(float, input(f"Спортсмен {i+1} (обязательная, короткая, произвольная): ").split()))
    if len(programs_scores) != m:
        print(f"Ошибка: нужно ввести ровно {m} значения. Повторите ввод.")
        programs_scores = list(map(float, input(f"Спортсмен {i+1} (обязательная, короткая, произвольная): ").split()))
    results_table[i] = programs_scores
average_per_athlete = [sum(row) / m for row in results_table]
average_per_program = [sum(results_table[i][j] for i in range(n)) / n for j in range(m)]
program_names = ["Обязательная", "Короткая", "Произвольная"]
print("\nРезультаты:")
print("а) Среднее количество баллов каждого спортсмена:")
for i in range(n):
    print(f"   Спортсмен {i+1}: {average_per_athlete[i]:.2f}")
print("\nб) Среднее количество баллов по каждому виду программы:")
for j in range(m):
    print(f"   {program_names[j]}: {average_per_program[j]:.2f}")
