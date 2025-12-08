def is_arithmetic(n, first, step):
    if step == 0:
        return n == first
    return (n - first) % step == 0 and (n - first) // step >= 0
f = int(input("Первый член прогрессии: "))
s = int(input("Шаг прогрессии: "))
n = int(input("Проверяемое число: "))
if is_arithmetic(n, f, s):
    print(f"{n} является членом арифметической прогрессии")
else:
    print(f"{n} не является членом арифметической прогрессии")
