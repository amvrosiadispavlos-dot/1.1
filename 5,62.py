a = float(input("a = "))
n = int(input("n = "))
result = 1
for _ in range(abs(n)):
    result *= a
if n < 0:
    result = 1 / result
print(f"{a}^{n} = {result}")
