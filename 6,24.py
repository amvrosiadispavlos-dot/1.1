n = int(input("n = "))
sign = 1
total = 0
temp = abs(n)
while temp > 0:
    total += sign * (temp % 10)
    sign = -sign
    temp //= 10
print("Знакочередующаяся сумма (с конца):", total)
n = int(input("n = "))
digits = []
temp = abs(n)
if temp == 0:
    digits = [0]
else:
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()
sign = 1
total = 0
for digit in digits:
    total += sign * digit
    sign = -sign
print("Знакочередующаяся сумма (с начала):", total)
