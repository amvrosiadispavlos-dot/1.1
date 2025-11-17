n = int(input("Введите двузначное число: "))
digit1 = n // 10
digit2 = n % 10
square = n ** 2
sum_cubes = 4 * (digit1**3 + digit2**
                 3)
if square == sum_cubes:
    print("Квадрат числа равен учетверенной сумме кубов его цифр")
else:
    print("Квадрат числа НЕ равен учетверенной сумме кубов его цифр")
