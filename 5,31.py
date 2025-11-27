n = int(input("n = "))
total = 0
for i in range(n, 2 * n + 1):
    total += i ** 2
print("Сумма квадратов от", n, "до", 2 * n, ":", total)
