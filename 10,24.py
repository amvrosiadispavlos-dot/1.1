import random

def generate_position():
    return random.randint(1, 8), random.randint(1, 8)

# a) Ладья не угрожает полю (c, d)
a, b = generate_position()
while True:
    c, d = generate_position()
    if not (a == c or b == d):
        break
print(f"a) Ладья на ({a},{b}) не угрожает полю ({c},{d})")

# b) Слон не угрожает полю (c, d)
a, b = generate_position()
while True:
    c, d = generate_position()
    if abs(a - c) != abs(b - d):
        break
print(f"b) Слон на ({a},{b}) не угрожает полю ({c},{d})")

# c) Король может одним ходом попасть на поле (c, d)
a, b = generate_position()
while True:
    c, d = generate_position()
    if max(abs(a - c), abs(b - d)) == 1:
        break
print(f"c) Король на ({a},{b}) может попасть на поле ({c},{d}) за один ход")

# d) Ферзь не угрожает полю (c, d)
a, b = generate_position()
while True:
    c, d = generate_position()
    if not (a == c or b == d or abs(a - c) == abs(b - d)):
        break
print(f"d) Ферзь на ({a},{b}) не угрожает полю ({c},{d})")
