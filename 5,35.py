n = int(input("n (≥2) = "))
total = 0
for i in range(1, n):
    total += i * (i + 1)
print("Сумма произведений:", total)
