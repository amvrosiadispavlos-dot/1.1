n = int(input("n = "))
a = float(input("a = "))
product = 0
for _ in range(abs(n)):
    product += a
if n < 0:
    product = -product
print(f"{n} × {a} = {product}")
