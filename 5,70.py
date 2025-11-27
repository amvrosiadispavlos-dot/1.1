n = int(input("n (1 < n ≤ 10) = "))
x = float(input("x = "))
total = 1.0
factorial = 1
power = 1
for i in range(1, n + 1):
    factorial *= i
    power *= x
    total += power / factorial
print("Сумма ряда:", total)
