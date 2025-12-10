a = float(input("Введите a (начальное значение y0?): "))
x = float(input("Введите x: "))
eps = float(input("Введите ε: "))
y_prev = a
print(f"y0 = {y_prev}")
i = 1
while True:
    y = 0.5 * (y_prev + x / (y_prev - 1))
    diff_sq = abs(y2 - y_prev2)
    print(f"y{i} = {y:.5f}, |y{i}² - y{i-1}²| = {diff_sq:.6f}")
    if diff_sq < eps:
        print(f"Первый член, для которого |y_n² - y_{i-1}²| < {eps}: y{i} = {y:.5f}")
        break
    y_prev = y
    i += 1
