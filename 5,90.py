n = int(input("n = "))
a, b = 1, 1
total = 2  
for _ in range(3, n + 1):
    a, b = b, a + b
    total += b
print("Сумма первых", n, "членов Фибоначчи чётная:", total % 2 == 0)
