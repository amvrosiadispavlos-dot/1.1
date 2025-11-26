a = float(input("a = "))
b = float(input("b = "))
max_val = a
min_val = b
if b > a:
    max_val = b
    min_val = a
print("Наибольшее:", max_val)
print("Наименьшее:", min_val)
a = float(input("a = "))
b = float(input("b = "))
max_val = a
min_val = b
if b > a:
    max_val, min_val = b, a
print("Наибольшее:", max_val)
print("Наименьшее:", min_val)
