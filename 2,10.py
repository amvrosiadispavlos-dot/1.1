import math
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
arithmetic_mean = (num1 + num2) / 2
geometric_mean = math.sqrt(num1 * num2)
print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")
