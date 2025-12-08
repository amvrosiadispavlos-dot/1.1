def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
a = int(input("Введите числитель a: "))
b = int(input("Введите знаменатель b: "))
d = gcd(a, b)
p = a // d
q = b // d
print(f"Сокращенная дробь: {p}/{q}")
