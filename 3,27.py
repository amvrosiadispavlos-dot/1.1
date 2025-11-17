num4 = int(input("Введите четырехзначное число: "))
thousands = num4 // 1000
hundreds = (num4 // 100) % 10
tens = (num4 // 10) % 10
units = num4 % 10
sum4 = thousands + hundreds + tens + units
print("Сумма цифр 4-значного числа:", sum4)
num5 = int(input("Введите пятизначное число: "))
tenthousands = num5 // 10000
thousands = (num5 // 1000) % 10
hundreds = (num5 // 100) % 10
tens = (num5 // 10) % 10
units = num5 % 10
sum5 = tenthousands + thousands + hundreds + tens + units
print("Сумма цифр 5-значного числа:", sum5)
