import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Корни уравнения: x1 = {x1:.2f}, x2 = {x2:.2f}")
else:
    print("Уравнение не имеет вещественных корней")
