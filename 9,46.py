def digital_root(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num
n = int(input("Введите натуральное число: "))
print(f"Цифровой корень: {digital_root(n)}")
