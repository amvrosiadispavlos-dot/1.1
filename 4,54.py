n = int(input("Четырёхзначное число: "))
d1 = n // 1000
d2 = n // 100 % 10
d3 = n // 10 % 10
d4 = n % 10
a = (d1 == 4) or (d2 == 4) or (d3 == 4) or (d4 == 4)
print("а) Входит цифра 4:", a)
b_digit = int(input("Цифра b: "))
b = (d1 == b_digit) or (d2 == b_digit) or (d3 == b_digit) or (d4 == b_digit)
print("б) Входит цифра b:", b)
