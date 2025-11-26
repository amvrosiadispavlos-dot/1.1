a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a + b > c) and (a + c > b) and (b + c > a):
    sides = sorted([a, b, c])
    right_triangle = abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-7
    print(f"Треугольник прямоугольный: {right_triangle}")
else:
    print("Треугольник не существует")
