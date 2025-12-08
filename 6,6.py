factorial = int(input("Факториал = "))
n = 1
product = 1
while product < factorial:
    n += 1
    product *= n
if product == factorial:
    print("Число n =", n)
else:
    print("Неверный факториал")
