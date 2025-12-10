def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
p = int(input("Введите p: "))
q = int(input("Введите q: "))
result = []
for i in range(1, q+1):
    if q % i == 0 and gcd(i, p) == 1:
        result.append(i)
print(f"Делители {q}, взаимно простые с {p}: {result}")
