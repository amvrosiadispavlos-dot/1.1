n = int(input("Введите количество учеников в каждом классе: "))
print(f"Введите оценки по физике первого класса ({n} чисел через пробел):")
grades1 = list(map(int, input().split()[:n]))
print(f"Введите оценки по физике второго класса ({n} чисел через пробел):")
grades2 = list(map(int, input().split()[:n]))
avg1 = sum(grades1) / n
avg2 = sum(grades2) / n
print(f"Средняя оценка в первом классе: {avg1:.2f}")
print(f"Средняя оценка во втором классе: {avg2:.2f}")
