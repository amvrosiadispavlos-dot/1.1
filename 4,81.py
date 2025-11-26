a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a + b > c) and (a + c > b) and (b + c > a):
    sides = sorted([a, b, c])
    cos_c = (sides[0]**2 + sides[1]**2 - sides[2]**2) / (2 * sides[0] * sides[1])
    if abs(cos_c) < 1e-7:
        print("Треугольник прямоугольный")
    elif cos_c > 0:
        print("Треугольник остроугольный")
    else:
        print("Треугольник тупоугольный")
else:
    print("Треугольник не существует")
    a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a + b > c) and (a + c > b) and (b + c > a):
    sides = sorted([a, b, c])
    cos_c = (sides[0]**2 + sides[1]**2 - sides[2]**2) / (2 * sides[0] * sides[1])
    if abs(cos_c) < 1e-7:
        angle_type = "прямоугольный"
    elif cos_c > 0:
        angle_type = "остроугольный"
    else:
        angle_type = "тупоугольный"
    if a == b == c:
        side_type = "равносторонний"
    elif a == b or b == c or a == c:
        side_type = "равнобедренный"
    else:
        side_type = "разносторонний"
    print(f"Треугольник {angle_type}, {side_type}")
else:
    print("Треугольник не существует")
