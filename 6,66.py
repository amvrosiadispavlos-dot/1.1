def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
gcd_ab = gcd(a, b)
gcd_abc = gcd(gcd_ab, c)
print(f"НОД({a}, {b}, {c}) = {gcd_abc}")
