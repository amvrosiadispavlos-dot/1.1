a = int(input("a (неотрицательное) = "))
b = int(input("b (положительное) = "))
c = int(input("c = "))
d = int(input("d = "))
remainder = a % b
result = (remainder == c) or (remainder == d)
print("Остаток равен c или d:", result)
