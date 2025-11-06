import math
a = float(input("Введите большее основание: "))
b = float(input("Введите меньшее основание: "))
h = float(input("Введите высоту: "))
side = math.sqrt(h**2 + ((a - b)/2)**2)
perimeter = a + b + 2 * side
print(f"Периметр трапеции: {perimeter:.4f}")
