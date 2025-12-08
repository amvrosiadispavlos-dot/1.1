n = int(input("n = "))
m = int(input("m = "))
total = 0
for _ in range(m):
    if n == 0:
        break
    total += n % 10
    n //= 10
print("Сумма последних", m, "цифр:", total)
