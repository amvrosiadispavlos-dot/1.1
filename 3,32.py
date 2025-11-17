print("x = 372")
x = 372
last_digit = x % 10
temp = (x - last_digit) // 10
result = last_digit * 100 + temp
print(f"Проверка: из {x} получили {result}")
