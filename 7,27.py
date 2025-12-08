grades = list(map(int, input("Введите оценки 20 учеников через пробел: ").split()[:20]))
average = sum(grades) / len(grades)
print("Средняя оценка по физике:", average)
