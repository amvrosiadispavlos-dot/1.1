n = 18  
m = 3   
grades_table = [[0] * m for _ in range(n)]
print("Введите оценки каждого ученика по трём предметам (через пробел):")
for i in range(n):
    subject_grades = list(map(int, input(f"Ученик {i+1} (предметы 1-{m}): ").split()))
    if len(subject_grades) != m:
        print(f"Ошибка: нужно ввести ровно {m} оценки. Повторите ввод.")
        subject_grades = list(map(int, input(f"Ученик {i+1} (предметы 1-{m}): ").split()))
    grades_table[i] = subject_grades
total_fives = sum(grades_table[i][j] == 5 for i in range(n) for j in range(m))
threes_per_student = [row.count(3) for row in grades_table]
twos_per_subject = [sum(grades_table[i][j] == 2 for i in range(n)) for j in range(m)]
print("\nРезультаты:")
print(f"а) Общее количество пятёрок: {total_fives}")
print("б) Количество троек у каждого ученика:")
for i in range(n):
    print(f"   Ученик {i+1}: {threes_per_student[i]}")
print("в) Количество двоек по каждому предмету:")
for j in range(m):
    print(f"   Предмет {j+1}: {twos_per_subject[j]}")
