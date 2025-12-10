m = float(input("Введите m (0.52 ≤ m ≤ 33.7): "))
x = 1
while x <= 100:
    y = (x*x + 100) / (x + 200)
    if y < m:
        print(f"x={x}, y={y:.3f}")
    x += 1
m = float(input("Введите m (0.52 ≤ m ≤ 33.7): "))
for x in range(1, 101):
    y = (x*x + 100) / (x + 200)
    if y < m:
        print(f"x={x}, y={y:.3f}")
