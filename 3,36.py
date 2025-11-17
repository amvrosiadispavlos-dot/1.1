print("x = 456")
x = 456
A = x // 100
B = (x // 10) % 10
C = x % 10
result = B * 100 + A * 10 + C
print(f"Проверка: из {x} получили {result}")
