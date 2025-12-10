n = 5  
m = 6   
students = [[0] * m for _ in range(n)]
print("Введите количество студентов в каждой группе (6 чисел через пробел):")
for i in range(n):
    row = list(map(int, input(f"Курс {i+1}: ").split()))
    if len(row) != m:
        print(f"Нужно {m} чисел. Повторите.")
        row = list(map(int, input(f"Курс {i+1}: ").split()))
    students[i] = row
total_per_course = [sum(row) for row in students]
min_course_total = min(total_per_course)
course_index = total_per_course.index(min_course_total) + 1
min_students = min(min(row) for row in students)
for i in range(n):
    if min_students in students[i]:
        min_course = i + 1
        min_group = students[i].index(min_students) + 1
        break
print(f"\nа) Курс с минимальным количеством студентов: {course_index}")
print(f"б) Самая малочисленная группа: курс {min_course}, группа {min_group}")
print("в) Самая малочисленная группа на каждом курсе:")
for i in range(n):
    min_in_course = min(students[i])
    group_index = students[i].index(min_in_course) + 1
    print(f"   Курс {i+1}: группа {group_index}")
