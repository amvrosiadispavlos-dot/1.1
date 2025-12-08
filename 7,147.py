n = 20  
students = list(map(int, input("Введите численность 20 классов через пробел: ").split()[:20]))
max_students = max(students)
min_students = min(students)
difference = max_students - min_students
print(f"Самый большой класс: {max_students} учеников")
print(f"Самый маленький класс: {min_students} учеников")
print(f"Разница: {difference} учеников")
