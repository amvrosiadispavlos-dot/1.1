a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
count = 0
if a < 0:
    count += 1
if b < 0:
    count += 1
if c < 0:
    count += 1
if d < 0:
    count += 1
print("Количество отрицательных:", count)
