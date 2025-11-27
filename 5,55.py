total = 0
sign = -1  
for i in range(1, 11):
    total += sign * (i ** 2)
    sign = -sign  
print("Сумма:", total)
