n = int(input("Введите n (100 ≤ n ≤ 999): "))
A = n // 100
C = (n // 10) % 10
B = n % 10
x = A * 100 + B * 10 + C
print("x =", x)
