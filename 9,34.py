n = int(input("Введите n (n < 100): "))
count = 0
for ten in range(0, n // 10 + 1):
    for five in range(0, (n - ten * 10) // 5 + 1):
        for two in range(0, (n - ten * 10 - five * 5) // 2 + 1):
            one = n - ten * 10 - five * 5 - two * 2
            if one >= 0:
                count += 1
print(f"а) Число способов выплаты: {count}")
print("\nб) Все способы выплаты:")
for ten in range(0, n // 10 + 1):
    for five in range(0, (n - ten * 10) // 5 + 1):
        for two in range(0, (n - ten * 10 - five * 5) // 2 + 1):
            one = n - ten * 10 - five * 5 - two * 2
            if one >= 0:
                parts = []
                if ten > 0:
                    parts.append(f"{ten}×10")
                if five > 0:
                    parts.append(f"{five}×5")
                if two > 0:
                    parts.append(f"{two}×2")
                if one > 0:
                    parts.append(f"{one}×1")
                print(" + ".join(parts))
