n = int(input("Введите натуральное число: "))
n_str = str(n)
min_digit = int(n_str[0])
max_digit = int(n_str[0])
for digit in n_str:
    digit_int = int(digit)
    if digit_int < min_digit:
        min_digit = digit_int
    if digit_int > max_digit:
        max_digit = digit_int
difference = max_digit - min_digit
if difference % 2 == 0:
    print(f"Разность {difference} является четным числом")
else:
    print(f"Разность {difference} является нечетным числом")
