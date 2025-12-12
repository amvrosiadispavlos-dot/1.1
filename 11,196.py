grades = [5, 5, 5, 5, 5, 4, 4, 3, 5, 4, 3, 2, 5, 4, 3, 4, 5, 4, 3, 5, 4, 3, 2, 1]
count_fives = grades.index(next(g for g in grades if g != 5)) if any(g != 5 for g in grades) else len(grades)
print(f"Количество учеников с оценкой '5': {count_fives}")
