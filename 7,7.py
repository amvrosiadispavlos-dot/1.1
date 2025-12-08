n = int(input("Введите количество элементов: "))
resistances = list(map(float, input("Введите сопротивления через пробел: ").split()[:n]))
total_resistance = 1 / sum(1 / r for r in resistances)
print("Общее сопротивление:", total_resistance)
