a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
sum_mult3 = 0
if a % 3 == 0:
    sum_mult3 += a
if b % 3 == 0:
    sum_mult3 += b
if c % 3 == 0:
    sum_mult3 += c
if d % 3 == 0:
    sum_mult3 += d
print("Сумма кратных трём:", sum_mult3)
