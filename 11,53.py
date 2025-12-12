import random
students_per_class = [random.randint(15, 35) for _ in range(42)]
total_students = sum(students_per_class)
print(f"Общее число учеников: {total_students}")
print(f"Четырехзначное число: {1000 <= total_students <= 9999}")
