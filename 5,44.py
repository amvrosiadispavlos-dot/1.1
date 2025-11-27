n = int(input("n (≥3) = "))
a, b = 1, 1
for _ in range(3, n + 1):
    a, b = b, a + b
print(f"{n}-й член Фибоначчи: {b}")
n = int(input("n (≥3) = "))
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print("Первые", n, "членов Фибоначчи:", fib)
