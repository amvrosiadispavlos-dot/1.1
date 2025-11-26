x = float(input("x = "))
if x < -1:
    y = -1
elif x <= 1:
    y = x
else:
    y = 1
print("а) y =", y)
x = float(input("x = "))
if x < -1:
    y = 1
elif x <= 1:
    y = -x
else:
    y = -1
print("б) y =", y)
x = float(input("x = "))
if x < 0:
    y = -1
elif x == 0:
    y = 0
else:
    y = 1
print("в) y =", y)
