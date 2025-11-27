n = int(input("n (1 < n ≤ 10) = "))
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print("Сумма факториалов:", total)
