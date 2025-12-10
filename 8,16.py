m = float(input("Введите m (0.5 < m < 1): "))
n = 1
while True:
    value = n / (n + 1)
    if value < m:
        print(f"{n}/{n+1} = {value:.3f}")
    else:
        break
    n += 1
m = float(input("Введите m (0.5 < m < 1): "))
for n in range(1, 10000):
    value = n / (n + 1)
    if value < m:
        print(f"{n}/{n+1} = {value:.3f}")
    else:
        break
