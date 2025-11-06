import math
a = float(input("Введите большее основание a: "))
b = float(input("Введите меньшее основание b: "))
h = float(input("Введите высоту h: "))
c = math.sqrt(h**2 + ((a - b) / 2)**2)
P = a + b + 2 * c
print(f"Периметр трапеции: {P:.2f}")
