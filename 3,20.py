num = int(input("Введите трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
print("а) Число единиц:", units)
print("б) Число десятков:", tens)
print("в) Сумма цифр:", hundreds + tens + units)
print("г) Произведение цифр:", hundreds * tens * units)
