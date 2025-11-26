a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
count = 0
if a % 2 == 0:
    count += 1
if b % 2 == 0:
    count += 1
if c % 2 == 0:
    count += 1
if d % 2 == 0:
    count += 1
print("Количество чётных:", count)
