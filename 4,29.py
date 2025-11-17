n = int(input("Введите двузначное число: "))
a = int(input("Введите число a: "))
digit1 = n // 10
digit2 = n % 10
digit_sum = digit1 + digit2
if digit_sum % 3 == 0:
    print("а) Сумма цифр кратна трем")
else:
    print("а) Сумма цифр не кратна трем")
if a != 0 and digit_sum % a == 0:
    print("б) Сумма цифр кратна числу a")
else:
    print("б) Сумма цифр не кратна числу a")
