n = int(input("Введите трехзначное число: "))
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10
if digit1 == digit2 == digit3:
    print("а) Все цифры одинаковые")
else:
    print("а) Не все цифры одинаковые")
if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
    print("б) Среди цифр есть одинаковые")
else:
    print("б) Все цифры различны")
