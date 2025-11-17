num = int(input("Введите трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
new_num = hundreds * 100 + units * 10 + tens
print("Число после перестановки 2-й и 3-й цифр:", new_num)
