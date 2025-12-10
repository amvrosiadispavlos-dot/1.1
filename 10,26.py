import random

def generate_position():
    return random.randint(1, 8), random.randint(1, 8)

def rook_threatens(a, b, c, d):
    return a == c or b == d

def bishop_threatens(a, b, c, d):
    return abs(a - c) == abs(b - d)

def queen_threatens(a, b, c, d):
    return rook_threatens(a, b, c, d) or bishop_threatens(a, b, c, d)

def knight_threatens(a, b, c, d):
    return (abs(a - c), abs(b - d)) in [(2, 1), (1, 2)]

def king_threatens(a, b, c, d):
    return max(abs(a - c), abs(b - d)) == 1

# Генерация позиций
a, b = generate_position()  # Белая фигура
c, d = generate_position()  # Черная фигура
e, f = generate_position()  # Целевое поле для белой

# Проверка для каждой комбинации фигур
combinations = [
    ("ладья", "ладья", rook_threatens, rook_threatens),
    ("ладья", "ферзь", rook_threatens, queen_threatens),
    ("ладья", "конь", rook_threatens, knight_threatens),
    ("ладья", "слон", rook_threatens, bishop_threatens),
    ("ферзь", "ферзь", queen_threatens, queen_threatens),
    ("ферзь", "ладья", queen_threatens, rook_threatens),
    ("ферзь", "конь", queen_threatens, knight_threatens),
    ("ферзь", "слон", queen_threatens, bishop_threatens),
    ("конь", "конь", knight_threatens, knight_threatens),
    ("конь", "ладья", knight_threatens, rook_threatens),
    ("конь", "ферзь", knight_threatens, queen_threatens),
    ("конь", "слон", knight_threatens, bishop_threatens),
    ("слон", "слон", bishop_threatens, bishop_threatens),
    ("слон", "ферзь", bishop_threatens, queen_threatens),
    ("слон", "конь", bishop_threatens, knight_threatens),
    ("слон", "ладья", bishop_threatens, rook_threatens),
    ("король", "слон", king_threatens, bishop_threatens),
    ("король", "ферзь", king_threatens, queen_threatens),
    ("король", "конь", king_threatens, knight_threatens),
    ("король", "ладья", king_threatens, rook_threatens),
]

print(f"Позиции: белая на ({a},{b}), черная на ({c},{d}), цель ({e},{f})")
print()

for white_name, black_name, white_move, black_threatens in combinations:
    # Может ли белая фигура пойти на (e,f)?
    can_move = white_move(a, b, e, f)
    # Подвергается ли белая фигура на (e,f) атаке черной?
    under_attack = black_threatens(c, d, e, f)
    
    if can_move and not under_attack:
        result = "МОЖЕТ"
    else:
        result = "НЕ МОЖЕТ"
    
    print(f"{white_name} vs {black_name}: {result}")
    if not can_move:
        print(f"  (белая фигура не может пойти на ({e},{f}))")
    elif under_attack:
        print(f"  (поле ({e},{f}) под атакой черной фигуры)")
