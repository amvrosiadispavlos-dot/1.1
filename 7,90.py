grades = list(map(int, input("Введите 12 оценок через пробел: ").split()[:12]))
has_3 = 3 in grades
print(f"Среди оценок нет троек: {not has_3}")
