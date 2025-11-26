n = int(input("Четырёхзначное число: "))
digits = [n // 1000, n // 100 % 10, n // 10 % 10, n % 10]
a = any(d in (2,7) for d in digits)
print("а) Входит 2 или 7:", a)
b = any(d in (3,6,9) for d in digits)
print("б) Входит 3, 6 или 9:", b)
