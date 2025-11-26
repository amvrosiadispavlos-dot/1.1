days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m = int(input("m (месяц): "))
n = int(input("n (число): "))
prev_n = n - 1
prev_m = m
if prev_n == 0:
    prev_m -= 1
    if prev_m == 0:
        prev_m = 12
    prev_n = days_in_month[prev_m - 1]
print(f"а) Предыдущий день: {prev_n}.{prev_m}")
next_n = n + 1
next_m = m
if next_n > days_in_month[m - 1]:
    next_n = 1
    next_m += 1
    if next_m > 12:
        next_m = 1
print(f"б) Следующий день: {next_n}.{next_m}")
