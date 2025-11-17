x = float(input("Введите x: "))
if x >= 0 and x <= 2:
    y = 2 - x
elif x > 2:
    y = 0
else:
    y = None  
    print("x должно быть ≥ 0")
if y is not None:
    print(f"y = {y}")
    x = float(input("Введите x (0 ≤ x ≤ 6): "))
if x >= 0 and x <= 3:
    y = 3 - x
elif x > 3 and x <= 6:
    y = x - 3
else:
    y = None
    print("x должен быть в диапазоне [0, 6]")
if y is not None:
    print(f"y = {y}")
