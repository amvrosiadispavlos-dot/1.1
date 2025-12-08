n = input("Введите натуральное число: ")
pos_2 = -1
pos_5 = -1
for i, digit in enumerate(n):
    if digit == '2' and pos_2 == -1:
        pos_2 = i
    if digit == '5' and pos_5 == -1:
        pos_5 = i
if pos_2 == -1 or pos_5 == -1:
    print("В числе нет цифр 2 и/или 5")
else:
    if pos_2 < pos_5:
        print("Цифра 2 расположена левее цифры 5")
    else:
        print("Цифра 5 расположена левее цифры 2")
