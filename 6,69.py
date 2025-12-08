def split_rectangle(a, b):
    squares = []
    while a > 0 and b > 0:
        if a >= b:
            count = a // b
            squares.append((b, count))
            a %= b
        else:
            count = b // a
            squares.append((a, count))
            b %= a
    return squares
a, b = 425, 131
result = split_rectangle(a, b)
print(f"Исходный прямоугольник {a}×{b} разрезается на квадраты:")
for size, count in result:
    print(f"  Квадрат со стороной {size}: {count} шт.")
