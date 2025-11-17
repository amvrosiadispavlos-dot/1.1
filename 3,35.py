n = int(input("Введите n (1 ≤ n ≤ 999): "))
for x in range(100, 1000):
    if (x % 100) * 10 + (x // 100) == n:
        print("x =", x)
        break
