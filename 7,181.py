numbers = list(map(int, input("Введите 20 чисел от 0 до 66 через пробел: ").split()[:20]))
def case_a():
    """Правая цифра числа — точки на правой половине кости"""
    for i in range(len(numbers) - 1):
        right_digit_current = numbers[i] % 10
        left_digit_next = numbers[i+1] // 10
        if right_digit_current != left_digit_next:
            return False
    return True
def case_b():
    """Любая из двух цифр может соответствовать правой/левой половине"""
    for i in range(len(numbers) - 1):
        a = numbers[i] // 10
        b = numbers[i] % 10
        c = numbers[i+1] // 10
        d = numbers[i+1] % 10
        return False
    return True
print("Случай а):", "Соответствует правилам" if case_a() else "Не соответствует")
print("Случай б):", "Соответствует правилам" if case_b() else "Не соответствует")
