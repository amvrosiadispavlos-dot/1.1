n = int(input("Введите трехзначное число: "))
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10
if digit1 > digit3:
    print("а) Первая цифра больше последней")
elif digit1 < digit3:
    print("а) Последняя цифра больше первой")
else:
    print("а) Первая и последняя цифры равны")
if digit1 > digit2:
    print("б) Первая цифра больше второй")
elif digit1 < digit2:
    print("б) Вторая цифра больше первой")
else:
    print("б) Первая и вторая цифры равны")
if digit2 > digit3:
    print("в) Вторая цифра больше последней")
elif digit2 < digit3:
    print("в) Последняя цифра больше второй")
else:
    print("в) Вторая и последняя цифры равны")
