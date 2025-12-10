n = 12 
m = 3  
print("Ввод оценок по строкам (для каждого ученика 3 оценки через пробел):")
sum_marks = 0
for student in range(1, n + 1):
    marks = list(map(int, input(f"Ученик {student}: ").split()))
    if len(marks) != m:
        print(f"Нужно ввести ровно {m} оценки. Повторите ввод для ученика {student}.")
        marks = list(map(int, input(f"Ученик {student}: ").split()))
    sum_marks += sum(marks)
print(f"Сумма всех оценок: {sum_marks}")
n = 12 
m = 3   
print("Ввод оценок по столбцам (для каждого предмета 12 оценок через пробел):")
sum_marks = 0
for subject in range(1, m + 1):
    marks = list(map(int, input(f"Предмет {subject}: ").split()))
    if len(marks) != n:
        print(f"Нужно ввести ровно {n} оценок. Повторите ввод для предмета {subject}.")
        marks = list(map(int, input(f"Предмет {subject}: ").split()))
    sum_marks += sum(marks)
print(f"Сумма всех оценок: {sum_marks}")
