def is_power_of(x, base):
    if x <= 0:
        return False
    while x % base == 0:
        x //= base
    return x == 1
n = int(input("Введите число: "))
print(f"а) Степень числа 3: {is_power_of(n, 3)}")
print(f"б) Степень числа 5: {is_power_of(n, 5)}")
