a = int(input("a = "))
b = int(input("b = "))
quotient = 0
while a >= b:
    a -= b
    quotient += 1
print("Целая часть:", quotient)
a = int(input("a = "))
b = int(input("b = "))
while a >= b:
    a -= b
print("Остаток:", a)
