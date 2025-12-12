import random
grades = [random.randint(2, 5) for _ in range(22)]
avg_grade = sum(grades) / len(grades)
indices = [i for i, g in enumerate(grades) if g < avg_grade]
print(f"Средняя оценка: {avg_grade:.2f}")
print(f"Количество учеников ниже среднего: {len(indices)}")
print(f"Их номера: {indices}")
