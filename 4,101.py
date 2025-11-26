a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print("Наибольшее:", max_val)
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
print("Наименьшее:", min_val)
