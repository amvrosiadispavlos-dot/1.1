import random

def generate_position():
    return random.randint(1, 8), random.randint(1, 8)

# а) Белая пешка (ходит снизу вверх)
print("а) Белая пешка:")
a, b = generate_position()
while True:
    c, d = generate_position()
    # Обычный ход: вперед на 1 или 2 клетки с начальной позиции
    if (d == b + 1 and c == a) or (b == 2 and d == 4 and c == a):
        print(f"  Обычный ход: ({a},{b}) -> ({c},{d})")
        break
    # Взятие: ход по диагонали на 1 клетку
    if d == b + 1 and abs(c - a) == 1:
        print(f"  Взятие: ({a},{b}) -> ({c},{d})")
        break

# б) Черная пешка (ходит сверху вниз)
print("\nб) Черная пешка:")
a, b = generate_position()
while True:
    c, d = generate_position()
    # Обычный ход: вниз на 1 или 2 клетки с начальной позиции
    if (d == b - 1 and c == a) or (b == 7 and d == 5 and c == a):
        print(f"  Обычный ход: ({a},{b}) -> ({c},{d})")
        break
    # Взятие: ход по диагонали вниз на 1 клетку
    if d == b - 1 and abs(c - a) == 1:
        print(f"  Взятие: ({a},{b}) -> ({c},{d})")
        break

# в) Конь угрожает полю
print("\nв) Конь:")
a, b = generate_position()
while True:
    c, d = generate_position()
    # Ход коня: разница 2 и 1 или 1 и 2
    if (abs(a - c), abs(b - d)) in [(2, 1), (1, 2)]:
        print(f"  Конь на ({a},{b}) угрожает полю ({c},{d})")
        break
