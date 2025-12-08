n = int(input("Введите количество предметов: "))
masses = list(map(float, input("Введите массы предметов через пробел: ").split()[:n]))
print("Общая масса:", sum(masses))
