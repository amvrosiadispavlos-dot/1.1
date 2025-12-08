def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
n = int(input("Введите число: "))
if is_fibonacci(n):
    print(f"{n} является членом последовательности Фибоначчи")
else:
    print(f"{n} не является членом последовательности Фибоначчи")
