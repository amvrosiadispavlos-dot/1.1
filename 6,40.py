num = int(input("n = "))
temp = abs(num)
first_digit = 0
if temp == 0:
    first_digit = 0
else:
    first_temp = temp
    while first_temp > 0:
        first_digit = first_temp % 10
        first_temp //= 10
count = 0
if temp == 0:
    count = 1 if first_digit == 0 else 0
else:
    while temp > 0:
        if temp % 10 == first_digit:
            count += 1
        temp //= 10
print(f"Первая цифра {first_digit} встречается {count} раз")
