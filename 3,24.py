num = int(input("Введите трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
new_num = tens * 100 + hundreds * 10 + units
print("Число после перестановки 1-й и 2-й цифр:", new_num)
