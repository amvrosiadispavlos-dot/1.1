def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
fractions = set()
for den in range(2, 8):
    for num in range(1, den):
        if gcd(num, den) == 1:
            fractions.add((num, den))
print("Простые несократимые дроби между 0 и 1 (знаменатель ≤ 7):")
for num, den in sorted(fractions, key=lambda x: x[0]/x[1]):
    print(f"{num}/{den}")
