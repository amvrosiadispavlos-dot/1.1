num = int(input("n = "))
count = 0
temp = abs(num)
if temp == 0:
    count = 1 if num == 3 else 0
else:
    while temp > 0:
        if temp % 10 == 3:
            count += 1
        temp //= 10
print("Цифр 3:", count)
num = int(input("n = "))
last_digit = abs(num) % 10
temp = abs(num)
count = 0
if temp == 0:
    count = 1 if last_digit == 0 else 0
else:
    while temp > 0:
        if temp % 10 == last_digit:
            count += 1
        temp //= 10
print(f"Цифра {last_digit} встречается {count} раз")
num = int(input("n = "))
temp = abs(num)
count = 0
if temp == 0:
    count = 1  
else:
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            count += 1
        temp //= 10
print("Чётных цифр:", count)
num = int(input("n = "))
temp = abs(num)
total = 0
while temp > 0:
    digit = temp % 10
    if digit > 5:
        total += digit
    temp //= 10
print("Сумма цифр >5:", total)
num = int(input("n = "))
temp = abs(num)
product = 1
found = False
if temp == 0:
    product = 0
else:
    while temp > 0:
        digit = temp % 10
        if digit > 7:
            product *= digit
            found = True
        temp //= 10
if not found:
    product = 0
print("Произведение цифр >7:", product)
num = int(input("n = "))
temp = abs(num)
count = 0
if temp == 0:
    count = 1 
else:
    while temp > 0:
        digit = temp % 10
        if digit == 0 or digit == 5:
            count += 1
        temp //= 10
print("Цифр 0 и 5 всего:", count)
