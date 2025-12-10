fib1, fib2 = 1, 1
total = 0
while fib1 <= 1000:
    total += fib1
    fib1, fib2 = fib2, fib1 + fib2
print(f"a) Сумма чисел Фибоначчи ≤ 1000: {total}")
n = int(input("Введите n (n > 1): "))
fib1, fib2 = 1, 1
while fib1 <= n:
    fib1, fib2 = fib2, fib1 + fib2
print(f"b) Первое число Фибоначчи > {n}: {fib1}")
