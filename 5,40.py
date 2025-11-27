num = int(input("9-значное число: "))
total = 0
for _ in range(9):
    total += num % 10  
    num //= 10  
print("Сумма цифр:", total)
