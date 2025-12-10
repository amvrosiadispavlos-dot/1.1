n = 11  
m = 4   
students = [[0] * m for _ in range(n)]
print("Введите количество учеников для каждой параллели (4 числа через пробел):")
for i in range(n):
    row = list(map(int, input(f"Параллель {i+1}: ").split()))
    if len(row) != m:
        print(f"Нужно {m} чисел. Повторите.")
        row = list(map(int, input(f"Параллель {i+1}: ").split()))
    students[i] = row
min_class = min(min(row) for row in students)
min_parallel_total = min(sum(row) for row in students)
min_class_type_total = min(sum(students[i][j] for i in range(n)) for j in range(m))
print(f"\nа) В самом малочисленном классе: {min_class} учеников")
print(f"б) Минимальное количество учеников в параллели: {min_parallel_total}")
print(f"в) Минимальное количество учеников по типам классов (А-Г): {min_class_type_total}")
