n = int(input("n = "))
total = 0
sign = 1  
for i in range(1, n + 1):
    total += sign / i
    sign = -sign
    print("Сумма ряда:", total)
