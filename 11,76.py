import random
grades = [random.randint(2, 5) for _ in range(10)]
count_4_and_5 = sum(1 for g in grades if g == 4 or g == 5)
print(f"Оценки: {grades}")
print(f"Четверок и пятерок: {count_4_and_5}")
