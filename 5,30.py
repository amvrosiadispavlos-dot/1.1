total = 0
for i in range(25, 41):
    total += i ** 3
print("Сумма кубов от 25 до 40:", total)
a = int(input("a (0-50) = "))
total = 0
for i in range(a, 51):
    total += i ** 2
print("Сумма квадратов от", a, "до 50:", total)
n = int(input("n (1-100) = "))
total = 0
for i in range(1, n + 1):
    total += i ** 2
print("Сумма квадратов от 1 до", n, ":", total)
a = int(input("a = "))
b = int(input("b (>a) = "))
total = 0
for i in range(a, b + 1):
    total += i ** 2
print("Сумма квадратов от", a, "до", b, ":", total)
