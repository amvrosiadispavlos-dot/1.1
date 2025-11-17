num = int(input("Введите трехзначное число: "))
hundreds = num // 100
remainder = num % 100 
new_num = remainder * 10 + hundreds
print("Число после перестановки:", new_num)
