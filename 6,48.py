n = int(input("Введите натуральное число: "))
n_str = str(n)
max_odd = -1
min_digit = int(n_str[0])
min_pos = 1
for i, digit in enumerate(n_str):
    digit_int = int(digit)
    if digit_int % 2 == 1 and digit_int > max_odd:
        max_odd = digit_int
    if digit_int < min_digit:
        min_digit = digit_int
        min_pos = i + 1
print(f"а) Максимальная нечетная цифра: {max_odd if max_odd != -1 else 'нет нечетных'}")
print(f"б) Номер минимальной цифры слева направо: {min_pos}")
