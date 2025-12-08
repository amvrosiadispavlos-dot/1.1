a = int(input("a = "))
b = int(input("b = "))
quotient = 0
temp = abs(b)
abs_a = abs(a)
if a != 0:
    while temp >= abs_a:
        temp -= abs_a
        quotient += 1
    if (a < 0) != (b < 0):  # разные знаки
        quotient = -quotient
print("Целая часть:", quotient)
a = int(input("a = "))
b = int(input("b = "))
abs_a = abs(a)
if a != 0:
    remainder = abs(b)
    while remainder >= abs_a:
        remainder -= abs_a
    if b < 0:
        remainder = -remainder
    print("Остаток:", remainder)
else:
    print("Деление на ноль.")
