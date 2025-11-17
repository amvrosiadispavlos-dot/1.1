n = int(input("Введите двузначное число: "))
a = int(input("Введите число a: "))
digit1 = n // 10
digit2 = n % 10
digit_sum = digit1 + digit2
if digit_sum >= 10:
    print("а) Сумма цифр является двузначным числом")
else:
    print("а) Сумма цифр не является двузначным числом")
if digit_sum > a:
    print("б) Сумма цифр больше числа a")
else:
    print("б) Сумма цифр не больше числа a")
