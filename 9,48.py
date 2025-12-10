n = int(input("Введите натуральное число: "))
temp = n
factors = []
i = 2
while i * i <= temp:
    while temp % i == 0:
        factors.append(i)
        temp //= i
    i += 1
if temp > 1:
    factors.append(temp)
print("1) Простые множители по одному разу:")
unique_factors = sorted(set(factors))
print(" * ".join(map(str, unique_factors)))

print("\n2) Простые множители с кратностями:")
from collections import Counter
counted = Counter(factors)
result = []
for factor, exp in sorted(counted.items()):
    if exp == 1:
        result.append(str(factor))
    else:
        result.append(f"{factor}^{exp}")
print(" * ".join(result))
