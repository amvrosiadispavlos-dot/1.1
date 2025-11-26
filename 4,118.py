x = float(input("x = "))
if x <= 0:
    f = 0
elif 0 < x <= 1:
    f = x
else:
    f = x**2
print("f(x) =", f)
