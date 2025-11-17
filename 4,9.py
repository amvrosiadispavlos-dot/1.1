a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if a > b:
    max_val = a
    min_val = b
else:
    max_val = b
    min_val = a
print(f"Максимальное: {max_val}")
print(f"Минимальное: {min_val}")
