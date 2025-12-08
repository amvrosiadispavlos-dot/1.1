n = int(input("Введите количество студентов: "))
count_2 = 0
for i in range(n):
    print(f"Студент {i+1}:")
    grade1 = int(input("  Оценка за первый экзамен: "))
    grade2 = int(input("  Оценка за второй экзамен: "))
    if grade1 == 2 or grade2 == 2:
        count_2 += 1
print(f"Количество студентов, получивших двойку: {count_2}")
