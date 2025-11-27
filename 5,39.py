x = 2
total = 0
sign = 1  
for i in range(0, 11):
    numerator = i + 1
    denominator = i + 2
    total += sign * (numerator / denominator) * (x ** i)
    sign = -sign
print("Сумма ряда:", total)
