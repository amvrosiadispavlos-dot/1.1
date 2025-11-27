product = 1
for i in range(7, 15):
    product *= i
print("Произведение от 7 до 14:", product)
a = int(input("a (1-15) = "))
product = 1
for i in range(a, 16):
    product *= i
print("Произведение от", a, "до 15:", product)
b = int(input("b (1-10) = "))
product = 1
for i in range(1, b + 1):
    product *= i
print("Произведение от 1 до", b, ":", product)
a = int(input("a = "))
b = int(input("b (≥a) = "))
product = 1
for i in range(a, b + 1):
    product *= i
print("Произведение от", a, "до", b, ":", product)
