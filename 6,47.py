n = int(input("Введите натуральное число с разными цифрами: "))
n_str = str(n)
min_digit = int(n_str[0])
max_digit = int(n_str[0])
min_pos = 0
max_pos = 0
for i, digit in enumerate(n_str):
    digit_int = int(digit)
    if digit_int < min_digit:
        min_digit = digit_int
        min_pos = i
    if digit_int > max_digit:
        max_digit = digit_int
        max_pos = i
if min_pos < max_pos:
    print("Минимальная цифра расположена левее")
else:
    print("Максимальная цифра расположена левее")
