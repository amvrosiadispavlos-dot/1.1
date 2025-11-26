n = int(input("Введите четырехзначное число: "))
a = int(input("Введите число a: "))
digit1 = n // 1000
digit2 = (n // 100) % 10
digit3 = (n // 10) % 10
digit4 = n % 10
sum_first_two = digit1 + digit2
sum_last_two = digit3 + digit4
total_sum = digit1 + digit2 + digit3 + digit4
product = digit1 * digit2 * digit3 * digit4
if sum_first_two == sum_last_two:
    print("а) Сумма первых двух цифр РАВНА сумме последних двух")
else:
    print("а) Сумма первых двух цифр НЕ РАВНА сумме последних двух")
if total_sum % 3 == 0:
    print("б) Сумма цифр кратна трем")
else:
    print("б) Сумма цифр не кратна трем")
if product % 4 == 0:
    print("в) Произведение цифр кратно четырем")
else:
    print("в) Произведение цифр не кратно четырем")
if a != 0 and product % a == 0:
    print(f"г) Произведение цифр кратно числу {a}")
else:
    print(f"г) Произведение цифр не кратно числу {a}")
