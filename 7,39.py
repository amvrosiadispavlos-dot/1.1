n = int(input("Введите количество чисел n: "))
numbers = list(map(float, input(f"Введите {n} чисел через пробел: ").split()[:n]))
sum_abs = sum(abs(x) for x in numbers)
print(f"а) Сумма модулей: {sum_abs}")
prod_abs = 1
for x in numbers:
    prod_abs *= abs(x)
print(f"б) Произведение модулей: {prod_abs}")
pairs_sum = [numbers[i] + numbers[i+1] for i in range(n-1)]
print(f"в) Суммы соседних пар: {pairs_sum}")
alt_sum = 0
sign = 1
for x in numbers:
    alt_sum += sign * x
    sign = -sign  # меняем знак без возведения в степень
print(f"г) Знакопеременная сумма: {alt_sum}")
