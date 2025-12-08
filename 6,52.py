n = input("Введите натуральное число: ")
has_3 = False
has_2 = False
has_5 = False
for digit in n:
    if digit == '3':
        has_3 = True
    if digit == '2':
        has_2 = True
    if digit == '5':
        has_5 = True
print("а) Есть ли цифра 3:", has_3)
print("б) Есть ли цифры 2 и 5:", has_2 and has_5)
