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
print(f"a) От конца числа: номер max = {max_pos_end}, номер min = {min_pos_end}")
print(f"б) От начала числа: номер max = {max_pos_start}, номер min = {min_pos_start}")
