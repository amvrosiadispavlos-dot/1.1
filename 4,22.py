m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
if n == 0:
    print("Ошибка: деление на ноль")
elif m % n == 0:
    quotient = m // n
    print(f"Частное: {quotient}")
else:
    print(f"{m} на {n} нацело не делится")
