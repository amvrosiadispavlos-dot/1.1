x = int(input("x = "))
y = int(input("y = "))
product = 0
for _ in range(abs(y)):
    product += x
if y < 0:
    product = -product
print(f"{x} × {y} = {product}")
