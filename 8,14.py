a = float(input("Введите a (0 < a <= 1): "))
n = 1
while True:
    value = 1.0 / n
    if value < a:
        print(f"Первое число меньше {a}: 1/{n} = {value:.5f}")
        break
    n += 1
a = float(input("Введите a (0 < a <= 1): "))
for n in range(1, 10000): 
    value = 1.0 / n
    if value < a:
        print(f"Первое число меньше {a}: 1/{n} = {value:.5f}")
        break
