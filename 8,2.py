n = int(input("Введите n: "))
i = 1
while i * i <= n:
    i += 1
print(f"Первое число больше {n}: {i * i}")
n = int(input("Введите n: "))
for i in range(1, n + 2): 
    if i * i > n:
        print(f"Первое число больше {n}: {i * i}")
        break

