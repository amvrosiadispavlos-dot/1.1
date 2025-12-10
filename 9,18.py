n_groups = 3
n_students = 20
n_exams = 3
scores = [[[0] * n_exams for _ in range(n_students)] for _ in range(n_groups)]
for g in range(n_groups):
    print(f"Группа {g+1}:")
    for s in range(n_students):
        row = list(map(int, input(f"  Студент {s+1} (3 оценки): ").split()))
        if len(row) != n_exams:
            print("Нужно 3 оценки. Повторите.")
            row = list(map(int, input(f"  Студент {s+1}: ").split()))
        scores[g][s] = row
avg_per_group = []
for g in range(n_groups):
    total = sum(sum(scores[g][s]) for s in range(n_students))
    avg = total / (n_students * n_exams)
    avg_per_group.append(avg)
max_avg = max(avg_per_group)
best_group = avg_per_group.index(max_avg) + 1
print(f"\nЛучшая группа по среднему баллу: группа {best_group} ({max_avg:.2f})")
