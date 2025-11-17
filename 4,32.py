n = int(input("Введите трехзначное число: "))
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10
square = n ** 2
sum_cubes = digit1**3 + digit2**3 + digit3**3
if square == sum_cubes:
    print("Квадрат числа равен сумме кубов его цифр")
else:
    print("Квадрат числа НЕ равен сумме кубов его цифр")
