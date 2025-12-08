n = int(input("Введите натуральное число: "))
a = int(input("Введите число a: "))
n_str = str(n)
min_digit = int(n_str[0])
max_digit = int(n_str[0])
for digit in n_str:
    digit_int = int(digit)
    if digit_int < min_digit:
        min_digit = digit_int
    if digit_int > max_digit:
        max_digit = digit_int
sum_min_max = min_digit + max_digit
if sum_min_max % a == 0:
    print(f"Сумма {sum_min_max} кратна {a}")
else:
    print(f"Сумма {sum_min_max} не кратна {a}")
