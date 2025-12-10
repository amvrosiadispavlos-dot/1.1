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
print("\nа) Самый малочисленный класс в каждой параллели:")
for i in range(n):
    min_in_parallel = min(students[i])
    print(f"   Параллель {i+1}: {min_in_parallel} учеников")
print("\nб) Самый малочисленный класс по каждому типу (А-Г):")
for j in range(m):
    min_in_type = min(students[i][j] for i in range(n))
    class_name = chr(ord('А') + j)
    print(f"   Класс {class_name}: {min_in_type} учеников")
