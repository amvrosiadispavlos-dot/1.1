n = int(input("Введите количество элементов: "))
resistances = list(map(float, input("Введите сопротивления через пробел: ").split()[:n]))
print("Общее сопротивление:", sum(resistances))
