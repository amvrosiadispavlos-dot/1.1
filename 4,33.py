n = int(input("Введите трехзначное число: "))
a = int(input("Введите число a: "))
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10
digit_sum = digit1 + digit2 + digit3
digit_product = digit1 * digit2 * digit3
if 10 <= digit_sum <= 99:
    print("а) Сумма цифр является двузначным числом")
else:
    print("а) Сумма цифр не является двузначным числом")
if 100 <= digit_product <= 999:
    print("б) Произведение цифр является трехзначным числом")
else:
    print("б) Произведение цифр не является трехзначным числом")
if digit_product > a:
    print("в) Произведение цифр больше числа a")
else:
    print("в) Произведение цифр не больше числа a")
if digit_sum % 5 == 0:
    print("г) Сумма цифр кратна пяти")
else:
    print("г) Сумма цифр не кратна пяти")
if a != 0 and digit_sum % a == 0:
    print("д) Сумма цифр кратна числу a")
else:
    print("д) Сумма цифр не кратна числу a")
