n = int(input("n = "))
total = 0
temp = abs(n)
while temp > 0:
    total += temp % 10
    temp //= 10
print("Сумма цифр:", total)
n = int(input("n = "))
count = 0
temp = abs(n)
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
print("Количество цифр:", count)
n = int(input("n = "))
product = 1
temp = abs(n)
if temp == 0:
    product = 0
else:
    while temp > 0:
        product *= temp % 10
        temp //= 10
print("Произведение цифр:", product)
n = int(input("n = "))
temp = abs(n)
total = 0
count = 0
if temp == 0:
    total, count = 0, 1
else:
    while temp > 0:
        total += temp % 10
        count += 1
        temp //= 10
print("Среднее арифметическое цифр:", total / count)
n = int(input("n = "))
total = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    total += digit ** 2
    temp //= 10
print("Сумма квадратов цифр:", total)
n = int(input("n = "))
total = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
print("Сумма кубов цифр:", total)
n = int(input("n = "))
temp = abs(n)
while temp >= 10:
    temp //= 10
print("Первая цифра:", temp)
n = int(input("n = "))
temp = abs(n)
last = temp % 10
while temp >= 10:
    temp //= 10
first = temp
print("Сумма первой и последней цифры:", first + last)
