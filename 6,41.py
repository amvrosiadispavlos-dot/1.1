num = int(input("n = "))
temp = abs(num)
if temp == 0:
    max_digit = 0
else:
    max_digit = 0
    while temp > 0:
        digit = temp % 10
        if digit > max_digit:
            max_digit = digit
        temp //= 10
print("Максимальная цифра:", max_digit)
num = int(input("n = "))
temp = abs(num)
if temp == 0:
    min_digit = 0
else:
    min_digit = 9
    while temp > 0:
        digit = temp % 10
        if digit < min_digit:
            min_digit = digit
        temp //= 10
print("Минимальная цифра:", min_digit)
