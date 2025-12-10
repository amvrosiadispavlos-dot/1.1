a = float(input("Введите a: "))
s = 0.0
n = 1
print(f"n, при которых сумма > {a}:")
while True:
    s += 1.0 / n
    if s > a:
        print(n, end=' ')
    n += 1
    if n > 100000:
        print("\n(вывод ограничен)")
        break
