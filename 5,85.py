a = int(input("a = "))
b = int(input("b = "))
total = 0
for num in range(a, b + 1):
    if num > 0 and num % 4 == 0:
        total += num
print("Сумма:", total)
