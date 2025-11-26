n = int(input("Двузначное число: "))
d1 = n // 10
d2 = n % 10
a = (d1 == 3) or (d2 == 3)
print("а) Входит цифра 3:", a)
a_digit = int(input("Цифра a: "))
b = (d1 == a_digit) or (d2 == a_digit)
print("б) Входит цифра a:", b)
