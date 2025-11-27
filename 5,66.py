total = 0
odd = 1
for i in range(1, 13):
    square = 0
    for _ in range(i):
        square += odd
        odd += 2
    total += square
print("Сумма квадратов:", total)
