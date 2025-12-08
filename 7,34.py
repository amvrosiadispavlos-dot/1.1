n = int(input("Введите количество учеников в каждом классе: "))
print(f"Введите рост учеников первого класса ({n} чисел через пробел):")
heights1 = list(map(float, input().split()[:n]))
print(f"Введите рост учеников второго класса ({n} чисел через пробел):")
heights2 = list(map(float, input().split()[:n]))
avg1 = sum(heights1) / n
avg2 = sum(heights2) / n
print(f"Средний рост в первом классе: {avg1:.2f}")
print(f"Средний рост во втором классе: {avg2:.2f}")
