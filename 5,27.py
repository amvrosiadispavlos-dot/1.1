total = 0
for i in range(200, 601):
    total += i
print("Сумма от 200 до 600:", total)
a = int(input("a (≤400) = "))
total = 0
for i in range(a, 401):
    total += i
print("Сумма от", a, "до 400:", total)
b = int(input("b (≥-15) = "))
total = 0
for i in range(-15, b + 1):
    total += i
print("Сумма от -15 до", b, ":", total)
a = int(input("a = "))
b = int(input("b (≥a) = "))
total = 0
for i in range(a, b + 1):
    total += i
print("Сумма от", a, "до", b, ":", total)
