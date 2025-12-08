grades = list(map(int, input("Введите оценки по 10 предметам через пробел: ").split()[:10]))
average = sum(grades) / len(grades)
print("Средняя оценка ученика:", average)
