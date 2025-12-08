a = int(input("Введите длину a: "))
b = int(input("Введите ширину b: "))
result = split_rectangle(a, b) 
print(f"Прямоугольник {a}*{b} разрезается на квадраты:")
for size, count in result:
    print(f"  Квадрат со стороной {size}: {count} шт.")
