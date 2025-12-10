def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input("Введите натуральное число n: "))
result = []
for i in range(1, n):
    if gcd(i, n) == 1:
        result.append(i)
print(f"Числа, взаимно простые с {n}: {result}")
