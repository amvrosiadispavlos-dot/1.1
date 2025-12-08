n = int(input("Введите сумму n: "))
denominations = [64, 32, 16, 8, 4, 2, 1]
counts = {}
remaining = n
for denom in denominations:
    count = remaining // denom
    if count > 0:
        counts[denom] = count
        remaining -= count * denom
print("Купюры для выплаты суммы:")
for denom in denominations:
    if denom in counts:
        print(f"Купюра {denom}: {counts[denom]} шт.")
