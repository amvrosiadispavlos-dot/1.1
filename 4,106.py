from math import sqrt
x = float(input("x = "))
y = float(input("y = "))
if sqrt(y) < x:
    y *= 5
print("y =", y)
