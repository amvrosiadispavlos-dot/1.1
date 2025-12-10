n = int(input("Введите натуральное число: "))
temp = n
factors = set()
i = 2
while i * i <= temp:
    while temp % i == 0:
        factors.add(i)
        temp //= i
    i += 1
if temp > 1:
    factors.add(temp)
print("Простые делители:", sorted(factors))
