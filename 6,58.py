n = input("Введите натуральное число: ")
max_digit = '0'
count = 0
for digit in n:
    if digit > max_digit:
        max_digit = digit
        count = 1
    elif digit == max_digit:
        count += 1
print(f"Максимальная цифра {max_digit} встречается {count} раз(а)")
