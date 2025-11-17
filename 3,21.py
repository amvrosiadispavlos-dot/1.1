num = int(input("Введите трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
reversed_num = units * 100 + tens * 10 + hundreds
print("Число справа налево:", reversed_num)
