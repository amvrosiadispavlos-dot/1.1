x = 2
total = 0
power = 1  
for i in range(1, 12, 2): 
    total += x ** power / i
    power += 2
print("Сумма ряда:", total)
