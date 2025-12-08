num = int(input("n = "))
a = int(input("a (0-9) = "))
temp = abs(num)
count = 0
if temp == 0:
    count = 1 if a == 0 else 0
else:
    while temp > 0:
        if temp % 10 == a:
            count += 1
        temp //= 10
print(f"Цифра {a} встречается {count} раз")
num = int(input("n = "))
a = int(input("a (0-8) = "))
temp = abs(num)
total = 0
while temp > 0:
    digit = temp % 10
    if digit > a:
        total += digit
    temp //= 10
print(f"Сумма цифр > {a}: {total}")
num = int(input("n = "))
temp = abs(num)
total = 0
while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        total += digit
    temp //= 10
print("Сумма чётных цифр:", total)
num = int(input("n = "))
x = int(input("x (0-9) = "))
y = int(input("y (0-9) = "))
temp = abs(num)
count = 0
if temp == 0:
    if x == 0:
        count += 1
    if y == 0:
        count += 1
else:
    while temp > 0:
        digit = temp % 10
        if digit == x or digit == y:
            count += 1
        temp //= 10
print(f"Цифр {x} и {y} всего: {count}")
