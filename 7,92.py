grades = list(map(int, input("Введите 28 оценок через пробел: ").split()[:28]))
has_2 = 2 in grades
print(f"Есть двойки: {has_2}")
