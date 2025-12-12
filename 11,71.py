import random
grades = [random.randint(2, 5) for _ in range(25)]
failing = sum(1 for g in grades if g == 2)
print(f"Оценки: {grades}")
print(f"Количество неуспевающих: {failing}")
