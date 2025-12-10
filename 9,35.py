denominations = [64, 32, 16, 8, 4, 2, 1]
n = int(input("Введите n: "))
for amount in range(n, n+11):
    temp = amount
    result = []
    for d in denominations:
        count = temp // d
        if count > 0:
            result.append((d, count))
        temp %= d
    print(f"Сумма {amount}: {result}")
