def is_leap_year(g):
    return (g % 400 == 0) or (g % 4 == 0 and g % 100 != 0)
g = int(input("Год: "))
m = int(input("Месяц: "))
n = int(input("Число: "))
days_in_month = [31, 29 if is_leap_year(g) else 28, 31, 30, 31, 30, 
                 31, 31, 30, 31, 30, 31]
prev_n = n - 1
prev_m = m
prev_g = g
if prev_n == 0:
    prev_m -= 1
    if prev_m == 0:
        prev_m = 12
        prev_g -= 1
    prev_n = days_in_month[prev_m - 1]
print(f"а) Предыдущий день: {prev_n}.{prev_m}.{prev_g}")
next_n = n + 1
next_m = m
next_g = g
if next_n > days_in_month[m - 1]:
    next_n = 1
    next_m += 1
    if next_m > 12:
        next_m = 1
        next_g += 1
print(f"б) Следующий день: {next_n}.{next_m}.{next_g}")
