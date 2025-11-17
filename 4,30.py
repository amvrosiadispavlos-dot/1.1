n = int(input("Введите трехзначное число: "))
digit1 = n // 100
digit2 = (n // 10) % 10
digit3 = n % 10
if digit1 == digit3:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
