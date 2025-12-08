n = int(input("Введите натуральное число с разными цифрами: "))
n_str = str(n)
min_digit = int(n_str[0])
max_digit = int(n_str[0])
min_pos_start = 1
max_pos_start = 1
min_pos_end = 1
max_pos_end = 1
for i, digit in enumerate(n_str):
    digit_int = int(digit)
    pos_end = len(n_str) - i
    if digit_int < min_digit:
        min_digit = digit_int
        min_pos_start = i + 1
        min_pos_end = pos_end
    if digit_int > max_digit:
        max_digit = digit_int
        max_pos_start = i + 1
        max_pos_end = pos_end
print(f"а) Порядковый номер максимальной цифры:")
print(f"   - от конца: {max_pos_end}")
print(f"   - от начала: {max_pos_start}")
print(f"б) Порядковый номер минимальной цифры:")
print(f"   - от конца: {min_pos_end}")
print(f"   - от начала: {min_pos_start}")
