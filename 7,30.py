n = int(input("Введите количество предметов: "))
masses = list(map(float, input("Введите массы предметов через пробел: ").split()[:n]))
average = sum(masses) / n
print("Средняя масса:", average)
