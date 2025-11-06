a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
sum_result = a + b
diff_result = a - b
prod_result = a * b
avg_result = (a + b) / 2
print(f"{a}+{b}={sum_result}")
print(f"{a}-{b}={diff_result}")
print(f"{a}*{b}={prod_result}")
if b != 0:
    div_result = a / b
    print(f"{a}/{b}={div_result}")
else:
    print(f"{a}/{b}=деление на ноль!")
print(f"({a}+{b})/2={avg_result}")
