import math
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
abs_x = abs(x)
abs_y = abs(y)
average_arith = (abs_x + abs_y) / 2
average_geom = math.sqrt(abs_x * abs_y)
print(f"Среднее арифметическое модулей: {average_arith:.4f}")
print(f"Среднее геометрическое модулей: {average_geom:.4f}")
