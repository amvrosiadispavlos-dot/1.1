num = int(input("Введите двузначное число: "))
tens = num // 10
units = num % 10
reversed_num = units * 10 + tens
print("Число после перестановки цифр:", reversed_num)
