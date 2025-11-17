print("x = 456")
x = 456
A = x // 100
B = (x // 10) % 10
C = x % 10
result = C * 100 + B * 10 + A
print(f"Проверка: из {x} получили {result}")
