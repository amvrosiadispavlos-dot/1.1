import math
a = float(input("Введите значение a: "))
result_a = math.sqrt((2*a + math.sin(abs(5*a))) / 3.56)
print(f"√((2a + sin|5a|)/3,56) = {result_a}")
x = float(input("Введите значение x (x ≠ 0): "))
if x == 0:
    print("Ошибка: x не может быть равен 0")
else:
    result_b = math.sin((3.2 + math.sqrt(1 + x)) / (15*x))
    print(f"sin((3,2 + √(1 + x))/(15x)) = {result_b}")
