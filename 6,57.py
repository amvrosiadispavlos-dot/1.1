n = input("Введите натуральное число: ")
a = input("Введите цифру a: ")
b = input("Введите цифру b: ")
pos_a = -1
pos_b = -1
for i, digit in enumerate(n):
    if digit == a:
        pos_a = i
    if digit == b:
        pos_b = i
if pos_a == -1 or pos_b == -1:
    print("В числе нет цифр a и/или b")
else:
    if pos_a > pos_b:
        print(f"Цифра {a} расположена правее цифры {b}")
    else:
        print(f"Цифра {b} расположена правее цифры {a}")
