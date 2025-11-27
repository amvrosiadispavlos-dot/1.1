total = 0
for num in range(30, 100):
    if num % 3 == 0 and (num % 10 in [2, 4, 8]):
        total += num
print("Сумма:", total)
