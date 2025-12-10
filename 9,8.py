n = 14  
m = 3  
grades_table = [[0] * m for _ in range(n)]
print("Введите оценки каждого студента по трём предметам (через пробел):")
for i in range(n):
    subject_grades = list(map(int, input(f"Студент {i+1} (предметы 1-{m}): ").split()))
    if len(subject_grades) != m:
        print(f"Ошибка: нужно ввести ровно {m} оценки. Повторите ввод.")
        subject_grades = list(map(int, input(f"Студент {i+1} (предметы 1-{m}): ").split()))
    grades_table[i] = subject_grades
students_without_twos = sum(2 not in row for row in grades_table)
subjects_only_4_and_5 = 0
for j in range(m):
    column_grades = [grades_table[i][j] for i in range(n)]
    if all(grade == 5 or grade == 4 for grade in column_grades):
        subjects_only_4_and_5 += 1
twos_per_subject = [sum(grades_table[i][j] == 2 for i in range(n)) for j in range(m)]
print("\nРезультаты:")
print(f"а) Количество студентов, сдавших сессию без двоек: {students_without_twos}")
print(f"б) Количество предметов с оценками только «5» и «4»: {subjects_only_4_and_5}")
print("в) Количество двоек по каждому предмету:")
for j in range(m):
    print(f"   Предмет {j+1}: {twos_per_subject[j]}")
