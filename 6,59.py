n = input("Введите натуральное число: ")
min_digit = '9'
count = 0
for digit in n:
    if digit < min_digit:
        min_digit = digit
        count = 1
    elif digit == min_digit:
        count += 1
print(f"Минимальная цифра {min_digit} встречается {count} раз(а)")
