def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input("Введите n: "))
p = int(input("Введите p: "))
result = []
for i in range(1, n):
    if gcd(i, p) == 1:
        result.append(i)
print(f"Числа < {n}, взаимно простые с {p}: {result}")
