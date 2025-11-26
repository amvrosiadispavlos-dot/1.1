n = int(input("Трёхзначное число: "))
d1 = n // 100
d2 = n // 10 % 10
d3 = n % 10
a = (d1 == 6) or (d2 == 6) or (d3 == 6)
print("а) Входит цифра 6:", a)
n_digit = int(input("Цифра n: "))
b = (d1 == n_digit) or (d2 == n_digit) or (d3 == n_digit)
print("б) Входит цифра n:", b)
