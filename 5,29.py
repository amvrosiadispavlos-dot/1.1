total = 0
count = 0
for i in range(1, 751):
    total += i
    count += 1
average = total / count
print("Среднее от 1 до 750:", average)
b = int(input("b (≥150) = "))
total = 0
count = 0
for i in range(150, b + 1):
    total += i
    count += 1
average = total / count
print("Среднее от 150 до", b, ":", average)
a = int(input("a (≤200) = "))
total = 0
count = 0
for i in range(a, 201):
    total += i
    count += 1
average = total / count
print("Среднее от", a, "до 200:", average)
a = int(input("a = "))
b = int(input("b (≥a) = "))
total = 0
count = 0
for i in range(a, b + 1):
    total += i
    count += 1
average = total / count
print("Среднее от", a, "до", b, ":", average)
