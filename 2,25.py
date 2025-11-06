a = float(input("Введите длину параллелепипеда: "))
b = float(input("Введите ширину параллелепипеда: "))
c = float(input("Введите высоту параллелепипеда: "))
volume = a * b * c
lateral_surface_area = 2 * c * (a + b)
print(f"Объем: {volume}")
print(f"Площадь боковой поверхности: {lateral_surface_area}")
