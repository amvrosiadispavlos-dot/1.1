def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
gcd_ab = gcd(a, b)
lcm_ab = abs(a * b) // gcd_ab
print(f"НОК({a}, {b}) = {lcm_ab}")
