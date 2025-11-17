n = int(input("Введите двузначное число: "))
digit1 = n // 10 
digit2 = n % 10  
if digit1 > digit2:
    print("а) Первая цифра больше")
elif digit1 < digit2:
    print("а) Вторая цифра больше")
else:
    print("а) Цифры равны")
if digit1 == digit2:
    print("б) Цифры одинаковы")
else:
    print("б) Цифры различны")
