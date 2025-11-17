print("x = 465")
x = 465
A = x // 100
B = (x // 10) % 10
C = x % 10
result = A * 100 + C * 10 + B
print(f"Проверка: из {x} получили {result}")
